# first import the `socket` module which let's us make network connections
import socket

#Ask the user for a target to scan
target = input("Enter the IP address or hostname of the target: ")

#Convert the hostname to IP (if needed)
try:
    ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid hostname or IP address.")
    exit()
