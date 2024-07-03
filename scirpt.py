import os
import subprocess
import requests

def get_public_ip():
    try:
        response = requests.get("http://ipecho.net/plain")
        return response.text
    except requests.RequestException as e:
        return f"Error retrieving public IP: {e}"

def get_internal_ip():
    result = subprocess.run(["hostname", "-I"], capture_output=True, text=True)
    return result.stdout.strip().split()[0]

def get_mac_address():
    result = subprocess.run(["ip", "route"], capture_output=True, text=True)
    default_interface = [line.split()[4] for line in result.stdout.splitlines() if "default" in line][0]
    result = subprocess.run(["ip", "link", "show", default_interface], capture_output=True, text=True)
    mac_address = [line.split()[1] for line in result.stdout.splitlines() if "ether" in line][0]
    censored_mac = ':'.join(['XX' if i < 3 else part for i, part in enumerate(mac_address.split(':'))])
    return censored_mac

def get_top_cpu_processes():
    result = subprocess.run(["ps", "-eo", "pid,%cpu,cmd", "--sort=-%cpu"], capture_output=True, text=True)
    lines = result.stdout.strip().splitlines()
    top_processes = "\n".join(lines[:6])
    return top_processes

def get_memory_usage():
    result = subprocess.run(["free", "-h"], capture_output=True, text=True)
    return result.stdout.strip()

def get_active_services():
    result = subprocess.run(["systemctl", "list-units", "--type=service", "--state=running"], capture_output=True, text=True)
    lines = result.stdout.strip().splitlines()
    active_services = "\n".join(lines[:10])
    return active_services

def get_top_largest_files():
    result = subprocess.run(["find", "/home", "-type", "f", "-exec", "du", "-h", "{}", "+"], capture_output=True, text=True)
    lines = result.stdout.strip().splitlines()
    sorted_lines = sorted(lines, key=lambda x: float(x.split()[0].replace('G', '').replace('M', '').replace('K', '')), reverse=True)
    top_files = "\n".join(sorted_lines[:10])
    return top_files

def main():
    print("Starting system information retrieval\n")

    public_ip = get_public_ip()
    print(f"Your Public IP is: {public_ip}\n")

    internal_ip = get_internal_ip()
    print(f"Your Internal IP is: {internal_ip}\n")

    mac_address = get_mac_address()
    print(f"Your MAC address is: {mac_address}\n")

    print("Displaying the top 5 processes by CPU usage.")
    print(f"{'PID':<8} {'%CPU':<6} {'COMMAND':<10}")
    print(get_top_cpu_processes())
    print("\n")

    print("Displaying memory usage.")
    print(get_memory_usage())
    print("\n")

    print("Displaying active system services.")
    print(get_active_services())
    print("\n")

    print("Displaying the top 10 largest files in the /home directory.")
    print(get_top_largest_files())
    print("\n")

    print("System information retrieval complete.")

if __name__ == "__main__":
    main()
