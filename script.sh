#!/bin/bash

# Begin script execution
echo -e "Starting system information retrieval\n"

# Retrieve public IP address using curl
public_ip=$(curl -s http://ipecho.net/plain)
echo -e "Your Public IP is: $public_ip\n"

# Retrieve internal IP address using hostname command
internal_ip=$(hostname -I | cut -d' ' -f1)
echo -e "Your Internal IP is: $internal_ip\n"

#retrieve and censor the MAC address of the default network interface
default_interface=$(ip route | grep default | awk '{print $5}')
mac_address=$(ip link show $default_interface | awk '/ether/ {print $2}')
censored_mac=$(echo $mac_address | awk 'BEGIN {FS=":"; OFS=":"} {for(i=1;i<=3;i++) $i="XX"; print}')
echo -e "Your MAC address is: $censored_mac\n"

# Display the top 5 processes by CPU usage with headers
echo "Displaying the top 5 processes by CPU usage."
printf "%-8s %-6s %-10s\n" "PID" "%CPU" "COMMAND"  # Print headers with fixed width
ps -eo pid,%cpu,cmd --sort=-%cpu | awk 'NR>1 {printf "%-8s %-6s %-10s\n", $1, $2, $3}' | head -n 6
echo -e "\n"  # Adds an extra line for spacing

# Display memory usage using free
echo "Displaying memory usage."
free -h
echo -e "\n"  # Adds an extra line for spacing

# Display active system services using systemctl
echo "Displaying active system services."
systemctl list-units --type=service --state=running | head -n 10
echo -e "\n"  # Adds an extra line for spacing

# Display the top 10 largest files in the /home directory using du and find
echo "Displaying the top 10 largest files in the /home directory."
find /home -type f -exec du -h {} + | sort -rh | head -n 10
echo -e "\n"  # Adds an extra line for spacing

# End of script
echo "System information retrieval complete."
