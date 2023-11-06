#!/usr/bin/python3

from colorama import Fore
import socket
import sys
import threading
import datetime
import time as t


print("*"*25)
print(Fore.RED + "  _______  _______  _______  _______  _ ")      
print(" (       )(  ____ \(  ____ \(  ___  )( (    /|") 
print(" | () () || (    \/| (    \/| (   ) ||  \  ( |") 
print(" | || || || (_____ | |      | (___) ||   \ | |") 
print(" | |(_)| |(_____  )| |      |  ___  || (\ \) |") 
print(" | |   | |      ) || |      | (   ) || | \   |") 
print(" | )   ( |/\____) || (____/\| )   ( || )  \  |") 
print(" |/     \|\_______)(_______/|/     \||/    )_)") 
                                             
print(Fore.WHITE + "*"*50)

uhelp = "python3 mscan.py HOST START_PORT END_PORT"

openports = []

now = datetime.datetime.now()
print(Fore.MAGENTA + "Started the Scan at :", now.strftime("%y-%m-%d %H:%M:%S"))
print(Fore.WHITE + "*"*50)

st = t.time()

if (len(sys.argv) != 4):
    print(Fore.YELLOW + uhelp)
    sys.exit()
    
try:
    host = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print(Fore.RED + "Can't resolve host name. The target may be down or you may be blocked.")
    sys.exit()

sport = int(sys.argv[2])
eport = int(sys.argv[3])

print(Fore.GREEN + "Starting the Scan: ")


def port_scan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scan = s.connect_ex((host, port))
    s.settimeout(3)
    if (not scan):
        print(Fore.BLUE + "Port {} is open.".format(port))
        openports.append(port)
    s.close()
    

for port in range(sport, eport+1):
    thread = threading.Thread(target = port_scan,daemon = True, args = (port,))
    thread.start()
 
    
if (len(openports) == 0):
        print(Fore.RED + "No open ports found!!")

et = t.time()
print(Fore.YELLOW + "Time elapsed:", et-st ,"s")
