"""
Example: 
1) Run the "enable_serial_studio_mode.py" script to enable the PBT223 Fixed/ADJ serial studio mode. 
After enabling, PBT223 product will continuously to transmit data via UART (USB Type-C cable) at 5Hz rate.
The transmit data format is: /*Vin,Vout,Iout,Pout,Temperature*/, each data is kept to 2 decimal places. 
3) Then, open the software "Serial Studio". Load the "PBT223-Data-Visualization.json" configuration file. Connect the PBT223 device. 
4) Now, you could see the real-time data dashboard from "Serial Studio" software. 
You can download "Serial Studio" software from this link: https://github.com/Serial-Studio/Serial-Studio/releases/tag/v2.0.0
5) If you would like to disable the serial studio mode, run the example script "disable_serial_studio_mode.py". 
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

    buck.set_serial_studio_off()
