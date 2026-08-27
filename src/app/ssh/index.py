import subprocess
import asyncio
import re; 
# Calls your operating system's native SSH client

def get_netstat():
    try:
        result = subprocess.run(
        ["ssh", "root@192.168.8.1", "netstat -tulpn"],
        capture_output=True,
        text=True,
        check=True
        )
        format_netstat(result.stdout)
        # with open("demofile.txt", "a") as f:
        #     f.write( result.stdout)
    except subprocess.CalledProcessError as e:
        print("SSH Command failed:", e.stderr)



def format_netstat(rawOutput:str):
        outputArray = rawOutput.splitlines()
        print(outputArray)
        for i, entry in enumerate(outputArray):
            if (i > 1):
                print()
                print(entry)
                parts = re.split(r" {2,}", entry)
                columnSeperator = re.split(r" {1,}",parts[2])
                activeSocket: dict = {
                     "protocol": parts[0],
                     "recieve": parts[1],
                     "send": columnSeperator[0],
                     "localAddress": columnSeperator[1],
                     "foreignAddress": parts[3],
                     "state": "" if len(parts) < 6 else parts[4],
                     "pid": parts[4] if len(parts) < 6 else parts[5]
                }
                print(activeSocket)
                print()