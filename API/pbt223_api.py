import serial
import time
from typing import Union, Optional

class PBT223:
    def __init__(self, port):
        self.cmd = ""
        self.DONT_CARE_BYTE = 0xFF
        
        self.ser = serial.Serial(port, baudrate=115200)
        self.ser.timeout = 1.0
        self.ser.close()
        time.sleep(0.1)

    def connect(self) -> None:
        self.ser.close()
        time.sleep(0.1)
        self.ser.open()
        time.sleep(0.1)

    def disconnect(self) -> None:
        self.ser.close()
        time.sleep(0.1)

    def read_serial_data(self) -> Optional[str]:
        data = self.ser.readline().decode('utf-8', errors='ignore').strip()
        if data:
            return data
        else:
            # print("No available data")
            return None

    def read_buck_state(self) -> bool:
        self.cmd = bytes([0x00, 0x00, self.DONT_CARE_BYTE, self.DONT_CARE_BYTE])
        self.ser.write(self.cmd)
        state = int(self.read_serial_data())
        time.sleep(0.1)
        if state == 1:
            return True
        else:
            return False

    def read_vin(self) -> float:
        self.cmd = bytes([0x00, 0x01, self.DONT_CARE_BYTE, self.DONT_CARE_BYTE])
        self.ser.write(self.cmd)
        vin = float(self.read_serial_data())
        time.sleep(0.1)
        return vin

    def read_vout(self) -> float:
        self.cmd = bytes([0x00, 0x02, self.DONT_CARE_BYTE, self.DONT_CARE_BYTE])
        self.ser.write(self.cmd)
        vout = float(self.read_serial_data())
        time.sleep(0.1)
        return vout

    def read_iout(self) -> float:
        self.cmd = bytes([0x00, 0x03, self.DONT_CARE_BYTE, self.DONT_CARE_BYTE])
        self.ser.write(self.cmd)
        iout = float(self.read_serial_data())
        time.sleep(0.1)
        return iout

    def read_pout(self) -> float:
        self.cmd = bytes([0x00, 0x04, self.DONT_CARE_BYTE, self.DONT_CARE_BYTE])
        self.ser.write(self.cmd)
        pout = float(self.read_serial_data())
        time.sleep(0.1)
        return pout

    def read_buck_adj_mode(self) -> Union[bool, str]:
        self.cmd = bytes([0x00, 0x05, self.DONT_CARE_BYTE, self.DONT_CARE_BYTE])
        self.ser.write(self.cmd)
        time.sleep(0.1)
        cvcp_mode = self.read_serial_data()
        try:  
            return bool(cvcp_mode)  
        except:
            return str(cvcp_mode) 
    
    def read_target_vout(self) -> Union[int, str]:
        self.cmd = bytes([0x00, 0x06, self.DONT_CARE_BYTE, self.DONT_CARE_BYTE])
        self.ser.write(self.cmd)
        target_vout = self.read_serial_data()
        time.sleep(0.1)
        try:
            return float(target_vout)
        except ValueError:
            return str(target_vout)

    def read_target_pout(self) -> Union[int, str]:
        self.cmd = bytes([0x00, 0x07, self.DONT_CARE_BYTE, self.DONT_CARE_BYTE])
        self.ser.write(self.cmd)
        target_pout = self.read_serial_data()
        time.sleep(0.1)
        try:
            return float(target_pout)
        except ValueError:
            return str(target_pout)
        
    def read_dac_digital_val(self) -> Union[int, str]:
        self.cmd = bytes([0x00, 0x08, self.DONT_CARE_BYTE, self.DONT_CARE_BYTE])
        self.ser.write(self.cmd)
        dac_val = self.read_serial_data()
        time.sleep(0.1)
        try:
            return int(dac_val)
        except ValueError:
            return str(dac_val)

    def read_vin_max_limit(self) -> float:
        self.cmd = bytes([0x00, 0x09, self.DONT_CARE_BYTE, self.DONT_CARE_BYTE])
        self.ser.write(self.cmd)
        vin_max_limit = float(self.read_serial_data())
        time.sleep(0.1)
        return vin_max_limit
    
    def read_vout_max_limit(self) -> float:
        self.cmd = bytes([0x00, 0x10, self.DONT_CARE_BYTE, self.DONT_CARE_BYTE])
        self.ser.write(self.cmd)
        vout_max_limit = float(self.read_serial_data())
        time.sleep(0.1)
        return vout_max_limit

    def read_iout_max_limit(self) -> float:
        self.cmd = bytes([0x00, 0x11, self.DONT_CARE_BYTE, self.DONT_CARE_BYTE])
        self.ser.write(self.cmd)
        iout_max_limit = float(self.read_serial_data())
        time.sleep(0.1)
        return iout_max_limit

    def read_pout_max_limit(self) -> float:
        self.cmd = bytes([0x00, 0x12, self.DONT_CARE_BYTE, self.DONT_CARE_BYTE])
        self.ser.write(self.cmd)
        pout_max_limit = float(self.read_serial_data())
        time.sleep(0.1)
        return pout_max_limit

    def read_temperature_sensor(self) -> float:
        self.cmd = bytes([0x00, 0x13, self.DONT_CARE_BYTE, self.DONT_CARE_BYTE])
        self.ser.write(self.cmd)
        temperature_sensor_degree = float(self.read_serial_data())
        time.sleep(0.1)
        return temperature_sensor_degree

    def read_mcu_temperature(self) -> float:
        self.cmd = bytes([0x00, 0x14, self.DONT_CARE_BYTE, self.DONT_CARE_BYTE])
        self.ser.write(self.cmd)
        mcu_degree = float(self.read_serial_data())
        time.sleep(0.1)
        return mcu_degree

    def read_ldo_vdda(self) -> float:
        self.cmd = bytes([0x00, 0x15, self.DONT_CARE_BYTE, self.DONT_CARE_BYTE])
        self.ser.write(self.cmd)
        ldo_vdda = float(self.read_serial_data())
        time.sleep(0.1)
        return ldo_vdda

    def read_oled_state(self) -> bool:
        self.cmd = bytes([0x00, 0x16, self.DONT_CARE_BYTE, self.DONT_CARE_BYTE])
        self.ser.write(self.cmd)
        oled_state = int(self.read_serial_data())
        time.sleep(0.1)
        if oled_state == 1:
            return True
        else:
            return False

    def read_eeprom_address(self, eeprom_address: int) -> str:
        # eeprom_address must be an integer
        self.cmd = bytes([0x00, 0x17, eeprom_address, self.DONT_CARE_BYTE])
        self.ser.write(self.cmd)
        eeprom_data = int(self.read_serial_data())
        time.sleep(0.1)
        return eeprom_data

    def read_pn(self) -> str:
        self.cmd = bytes([0x00, 0xF0, self.DONT_CARE_BYTE, self.DONT_CARE_BYTE])
        self.ser.write(self.cmd)
        pn = str(self.read_serial_data())
        time.sleep(0.1)
        return pn 
    
    def read_sn(self) -> str:
        self.cmd = bytes([0x00, 0xF1, self.DONT_CARE_BYTE, self.DONT_CARE_BYTE])
        self.ser.write(self.cmd)
        sn = str(self.read_serial_data())
        time.sleep(0.1)
        return sn

    def read_hardware_rev(self) -> str:
        self.cmd = bytes([0x00, 0xF2, self.DONT_CARE_BYTE, self.DONT_CARE_BYTE])
        self.ser.write(self.cmd)
        hardware_rev = str(self.read_serial_data())
        time.sleep(0.1)
        return hardware_rev
    
    def read_firmware_rev(self) -> str:
        self.cmd = bytes([0x00, 0xF3, self.DONT_CARE_BYTE, self.DONT_CARE_BYTE])
        self.ser.write(self.cmd)
        firmware_rev = str(self.read_serial_data())
        time.sleep(0.1)
        return firmware_rev

    def turn_off(self) -> None:
        self.cmd = bytes([0x01, 0x00, self.DONT_CARE_BYTE, self.DONT_CARE_BYTE])
        self.ser.write(self.cmd)
        time.sleep(0.1)

    def turn_on(self) -> None:
        self.cmd = bytes([0x01, 0x01, self.DONT_CARE_BYTE, self.DONT_CARE_BYTE])
        self.ser.write(self.cmd)
        time.sleep(0.1)

    def set_buck_adj_target_vout(self, target_vout: float) -> Union[float, str]:
        TARGET_VOUT_MIN = 1.0
        TARGET_VOUT_MAX = 22.0
        if target_vout<TARGET_VOUT_MIN or target_vout>TARGET_VOUT_MAX:
            err = f"Error: {TARGET_VOUT_MIN} <= target Vout <= {TARGET_VOUT_MAX} V"
            print(err)
            return err
        else:
            target_vout = max(TARGET_VOUT_MIN, min(TARGET_VOUT_MAX, target_vout))
            target_vout_str = f"{target_vout:.2f}"
            int_part_str, dec_part_str = target_vout_str.split(".")
            int_part = int(int_part_str)
            dec_part = int(dec_part_str)
            self.cmd = bytes([0x01, 0x02, int_part, dec_part])
            self.ser.write(self.cmd)
            target_vout = self.read_serial_data()
            time.sleep(0.1)
            try:
                return float(target_vout)
            except ValueError:
                return str(target_vout)

    def set_buck_adj_target_pout(self, target_pout: float) -> Union[float, str]:
        target_pout_str = f"{target_pout:.2f}"
        int_part_str, dec_part_str = target_pout_str.split(".")
        int_part = int(int_part_str)
        dec_part = int(dec_part_str)
        self.cmd = bytes([0x01, 0x03, int_part, dec_part])
        self.ser.write(self.cmd)
        time.sleep(0.1)
        target_pout = self.read_serial_data()
        try:
            return float(target_pout)
        except ValueError:
            return str(target_pout)

    def set_dac_digital_val(self, dac_digital_val: int) -> Union[int, str]:
        # 0 <= dac_val <= 4095
        dac_digital_val = max(0, min(4095, dac_digital_val))
        dac_digital_high = (dac_digital_val >> 8) & 0xFF
        dac_digital_low = dac_digital_val & 0xFF
        self.cmd = bytes([0x01, 0x04, dac_digital_high, dac_digital_low])
        self.ser.write(self.cmd)
        dac_digital_val = self.read_serial_data()
        time.sleep(0.1)
        try:
            return int(dac_digital_val)
        except ValueError:
            return str(dac_digital_val)
    
    def set_vin_max_limit(self, vin_max_limit: float) -> None:
        int_part = int(vin_max_limit)
        dec_part = int(round((vin_max_limit - int_part) * 10))
        self.cmd = bytes([0x01, 0x05, int_part, dec_part])
        self.ser.write(self.cmd)
        # We must add delay for EEPROM write operation
        time.sleep(0.1)

    def set_vout_max_limit(self, vout_max_limit: float) -> None:
        int_part = int(vout_max_limit)
        dec_part = int(round((vout_max_limit - int_part) * 10))
        self.cmd = bytes([0x01, 0x06, int_part, dec_part])
        self.ser.write(self.cmd)
        # We must add delay for EEPROM write operation
        time.sleep(0.1)

    def set_iout_max_limit(self, iout_max_limit: float) -> None:
        int_part = int(iout_max_limit)
        dec_part = int(round((iout_max_limit - int_part) * 10))
        self.cmd = bytes([0x01, 0x07, int_part, dec_part])
        self.ser.write(self.cmd)
        # We must add delay for EEPROM write operation
        time.sleep(0.1)

    def set_pout_max_limit(self, pout_max_limit: float) -> None:
        int_part = int(pout_max_limit)
        dec_part = int(round((pout_max_limit - int_part) * 100))
        self.cmd = bytes([0x01, 0x08, int_part, dec_part])
        self.ser.write(self.cmd)
        # We must add delay for EEPROM write operation
        time.sleep(0.1)

    def set_oled_on(self) -> None:
        self.cmd = bytes([0x01, 0x09, self.DONT_CARE_BYTE, self.DONT_CARE_BYTE])
        self.ser.write(self.cmd)
        time.sleep(0.1)

    def set_oled_off(self) -> None:
        self.cmd = bytes([0x01, 0x10, self.DONT_CARE_BYTE, self.DONT_CARE_BYTE])
        self.ser.write(self.cmd)
        time.sleep(0.1)
        
    def set_serial_studio_on(self) -> None:
        self.cmd = bytes([0x01, 0x11, self.DONT_CARE_BYTE, self.DONT_CARE_BYTE])
        self.ser.write(self.cmd)
        time.sleep(0.1)
        
    def set_serial_studio_off(self) -> None:
        self.cmd = bytes([0x01, 0x12, self.DONT_CARE_BYTE, self.DONT_CARE_BYTE])
        self.ser.write(self.cmd)
        time.sleep(0.1)
        
    def write_eeprom_address(self, eeprom_address: int, eeprom_data: int) -> None:
        self.cmd = bytes([0x01, 0x13, eeprom_address, eeprom_data])
        self.ser.write(self.cmd)
        # We must add delay for EEPROM write operation
        time.sleep(0.1)
