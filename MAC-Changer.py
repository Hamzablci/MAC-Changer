import subprocess
import random
import os

def random_mac():
    mac = [0x02,
           random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]
    return ":".join(f"{b:02x}" for b in mac)


if os.getuid() != 0:
    os.system("clear")
    print("----------------")
    print(" RUN AS ROOT !!! ")
    print("----------------")
    exit()

while True:
    os.system("clear")
    print("---------------------------------")
    print("---> MAC Changer Application <---")
    print("1: Manual MAC Changer ")
    print("2: Random MAC Changer ")
    print("3: Exit ")
    print("---------------------------------")

    try:
        arayuz = int(input("Make Your Choice : "))
    except ValueError:
        print("Please enter a number!")
        input("Press ENTER to return to the menu...")
        continue

    if arayuz == 1:
        os.system("clear")
        print("---------------------------------")
        print("---> Manual MAC Changer <---")
        print("1: eth0 ")
        print("2: wlan0 ")
        print("3: Menu ")
        print("---------------------------------")
        interface = input("Enter Network Interface : ")

        if interface == "1":
            interface = "eth0"
        elif interface == "2":
            interface = "wlan0"
        elif interface == "3":
            continue  
        else:
            print("Incorrect Entry Detected!")
            input("Press ENTER to return to menu...")
            continue

        mac_address = input("Enter New MAC Address : ")
        subprocess.call(["ip", "link", "set", interface, "down"])
        subprocess.call(["ip", "link", "set", interface, "address", mac_address])
        subprocess.call(["ip", "link", "set", interface, "up"])
        print("MAC address for " + interface + " has been changed to " + mac_address + ".")
        input("Press ENTER to return to menu...")

    elif arayuz == 2:
        os.system("clear")
        print("---------------------------------")
        print("---> Random MAC Changer <---")
        print("1: eth0 ")
        print("2: wlan0 ")
        print("3: Menu ")
        print("---------------------------------")
        interface = input("Enter Network Interface: ")
        if interface == "1":
            interface = "eth0"
        elif interface == "2":
            interface = "wlan0"
        elif interface == "3":
            continue
        else:
            print("Incorrect Entry Detected!")
            input("Press ENTER to return to menu...")
            continue
        
        mac_address = random_mac()
        subprocess.call(["ip", "link", "set", interface, "down"])
        subprocess.call(["ip", "link", "set", interface, "address", mac_address])
        subprocess.call(["ip", "link", "set", interface, "up"])
        print("Random MAC address for " + interface + " has been changed to " + mac_address + ".")
        input("Press ENTER to return to menu...")

    elif arayuz == 3:
        os.system("clear")
        print("Application Closed...")
        break  

    else:
        print("Invalid selection.")
        input("Press ENTER to return to menu...")