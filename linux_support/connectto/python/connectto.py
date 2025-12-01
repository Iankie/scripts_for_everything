#!/usr/bin/python3

import argparse
import netifaces as ni 
import subprocess
from termcolor import colored
   

def init_connection(iface):
    
    if iface.find('eth') != -1:
        
        subprocess.run(["ifconfig", f"{iface}", "up"])
    
        subprocess.run(["macchanger", "-r", "-p", f"{iface}"], stdout=subprocess.DEVNULL)
        
        subprocess.run(["dhclient", f"{iface}"])
        
    elif iface.find('wlan') != 1:
        
        subprocess.run(["ifconfig", f"{iface}", "up"])

        subprocess.run(["wpa_supplicant", "-B", "-c", "/etc/wpa_supplicant.conf", "-i", f"{iface}"], stdout=subprocess.DEVNULL)
        
        subprocess.run(["dhclient", f"{iface}"])
    
    ip = ni.ifaddresses(iface)[ni.AF_INET][0]['addr']
        
    print(f"Got {colored(ip, 'green')} on {iface} interface!")

def check_interface(iface):
    if iface in ni.interfaces():
        
        init_connection(iface)
        
    else:
        print(colored(f"Interface {iface} doesn't exists!", 'red'))   


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Connection Manager")
    parser.add_argument('interface', type=str, help='Set interface using to connection')
    args = parser.parse_args()    

    interface = args.interface
    
    check_interface(interface)
