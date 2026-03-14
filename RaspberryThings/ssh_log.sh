
#!/bin/bash

current_date_time="$(date)"
username="$(whoami)"
client_info="$SSH_CLIENT"

# log SSH info connection to a file
echo "${current_date_time}, ${username}, ${client_info}. Log in recorded." >> /var/log/ssh_log.log

# send alert details to telegram
curl -s -X POST https://api.telegram.org/bot"000000000:XXXXXXXXXX-XXXXXXXXXXXXX"/sendMessage -d chat_id="000000000" -d text="SSH Connection - ${current_date_time}, ${username}, ${client_info}" "
