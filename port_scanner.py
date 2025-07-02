# first import the `socket` module which let's us make network connections
import socket

#Ask the user for a target to scan
target = input("Enter the IP address or hostname of the target: ")

#Convert the hostname to IP (if needed)
try:
    ip = socket.gethostbyname(target)# Converts a hostname into a IP address
except socket.gaierror:
    print("Invalid hostname or IP address.")
    exit()


print(f"\nScanning target: {ip}\n")

#Scan common ports (20 to 1024)
for port in range(20, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5) #Optional: speeds up scanning if host doesn't respond
    result = s.connect_ex((ip, port)) #0 = success (open port)
    if result == 0:
        print(f"Port {port} is OPEN")
    s.close