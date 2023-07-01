#!/usr/bin/env python

import subprocess

interface = input("Interface >> ")
new_mac = input("New MAC address >>")

print(f"[!] Changing MAC address for {interface} to {new_mac}")

subprocess.call(f"ifconfig {interface} down", shell=True)
subprocess.call(f"ifconfig {interface} hw ether {new_mac}", shell=True)
subprocess.call(f"ifconfig {interface} up", shell=True)