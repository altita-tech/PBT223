"""
Example: Set PBT223 Fixed/ADJ max Vin/Vout/Iout/Pout protection values, then read max protection values to verify
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

    # Set PBT223 Fixed/ADJ max Vin/Vout/Iout/Pout protection values
    vin_max_val  = 33.0
    vout_max_val = 25
    iout_max_val = 3.5
    pout_max_val = 75.0
    buck.set_vin_max_limit(vin_max_val)
    buck.set_vout_max_limit(vout_max_val)
    buck.set_iout_max_limit(iout_max_val)
    buck.set_pout_max_limit(pout_max_val)

    print("--------------------------------------")
    # Read Set PBT223 Fixed/ADJ max Vin/Vout/Iout/Pout protection values
    buck_vin_max  = buck.read_vin_max_limit()
    buck_vout_max = buck.read_vout_max_limit()
    buck_iout_max = buck.read_iout_max_limit()
    buck_pout_max = buck.read_pout_max_limit()
    print("DC/DC buck protection values:")
    print(f"Max Vin  = {buck_vin_max}")
    print(f"Max Vout = {buck_vout_max}")
    print(f"Max Iout = {buck_iout_max}")
    print(f"Max Pout = {buck_pout_max}")

