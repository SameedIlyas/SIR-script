# System Information Retrieval Script

This script retrieves various pieces of system information and displays them in a human-readable format. The information includes public and internal IP addresses, a censored MAC address, top CPU-consuming processes, memory usage, active system services, and the largest files in the `/home` directory.

## Features

- **Public IP Address**: Retrieves the public IP address using the `curl` command.
- **Internal IP Address**: Retrieves the internal IP address using the `hostname` command.
- **Censored MAC Address**: Retrieves and censors the MAC address of the default network interface.
- **Top CPU Processes**: Displays the top 5 processes by CPU usage with formatted headers.
- **Memory Usage**: Displays the current memory usage in a human-readable format.
- **Active System Services**: Lists the active system services managed by `systemctl`.
- **Largest Files in /home Directory**: Finds and lists the top 10 largest files in the `/home` directory.

## Usage

### Running the Script

1. Save the script to a file, e.g., `system_info.sh`.
2. Make the script executable:
    ```bash
    chmod +x system_info.sh
    ```
3. Run the script:
    ```bash
    ./system_info.sh
    ```

### Script Output

The script will output the following information:

1. **Public IP Address**: Your external IP address.
2. **Internal IP Address**: Your internal IP address within the local network.
3. **Censored MAC Address**: The MAC address with the first three octets censored for privacy.
4. **Top CPU Processes**: A table of the top 5 processes by CPU usage.
5. **Memory Usage**: Current memory usage statistics.
6. **Active System Services**: The first 10 active system services.
7. **Largest Files in /home Directory**: The top 10 largest files in the `/home` directory.

### Example Output
![Output](https://github.com/SameedIlyas/SIR-script/assets/127698326/cb4de81a-9cfd-496b-b3db-dfbc13415c7f)

## Dependencies

The script uses the following commands:
- `curl`
- `hostname`
- `ip`
- `awk`
- `ps`
- `free`
- `systemctl`
- `find`
- `du`

Ensure these commands are available on your system before running the script.

---

This README provides an overview of the script's functionality, usage instructions, example output, and other relevant information for users.

