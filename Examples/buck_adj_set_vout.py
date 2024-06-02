"""
Example: Set PBT223-ADJ to constant voltage (CV) mode with target Vout 1-22V
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

    target_vout = float(input("Enter PBT223-ADJ target Vout 1-22V (V): "))
    buck.set_buck_adj_target_vout(target_vout)
    time.sleep(1)

    for _ in range(5): 
        buck_vout       = buck.read_vout()
        buck_iout       = buck.read_iout()
        buck_pout       = buck.read_pout()
        dac_digital_val = buck.read_dac_digital_val()
        print(f"DAC={dac_digital_val}, Buck vout={buck_vout}, iout={buck_iout}, pout={buck_pout}")
