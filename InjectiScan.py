import nmap
import os
import socket
import pyfiglet

# Define color variables
YELLOW = "\033[93m"
WHITE = "\033[97m"
CYAN = "\033[96m"
GREEN = "\033[92m"
RED = "\033[91m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

def print_banner():

    banner = pyfiglet.figlet_format("Injecti  Scan")
    print(f"{GREEN}{banner}{RESET}")
    print(f"{GREEN}Developed by Ayush Kumar{RESET}")
    print(f"{GREEN}GitHub: https://github.com/0xHawkEye{RESET}")
    print(f"{GREEN}Linkedin: https://www.linkedin.com/in/ayushkr4422{RESET}")
    print()
    print()


def scan_ports(ip):
    nm = nmap.PortScanner()
    print(GREEN + "[*] Scanning ports on " + ip + RESET)
    try:
        nm.scan(ip)
    except KeyboardInterrupt:
        print(RED + "\n[!] Port scan interrupted by user." + RESET)
        return
    except:
        print(RED + "[!] Error while scanning ports." + RESET)
        return
    for host in nm.all_hosts():
        print(GREEN + f"[*] Host : {host} ({nm[host].hostname()})" + RESET)
        print(GREEN + f"[*] Status : {nm[host].state()}" + RESET)
        for proto in nm[host].all_protocols():
            print(GREEN + f"[*] Protocol : {proto}" + RESET)
            ports = nm[host][proto].keys()
            for port in sorted(ports):
                state = nm[host][proto][port]['state']
                color = GREEN if state == 'open' else RED
                print(color + f"[*] Port : {port} Status : {state}" + RESET)

def scan_services(ip):
    print(GREEN + "[*] Scanning services on " + ip + RESET)
    try:
        for port in range(1, 65536):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "unknown"
                print(GREEN + f"[*] Port : {port} Service : {service}" + RESET)
            sock.close()
    except KeyboardInterrupt:
        print(RED + "\n[!] Service scan interrupted by user." + RESET)
        return
    except:
        print(RED + "[!] Error scanning services." + RESET)
        return

def sql_injection_scan(url):
    print(GREEN + "[*] Scanning for SQL injection vulnerabilities at " + url + RESET)
    try:
        os.system("sqlmap -u " + url)
    except KeyboardInterrupt:
        print(RED + "\n[!] SQL injection scan interrupted by user." + RESET)
        return
    except:
        print(RED + "[!] Error scanning for SQL injection vulnerabilities." + RESET)
        return

def main():
    print_banner()

    while True:
        print(CYAN + "[+] What do you want to audit?" + RESET)
        print("1. Port Scanning")
        print("2. Service Scanning")
        print("3. SQL Injection Scanning")
        print("4. Exit")
        choice = input(GREEN + "> " + RESET)
        if choice == "1":
            ip = input(CYAN + "[*] Enter the IP or domain to scan: " + RESET)
            scan_ports(ip)
            input("\nPress Enter to continue...")
            os.system("cls" if os.name == "nt" else "clear")
            print_banner()
        elif choice == "2":
            ip = input(CYAN + "[*] Enter the IP or domain to scan: " + RESET)
            scan_services(ip)
            input("\nPress Enter to continue...")
            os.system("cls" if os.name == "nt" else "clear")
            print_banner()
        elif choice == "3":
            url = input(CYAN + "[*] Enter the URL to perform SQL injection testing: " + RESET)
            sql_injection_scan(url)
            input("\nPress Enter to continue... ")
            os.system("cls" if os.name == "nt" else "clear")
            print_banner()
        elif choice == "4":
            print(RED + "[*] Exiting the program..." + RESET)
            print(GREEN + "[+] Happy hacking ;)" + RESET)
            exit()
        else:
            print(RED + "[!] Invalid option." + RESET)

if __name__ == "__main__":
    main()
