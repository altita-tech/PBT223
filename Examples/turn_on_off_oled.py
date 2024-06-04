"""
Example: Turn ON/OFF the OLED display to test the quality. 
"""

import sys
import os
# Add the parent directory to the Python path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)
from API.pbt223_api import PBT223
import time


if __name__ == "__main__":
    # Connect to PBT223 with your own serial port
    buck = PBT223(port='COM10')
    buck.connect()

    # Turn ON OLED display ====================
    buck.set_oled_on()
    oled_state = buck.read_oled_state()
    if oled_state == True:
        print("Successfully turn ON the OLED display")
    else:
        print("Failed to turn ON the OLED display")
    time.sleep(1)

    # Turn OFF OLED display ====================
    buck.set_oled_off()
    oled_state = buck.read_oled_state()
    if oled_state == False:
        print("Successfully turn OFF the OLED display")
    else:
        print("Failed to turn OFF the OLED display")
    time.sleep(1)

    # Turn ON OLED display ====================
    buck.set_oled_on()
    oled_state = buck.read_oled_state()
    if oled_state == True:
        print("Successfully turn ON the OLED display")
    else:
        print("Failed to turn ON the OLED display")
    time.sleep(1)



