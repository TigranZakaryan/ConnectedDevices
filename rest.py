import subprocess
import re
import os

os.system("adb devices")
DeviceID = raw_input("enter device ID")


def ConnectedDevices():
    list = []
    AllConnected = subprocess.check_output("adb devices")
    list.append(AllConnected)
    list = re.split('[\n \t]', AllConnected)
    list.remove('List')
    list.remove('devices')
    list.remove('of')
    for i in list:
        if 'device\r' in i:
            list.remove('device\r')
    list.remove('\r')
    list.remove('attached\r')
    list.remove('')
    return list


def detectConnected():
    connected = ConnectedDevices()
    if DeviceID in connected:
        print (" Status: Connected...")
    else:
        while True:
            connected = ConnectedDevices()
            if DeviceID in connected:
                break
            else:
                print (raw_input("Please connect device and press enter"))


detectConnected()
