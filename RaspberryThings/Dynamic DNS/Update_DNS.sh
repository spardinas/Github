# Set variables
LAST_IP_FILE="/path/to/last_ip.txt" # Path to the file storing the last known IP address
LAMBDA_NAME="updateDNS"          # Name of the AWS Lambda function to update DNS
AWS_PROFILE="default"            # AWS CLI profile name configured with AWS credentials in ~/.aws/credentials
LOG_FILE="/path/to/update-ip.log" # Log file to record IP changes
CURRENT_IP=$(curl -s https://ifconfig.co)

# Check if the log file exists, if not create it
if [[ -f "$LAST_IP_FILE" ]]; then
  LAST_IP=$(cat "$LAST_IP_FILE")
else
  LAST_IP=""
fi

# Check if the current IP is the same as the last known IP
if [[ "$CURRENT_IP" == "$LAST_IP" ]]; then
  echo "$(date): IP unchanged ($CURRENT_IP)" >> "$LOG_FILE"
  # Send a message to Telegram with the IP
  # Only because I want to know the current IP
  curl -s -X POST https://api.telegram.org/bot"XXXXXXXX:XXXXXXXXXXXXXXXXXXXXXXXXXXXX"/sendMessage -d chat_id="0000000000" -d text="IP: $( wget -qO- ifconfig.co | awk '{ print $1}')"
  exit 0
fi

# If the IP has changed, log the change and update the last known IP
echo "$(date): IP changed from $LAST_IP to $CURRENT_IP" >> "$LOG_FILE"
echo "$CURRENT_IP" > "$LAST_IP_FILE"
# Send a message to Telegram with the IP
# Only because I want to know the new IP
curl -s -X POST https://api.telegram.org/bot"XXXXXXXX:XXXXXXXXXXXXXXXXXXXXXXXXXXXX"/sendMessage -d chat_id="0000000000" -d text="IP: $( wget -qO- ifconfig.co | awk '{ print $1}')"

# Invoke the AWS Lambda function to update DNS with the new IP
PAYLOAD='{"ip":"'"$CURRENT_IP"'"}'
aws lambda invoke \
  --function-name "$LAMBDA_NAME" \
  --profile "$AWS_PROFILE" \
  --payload "$PAYLOAD" \
  /dev/stdout >> "$LOG_FILE" 2>&1


exit 0
