"""
Example: Set PBT223-ADJ to DAC mode with target DAC 0-4095, which maps to min-max Vout
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

    target_dac      = input("Enter PBT223-ADJ target DAC (0-4095): ")
    target_dac      = int(target_dac)
    target_pout_low = buck.set_dac_digital_val(dac_digital_val = target_dac)
    time.sleep(1)

    for _ in range(5): 
        buck_vout       = buck.read_vout()
        buck_iout       = buck.read_iout()
        buck_pout       = buck.read_pout()
        dac_digital_val = buck.read_dac_digital_val()
        print(f"DAC={dac_digital_val}, Buck vout={buck_vout}, iout={buck_iout}, pout={buck_pout}")

