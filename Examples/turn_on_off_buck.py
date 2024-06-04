"""
Example: Turn ON/OFF the DC/DC buck to test the quality. 
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

    # Turn ON DC/DC buck
    buck.turn_on()
    buck_state = buck.read_buck_state()
    if buck_state == True:
        print("Successfully turn ON the DC/DC buck")
    else:
        print("Failed to turn ON the DC/DC buck")
    time.sleep(1)

    # Turn OFF DC/DC buck
    buck.turn_off()
    buck_state = buck.read_buck_state()
    if buck_state == False:
        print("Successfully turn OFF the DC/DC buck")
    else:
        print("Failed to turn OFF the DC/DC buck")
    time.sleep(1)

    # Turn ON DC/DC buck
    buck.turn_on()
    buck_state = buck.read_buck_state()
    if buck_state == True:
        print("Successfully turn ON the DC/DC buck")
    else:
        print("Failed to turn ON the DC/DC buck")
    time.sleep(1)

