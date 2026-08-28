import subprocess
import re

from app.repository.netstat import init_netstat, insert_netstat_entries; 

def get_netstat():
    try:
        result = subprocess.run(
        ["ssh", "root@192.168.8.1", "netstat -tulpn"],
        capture_output=True,
        text=True,
        check=True
        )
        return format_netstat(result.stdout)
    except subprocess.CalledProcessError as e:
        print("SSH Command failed:", e.stderr)

def format_netstat(rawOutput:str):
        outputArray = rawOutput.splitlines()
        activeSockets = []
        for i, entry in enumerate(outputArray):

            if (i > 1):
                parts = re.split(r" {2,}", entry)
                columnSeperator = re.split(r" {1,}",parts[2])
                activeSocket: dict = {
                     "protocol": parts[0],
                     "recv_q": int(parts[1]),
                     "send_q": int(columnSeperator[0]),
                     "local_address": columnSeperator[1],
                     "foreign_address": parts[3],
                     "state": "" if len(parts) < 6 else parts[4],
                     "pid": parts[4] if len(parts) < 6 else parts[5]
                }
                activeSockets.append(activeSocket)
        return activeSockets

def handleNetstat():
    netstatEntries = get_netstat()
    init_netstat()
    insert_netstat_entries(netstatEntries)