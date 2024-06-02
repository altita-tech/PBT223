"""
Example: Read PBT223 Fixed/ADJ MCU internal temeprature sensor and external temperature sensor for 5 times 
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

    # Read MCU internal temperature sensor and external temperature sensor for 5 times 
    for i in range(5):
        mcu_temperature_degree = buck.read_mcu_temperature()
        temp_sensor_degree = buck.read_temperature_sensor()

        print("--------------------------------------------------")
        print(f"Index = {i}")
        print(f"MCU internal temperature sensor = {mcu_temperature_degree} (degree)")
        print(f"External temperature sensor     = {temp_sensor_degree} (degree)")

