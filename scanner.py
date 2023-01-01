#!/bin/python3
import socket
import datetime as dt
import argparse
import sys
import pyfiglet as pfg


banner = pfg.figlet_format("LAN PortScanner",font="slant")
print(banner)

parser = argparse.ArgumentParser(description="LAN Port scanner for IPV4 addresses")
parser.add_argument('arguments',metavar='IP OR Domain',help="enter the local IP or domain you want to get scanned")
# type is optional if you want to specify the type of daa you want
args = parser.parse_args()
input_list = []
input_list.append(args.arguments)

if len(input_list) == 1:
    target =  socket.gethostbyname(input_list[0])
else:
    print("invalid number of args")


print(f"Scanning target : {target}")
print(f"Scan start time {str(dt.datetime.now())}")
try:
    for port in range(1,65000):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        res=s.connect_ex((target,port))
        if res == 0:
            print(f"the port {port} is open on target {target}")
        s.close()


except KeyboardInterrupt:
    print("\n Exiting Program")
    sys.exit()

except socket.gaierror:
    print("Hostname cannot be resolved")
    sys.exit()

except socket.error:
    print("couldnt connect to server")
    sys.exit()