# Include the libraries for socket and system calls
import socket
import sys
import os
import argparse
import re
import time
import email.utils
import datetime


fresh = False
max_age = 0
expires_time = 0
cacheData=0
for line in cacheData:
    if "Cache-control" in line:
        if "no-cache" in line or "no-store" in line:
            fresh = False
        elif "max-age" in line:
            max_age = int(line.split("=")[1])
            
    if "Expires" in line:
        expires_str = line.split(":", 1)[1].strip()
        try:
            expires_time = email.utils.mktime_tz(email.utils.parsedate_tz(expires_str))
        except TypeError:
            expires_time = 0
            
if expires_time:
    if expires_time < time.time():
        fresh = False
    else:
        fresh = True
elif max_age is not None and max_age>0:
        fresh = True

if not fresh:
    cacheFile.close()
    raise Exception("Cache expired")

response_data = "".join(cacheData)
clientSocket.sendall(response_data.encode('utf-8'))
print(f"response sent to client: {response_data}")


    
    
        
        
        
        

        



