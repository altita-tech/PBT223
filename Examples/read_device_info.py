"""
Example: Read PBT223 Fixed/ADJ device information
"""

import sys
import os
# Add the parent directory to the Python path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)
from API.pbt223_api import PBT223


if __name__ == "__main__":
    # Connect to PBT223 with your own serial port
    buck = PBT223(port='COM10')
    buck.connect()

    part_number   = buck.read_pn()
    serial_number = buck.read_sn()
    hardware_rev  = buck.read_hardware_rev()
    firmware_rev  = buck.read_firmware_rev()

    print("Read PBT223 device information")
    print("--------------------------------------------------")
    print(f"Part number      = {part_number}")
    print(f"Serial number    = {serial_number}")
    print(f"Hardware version = {hardware_rev}")
    print(f"Firmware version = {firmware_rev}")


