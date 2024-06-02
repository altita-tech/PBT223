"""
Example: Read PBT223 Fixed/ADJ DC/DC buck electrical information
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

    buck_state      = buck.read_buck_state()
    vin             = buck.read_vin()
    vout            = buck.read_vout()
    iout            = buck.read_iout()
    pout            = buck.read_pout()
    dac_digital_val = buck.read_dac_digital_val()

    print("# Read DC/DC buck information")
    print("------------------------------------------")
    print(f"Buck state                  = {buck_state}")
    print(f"Vin                         = {vin} (V)")
    print(f"Vout                        = {vout} (V)")
    print(f"Iout                        = {iout} (A)")
    print(f"Pout                        = {pout} (W)")
    print(f"DAC digital value           = {dac_digital_val}")




