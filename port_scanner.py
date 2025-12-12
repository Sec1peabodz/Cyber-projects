import socket   #network connection
import sys  #for system operation like exiting
from datetime import datetime #timestamps of scans

def port_scan(target, port):
    """
    Attempts to connect to a specific port on the target machine.
    True if port open , otherwise false statement
    """
    try:
        #Create a socket object (AF_INET = IPV4, SOCK_STREAM = TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #Set timeout of 1 sec
        socket.setdefaulttimeout(1)

        #Try to connect to target IP
        result = s.connect_ex((target,port))

        #Close the socket connection
        s.close()

        #connect_ex returns 0 if connection succesfull
        return result == 0
    except socket.gaierror:
        print(f"Hostname could not be resolved")
        return False
    except socket.error:
        print(f"Could not connect to server")
        return False
    
def scan_range(target, start_port, end_port):
    """       
    Scans a range of ports on the target host.
    
    """
    print("-" * 50)
    print(f"Scanning Target: {target}")
    print(f"Range of Ports: {start_port}-{end_port}")
    print(f"Scan started at: {datetime.now()}")
    print("-" * 50)

    open_ports = []

    try:
        #Loop through each port in range 
        for port in range(start_port, end_port + 1):
            if port_scan(target, port):
                print(f"[+] Port {port} is OPEN")
                open_ports.append(port)
    except KeyboardInterrupt:
        print("\n[!] Scan interupted by user")
        sys.exit()

    print("-" * 50)
    print(f"Scan completed at: {datetime.now()}")
    print(f"Total open ports found: {len(open_ports)}")
    if open_ports:
        print(f"Open ports: {open_ports}")
    print("-" * 50)
def main():
    """
    Main function to run the port scanner.
    """
    print("=" * 50)
    print("     SIMPLE PORT SCANNER")
    print("=" * 50)

    #Get target from user
    target = input("\nEnter target IP or hostname").strip()

    #Resolve hostname to IP if needed
    try:
        target_ip = socket.gethostbyname(target)
        print(f"Resolved {target} to {target_ip}")
    except socket.gaierror:
        print(f"[!] Error: Could not resolver hostname {target}")
        sys.exit()
    
    #Get port range from user
    print("\nCommon port ranges:")
    print("1. Well-known ports (1-1023)")
    print("2. Registered ports (1024-49151)")
    print("3. Custom range")

    choice = input("\nSelect option (1/2/3)").strip()

    if choice == "1":
        start_port, end_port = 1, 1023
    elif choice == "2":
        start_port, end_port = 1024, 49151
    elif choice == "3":
        start_port = int(input("Enter start port: "))
        end_port = int(input("Enter end port: "))
    else:
        print("[!] Invalid choice, Using ports 1-1023")
        start_port, end_port = 1, 1023
    
    #Start scanning 
    scan_range(target_ip, start_port, end_port)

if __name__ == "__main__":
    main()