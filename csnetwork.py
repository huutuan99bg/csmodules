import os
import subprocess
from time import sleep
import requests
from termcolor import colored as cl

def check_connect():
    try:
        res = requests.get("https://google.com")
        if res:
            return True
    except:
        return False
def reconnect_phone():
    try:
        print(cl('Phone 3G reconnecting...','blue'))
        filepath="E:\\tools\\open_airmode.bat"
        p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)
        sleep(2)
        p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)
        count = 0
        while count < 15:
            if check_connect() == True:
                print(cl('Phone 3G reconnect successfully!','green'))
                return True
            else:
                sleep(.5)
                count = count + 0.5
        
    except:
        pass

def kcell_connect():
    os.system('rasdial Kcell')
    count = 0
    while count < 15:
        if check_connect() == True:
            return True
        else:
            sleep(.5)
            count = count + 0.5
def kcell_disconnect():
    os.system('rasdial /disconnect')
def kcell_reconnect():
    print(cl('Kcell reconnecting...','blue'))
    kcell_disconnect()
    kcell_connect()
    print(cl('Kcell reconnect successfully!','green'))

def reconnect(device = 'dcom'):
    if device == 'dcom':
        kcell_reconnect()
    elif device == 'phone':
        reconnect_phone()






