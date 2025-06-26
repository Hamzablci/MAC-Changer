import subprocess
import random
import os

def random_mac():
    first_octet = random.randint(0x00, 0xff)
    first_octet = (first_octet & 0b11111100) | 0b00000010  
    mac = [first_octet] + [random.randint(0x00, 0xff) for _ in range(5)]
    return ":".join(f"{b:02x}" for b in mac)

def get_interfaces():
    interfaces = []
    try:
        output = subprocess.check_output(["ip", "-o", "link", "show"]).decode()
        for line in output.splitlines():
            parts = line.split(": ")
            if len(parts) > 1:
                name = parts[1].split()[0]
                if name != "lo":  
                    interfaces.append(name)
    except Exception as e:
        print(f"Error reading interfaces: {e}")
    return interfaces

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
        print("---------------------------------")

        interfaces = get_interfaces()
        if not interfaces:
            print("No interfaces found!")
            input("Press ENTER to return to menu...")
            continue

        print("Available Network Interfaces:")
        for i, iface in enumerate(interfaces):
            print(f"{i + 1}: {iface}")
        print(f"{len(interfaces) + 1}: Menu")

        try:
            choice = int(input("Select Interface: "))
            if choice == len(interfaces) + 1:
                continue
            interface = interfaces[choice - 1]
        except (ValueError, IndexError):
            print("Invalid selection!")
            input("Press ENTER to return to menu...")
            continue

        mac_address = input("Enter New MAC Address : ")
        subprocess.call(["ip", "link", "set", interface, "down"])
        subprocess.call(["ip", "link", "set", interface, "address", mac_address])
        subprocess.call(["ip", "link", "set", interface, "up"])
        print(f"MAC address for {interface} has been changed to {mac_address}.")
        input("Press ENTER to return to menu...")

    elif arayuz == 2:
        os.system("clear")
        print("---------------------------------")
        print("---> Random MAC Changer <---")
        print("---------------------------------")

        interfaces = get_interfaces()
        if not interfaces:
            print("No interfaces found!")
            input("Press ENTER to return to menu...")
            continue

        print("Available Network Interfaces:")
        for i, iface in enumerate(interfaces):
            print(f"{i + 1}: {iface}")
        print(f"{len(interfaces) + 1}: Menu")

        try:
            choice = int(input("Select Interface: "))
            if choice == len(interfaces) + 1:
                continue
            interface = interfaces[choice - 1]
        except (ValueError, IndexError):
            print("Invalid selection!")
            input("Press ENTER to return to menu...")
            continue

        mac_address = random_mac()
        subprocess.call(["ip", "link", "set", interface, "down"])
        subprocess.call(["ip", "link", "set", interface, "address", mac_address])
        subprocess.call(["ip", "link", "set", interface, "up"])
        print(f"Random MAC address for {interface} has been changed to {mac_address}.")
        input("Press ENTER to return to menu...")

    elif arayuz == 3:
        os.system("clear")
        print("Application Closed...")
        break  

    else:
        print("Invalid selection.")
        input("Press ENTER to return to menu...")
