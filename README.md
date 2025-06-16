# MAC Changer Application

This is a Python-based terminal application to change the MAC address of network interfaces on Linux systems. You can manually enter a new MAC address or generate a random one.

---

## Features

- Must be run as root (sudo).
- Manual MAC address changing.
- Random MAC address generation and changing.
- User-friendly menu interface.
- Input validation and easy return to the menu.

---

## Requirements

- Python 3.x
- Linux operating system (uses `ip link` commands)
- Run with root (sudo) privileges

---

## Usage

1. Open your terminal.
2. Run the script:

   ```bash
   sudo python3 mac_changer.py
