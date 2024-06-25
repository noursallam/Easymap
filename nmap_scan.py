import subprocess
import time

def print_with_delay(message, delay=2):
    print(message)
    time.sleep(delay)

def check_nmap_exist():
    try:
        subprocess.run(['nmap', '-v'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        print("NMAP exists [yes]")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        while True:
            print_with_delay('You do not have nmap installed. Install it? (y/n)')
            install = input().strip().lower()
            if install == 'y':
                print_with_delay("Installing nmap...")
                # Code to install nmap goes here
                return True
            elif install == 'n':
                return False
            else:
                print("Invalid input. Please enter 'y' to install or 'n' to skip.")

def print_nmap_option_info(option_number):
    nmap_options = {
        1: {
            'option': '-sP',
            'description': 'Ping Scan - Determines which hosts are up.',
            'use_case': 'Use when you want to discover live hosts without scanning for open ports.',
            'example': 'nmap -sP 192.168.1.0/24'
        },
        2: {
            'option': '-sS',
            'description': 'TCP SYN Scan - Fast and stealthy scan.',
            'use_case': 'Use for fast and stealthy scans on large networks or to avoid detection by firewalls.',
            'example': 'nmap -sS 192.168.1.1'
        },
        3: {
            'option': '-sU',
            'description': 'UDP Scan - Scans for open UDP ports.',
            'use_case': 'Use to discover open UDP ports, though it is slower and more resource-intensive.',
            'example': 'nmap -sU 192.168.1.1'
        },
        4: {
            'option': '-sV',
            'description': 'Version Detection - Determines service version.',
            'use_case': 'Use to identify the version of services running on open ports.',
            'example': 'nmap -sV 192.168.1.1'
        },
        5: {
            'option': '-O',
            'description': 'OS Detection - Identifies the operating system.',
            'use_case': 'Use to determine the OS running on a host for tailored attacks or defenses.',
            'example': 'nmap -O 192.168.1.1'
        },
        6: {
            'option': '-A',
            'description': 'Aggressive Scan - Comprehensive scan including OS detection and more.',
            'use_case': 'Use for a detailed scan including OS detection, version detection, and script scanning. This scan is more intrusive.',
            'example': 'nmap -A 192.168.1.1'
        },
        7: {
            'option': '-T0',
            'description': 'Paranoid Timing Template - Very slow scan speed.',
            'use_case': 'Use when you want to avoid detection and have plenty of time for the scan.',
            'example': 'nmap -T0 192.168.1.1'
        },
        8: {
            'option': '-T1',
            'description': 'Sneaky Timing Template - Slower scan speed.',
            'use_case': 'Use when you want to slow down the scan to reduce network traffic and increase stealth.',
            'example': 'nmap -T1 192.168.1.1'
        },
        9: {
            'option': '-T2',
            'description': 'Polite Timing Template - Normal scan speed.',
            'use_case': 'Use as a default timing template for normal network scanning.',
            'example': 'nmap -T2 192.168.1.1'
        },
        10: {
            'option': '-T3',
            'description': 'Normal Timing Template - Faster scan speed.',
            'use_case': 'Use when you want a faster scan but still want to avoid causing too much network disruption.',
            'example': 'nmap -T3 192.168.1.1'
        },
        11: {
            'option': '-T4',
            'description': 'Aggressive Timing Template - Faster scan speed.',
            'use_case': 'Use for faster scans where speed is prioritized over stealth.',
            'example': 'nmap -T4 192.168.1.1'
        },
        12: {
            'option': '-T5',
            'description': 'Insane Timing Template - Very fast scan speed.',
            'use_case': 'Use when you need the fastest scan possible, even if it may cause significant network disruption.',
            'example': 'nmap -T5 192.168.1.1'
        },
        13: {
            'option': '-p',
            'description': 'Port Specification - Scans specific ports.',
            'use_case': 'Use to scan specific ports, useful for targeting known services or reducing scan time.',
            'example': 'nmap -p 80,443 192.168.1.1'
        },
        14: {
            'option': '--script',
            'description': 'Script Scan - Runs specific Nmap scripts.',
            'use_case': 'Use to run specific Nmap scripts for vulnerability checks, service enumeration, and more.',
            'example': 'nmap --script=vuln 192.168.1.1'
        },
        15: {
            'option': '-oN',
            'description': 'Output Normal - Saves scan results to a file.',
            'use_case': 'Use to save scan results in a human-readable format for documentation and analysis.',
            'example': 'nmap -oN scan_results.txt 192.168.1.1'
        },
        16: {
            'option': '-O',
            'description': 'IP Protocol Scan - Determines which IP protocols (TCP, UDP, ICMP, etc.) are supported by hosts.',
            'use_case': 'Use when you need to determine which IP protocols are supported by hosts on a network.',
            'example': 'nmap -O 192.168.1.1'
        },
        17: {
            'option': '-sC',
            'description': 'Default Script Scan - Runs a default set of Nmap scripts.',
            'use_case': 'Use when you want to run the default set of Nmap scripts for basic service enumeration and vulnerability detection.',
            'example': 'nmap -sC 192.168.1.1'
        },
        18: {
            'option': '-sW',
            'description': 'TCP Window Scan - Determines open ports by examining TCP window size.',
            'use_case': 'Use when you want to detect open ports by analyzing TCP window size.',
            'example': 'nmap -sW 192.168.1.1'
        },
        19: {
            'option': '-sN',
            'description': 'TCP Null Scan - Attempts to open a TCP connection without setting any flags.',
            'use_case': 'Use when you want to test how firewalls or intrusion detection systems (IDS) handle TCP connections with no flags set.',
            'example': 'nmap -sN 192.168.1.1'
        },
        20: {
            'option': '-sF',
            'description': 'TCP FIN Scan - Attempts to open a TCP connection by sending a TCP FIN flag.',
            'use_case': 'Use when you want to test how firewalls or IDS handle TCP connections closed by sending a TCP FIN flag.',
            'example': 'nmap -sF 192.168.1.1'
        },
    }

    if option_number in nmap_options:
        option_info = nmap_options[option_number]
        print(f"\nOption: {option_info['option']}")
        print(f"Description: {option_info['description']}")
        print(f"When to Use: {option_info['use_case']}")
        print(f"Example: {option_info['example']}\n")
        return option_info['option']
    else:
        print("Invalid option number. Please try again.")
        return None

def print_menu():
    print("|EASYMAP Options Guide")
    print("------------------")
    print("1. Ping Scan (-sP)")
    print("2. TCP SYN Scan (-sS)")
    print("3. UDP Scan (-sU)")
    print("4. Version Detection (-sV)")
    print("5. OS Detection (-O)")
    print("6. Aggressive Scan (-A)")
    print("7. Paranoid Timing Template (-T0)")
    print("8. Sneaky Timing Template (-T1)")
    print("9. Polite Timing Template (-T2)")
    print("10. Normal Timing Template (-T3)")
    print("11. Aggressive Timing Template (-T4)")
    print("12. Insane Timing Template (-T5)")
    print("13. Port Specification (-p)")
    print("14. Script Scan (--script)")
    print("15. Output Normal (-oN)")
    print("16. IP Protocol Scan (-O)")
    print("17. Default Script Scan (-sC)")
    print("18. TCP Window Scan (-sW)")
    print("19. TCP Null Scan (-sN)")
    print("20. TCP FIN Scan (-sF)")
    print("0. Exit")
    print("------------------")

def print_flag():
    flag = """
███████  █████  ███████ ██    ██     ███    ███  █████  ██████  
██      ██   ██ ██       ██  ██      ████  ████ ██   ██ ██   ██ 
█████   ███████ ███████   ████       ██ ████ ██ ███████ ██████  
██      ██   ██      ██    ██        ██  ██  ██ ██   ██ ██      
███████ ██   ██ ███████    ██        ██      ██ ██   ██ ██        
by/nour sallam  https://github.com/noursallam               
    """
    print(flag)

if __name__ == "__main__":
    if check_nmap_exist():
        print_flag()
        print_menu()
        while True:
            try:
                choice = int(input("Enter the number of the option you want to learn about (0 to exit): "))
                if choice == 0:
                    print("Exiting Nmap Options Guide. Goodbye!")
                    break
                else:
                    option = print_nmap_option_info(choice)
                    if option:
                        print('Do you want to perform this scan? (y/n): ')
                        answer = input().strip().lower()
                        if answer == 'y':
                            print('Enter the target IP: ')
                            ip = input().strip()
                            print('Enter the port(s) (comma-separated for multiple ports or leave blank for all ports): ')
                            port = input().strip()
                            scan_command = ['sudo','nmap', option, ip]
                            if port:
                                scan_command.extend(['-p', port])
                            result = subprocess.run(scan_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                            print_with_delay("Scanning...")
                            print(result.stdout)
                            print(result.stderr)
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 20.")

