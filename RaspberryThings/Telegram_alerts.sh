#!/bin/bash

# Telegram Configuration
chat_id="-100XXXXXXXXXX" # Reemplaza con tu chat_id
bot_token="XXXXXXXXXX:XXXXXXXXXXXXXXXXXXXXXXXXXX" # Reemplaza con tu token de bot
api_url="https://api.telegram.org/bot${bot_token}/sendDocument" # URL to send the pictures
msg_url="https://api.telegram.org/bot${bot_token}/sendMessage" # URL to send alerts

# File/Directory Configuration
output_dir="/path/to/Pictures/"
log_file="/path/to/Logs/capture_log_$(date +"%Y%m%d").log"
timestamp=$(date +"%Y_%m_%d_%H_%M") 
resolution="800x600"

# Camera List by name|URL
cameras=(
  "cam1|rtsp://admin:password@XX.XX.XX.XX/stream1"
  "cam2|rtsp://admin:password@XX.XX.XX.XX/stream1"
)

# General variables
total_cameras=0
error_count=0

# Logging function
log() {
  echo "[$(date +"%Y-%m-%d %H:%M:%S")] $1" >> "$log_file"
}

# Function to send alert messages to Telegram
send_alert() {
  local message="$1"
  curl -s -X POST "${msg_url}" \
    -d "chat_id=${chat_id}" \
    -d "text=🚨 ${message}" > /dev/null
}

# Function to capture image and send to Telegram
capture_and_send() {
  local name="$1"
  local url="$2"
  local output_file="${output_dir}/${name}-${timestamp}.jpg"
  ((total_cameras++))

  log "Capturing image from ${name}..."

  if ffmpeg -y -loglevel error -rtsp_transport tcp -i "${url}" -frames:v 1 -s ${resolution} "${output_file}"; then
    log "✅ Image from ${name} obtained."
    
    if curl -s -F "chat_id=${chat_id}" -F "document=@${output_file}" "${api_url}" > /dev/null; then
  log "📤 Imagen de ${name} enviada correctamente."

  # Eliminar la imagen local
  rm -f "${output_file}" && log "🗑️ Imagen ${output_file} eliminada del disco."
else
  log "⚠️ Error al enviar imagen de ${name}."
  send_alert "Error al enviar la imagen de *${name}* a Telegram."
  ((error_count++))
fi



# Proccess cameras
for cam in "${cameras[@]}"; do
  IFS="|" read -r name url <<< "${cam}"
  capture_and_send "$name" "$url"
done

# Sending alert if an error occurred
if [[ $error_count -gt 0 ]]; then
  send_alert "Summary: ${error_count} of ${total_cameras} camera(s) failed."
  log "Summary: ${error_count}/${total_cameras} cowith errors."
else
  log "✅ All of ${total_cameras} cameras proccesed correclty."
fi

# Clean up old ( +7 days) images
find "${output_dir}" -type f -name "*.jpg" -mtime +7 -exec rm -f {} \; \
  -exec echo "🧹 Old picture removed: {}" >> "$log_file" \;