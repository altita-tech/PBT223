# PBT223 API and Demo
* PBT223系列是一款可通过UART串口程控的直流转直流降压电路（DC-DC Buck）
    - **PBT223-Fixed：** 仅支持恒电压（CV）模式
    - **PBT223-ADJ：** 支持恒电压（CV），恒功率（CP）和DAC模式
* **DC/DC Buck同步降压电路** 
    - **Vin = 3.8 – 30 V**
    - **Vout = 0.8 – 22 V（固定输出 & 可调输出）**
    - **Iout  = 0 – 3 A**
    - **开关频率：** 默认500kHz，支持200kHz – 2.2MHz
    - **最大占空比：** 98%
    - **软起动时间：** 默认4.8ms
* **UART串口读取数据：** 输出状态， Vin，Vout，Iout，Pout ，温度传感器数值，EEPROM数据 等
* **UART串口写入数据：** 打开/关闭输出，设定 I(out_max)， P(out_max)，EEPROM数

* **OLED屏幕：** 展示实时数据 Vin， Vout， Iout， Pout ，温度传感器数值
* **软硬件保护电路：** 输入欠压保护UVLO，输入/输出过压保护OVP，输出过压保护OCP，输出过流保护OCP，输出过功率保护OPP，输出短路保护，过温保护OTP，输入/输出防反接保护，静电保护ESD
* **Python API & 例程代码：** Python语言，支持windows和Linux系统
工作温度范围：-40 - 85 ℃

<table style="width: 100%;">
  <tr>
    <td style="text-align: center; vertical-align: middle;">
      <img src="Images/PBT223-Fixed top view.png" style="height: 150;">
    </td>
    <td style="text-align: center; vertical-align: middle;">
      <img src="Images/PBT223-Fixed top view.png" style="height: 150;">
    </td>
  </tr>
</table>


## 产品选型表
| 功能                                 | PBT223-0V8 | PBT223-3V3 | PBT223-5V0 | PBT223-12V | PBT223-22V | PBT223-ADJ |
|--------------------------------------|------------|------------|------------|------------|------------|------------|
| UART 编程                            | ✅         | ✅         | ✅         | ✅         | ✅         | ✅         |
| 输出电压 Vout                        | 0.8V       | 3.3V       | 5V         | 12V        | 22V        | 1 - 22V 可调节 |
| 输出电流 Iout                        | 0 - 3A     | 0 - 3A     | 0 - 3A     | 0 - 3A     | 0 - 3A     | 0 - 3A     |
| 输入电压 Vin                         | 2 - 30V    | 5 - 30V    | 7 - 30V    | 14 - 30V   | 24 - 30V   | Vout + 2V  |
| 输出纹波 Vpp                         | &lt;150mV  | &lt;150mV  | &lt;150mV  | &lt;150mV  | &lt;150mV  | &lt;400mV  |
| 开关频率 f_sw                        | 200 - 2200kHz | 200 - 2200kHz | 200 - 2200kHz | 200 - 2200kHz | 200 - 2200kHz | 200 - 2200kHz |
| 工作温度                             | -40 - 85 ℃ | -40 - 85 ℃ | -40 - 85 ℃ | -40 - 85 ℃ | -40 - 85 ℃ | -40 - 85 ℃ |
| 保护电路：                           | ✅         | ✅         | ✅         | ✅         | ✅         | ✅         |
| 输入/输出防反接，OVP, OCP, OTP, UVP | ✅         | ✅         | ✅         | ✅         | ✅         | ✅         |





## 通讯协议
### 读指令
<div style="text-align: center; margin: 10px;">
    <img src="Images/PBT223 command table - read.png" alt="alt text" style="width: 100%;">
</div>

### 写指令
<div style="text-align: center; margin: 10px;">
    <img src="Images/PBT223 command table - write.png" alt="alt text" style="width: 100%;">
</div>

### 故障信息
<div style="text-align: center; margin: 10px;">
    <img src="Images/PBT223 command table - error.png" alt="alt text" style="width: 100%;">
</div>

### EEPROM数据映射
<div style="text-align: center; margin: 10px;">
    <img src="Images/PBT223 EEPROM map.png" alt="alt text" style="width: 100%;">
</div>


## 图纸
### 2D图纸
[2D图纸：下载链接](https://example.com/path/to/2D_drawing.zip)
<p align="center">
  <img src="Images/PBT223-Fixed 2D.png" alt="alt text" height="200">
</p>



### 3D模型
[3D模型：下载链接](https://example.com/path/to/2D_drawing.zip)
<table style="width: 100%;">
  <tr>
    <td style="text-align: center; vertical-align: middle;">
      <img src="Images/PBT223-Fixed 3D top view.png" style="height: 175px;">
    </td>
    <td style="text-align: center; vertical-align: middle;">
      <img src="Images/PBT223-ADJ 3D top view.png" style="height: 175px;">
    </td>
  </tr>
</table>




## 功能方框图
<p align="center">
  <img src="Images/PBT223 block diagram.png" alt="alt text" height="300">
</p>



## 联系我们
<div style="display: flex; justify-content: space-between; align-items: flex-start;">
  <div>
    <ul style="list-style-type: disc; padding-left: 20px; margin: 0;">
      <li><strong>公司官网：</strong> <a href="https://altita-tech.com/">https://altita-tech.com/</a></li>
      <li><strong>销售：</strong> <a href="mailto:sales@altita-tech.com">sales@altita-tech.com</a></li>
      <li><strong>技术支持：</strong> <a href="mailto:tech@altita-tech.com">tech@altita-tech.com</a></li>
    </ul>
  </div>
  <div>
    <img src="Images/Altita%20&%20Logo.png" alt="alt text" height="80">
  </div>
</div>


