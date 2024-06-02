"""
Example: Set PBT223-ADJ to constant power (CP) mode with target Pout 0-66 W
"""

import time 
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
    buck.turn_on()

    target_power = float(input("Enter PBT223-ADJ target power 0-66 (W): "))
    buck.set_buck_adj_target_pout(target_power)
    time.sleep(1)

    for _ in range(5): 
        buck_vout       = buck.read_vout()
        buck_iout       = buck.read_iout()
        buck_pout       = buck.read_pout()
        dac_digital_val = buck.read_dac_digital_val()
        print(f"DAC={dac_digital_val}, Buck vout={buck_vout}, iout={buck_iout}, pout={buck_pout}")

