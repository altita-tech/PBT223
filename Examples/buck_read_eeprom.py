"""
Example: On PBT223 Fixed/ADJ, write data to EEPROM address, then read data from address to verify 
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

    address = 0x10

    data1 = 111
    buck.write_eeprom_address(eeprom_address=address, eeprom_data=data1)
    read_result1 = buck.read_eeprom_address(eeprom_address=address)
    print(f"Read EEPROM address={address}, data={read_result1}")

    data2 = 222
    buck.write_eeprom_address(eeprom_address=address, eeprom_data=data2)
    read_result2 = buck.read_eeprom_address(eeprom_address=address)
    print(f"Read EEPROM address={address}, data={read_result2}")
