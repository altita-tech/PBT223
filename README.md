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

<table style="width:100%; text-align:center;">
  <tr>
    <td style="width: 50%;">
      <img src="Images/PBT223-fixed-top-view.png" style="height: auto; margin: 10px 10px;">
    </td>
    <td style="width: 50%;">
      <img src="Images/PBT223-ADJ-DAC-4095.png" style="height: auto; margin: 10px 10px;">
    </td>
  </tr>
</table>


<table style="width:100%; text-align:center;">
  <tr>
    <td style="width: 100%; margin: 0 auto;">
      <img src="Images/DAC-vs-Vout.png" style="max-width: 100%; height: auto; margin: 10px;">
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
<table style="width:100%; text-align:center;">
  <tr>
    <td style="width: 100%;">
      <img src="Images/PBT223-command-read.png" style="max-width: 100%; height: auto; margin: 10px 10px;">
    </td>
  </tr>
</table>


### 写指令
<table style="width:100%; text-align:center;">
  <tr>
    <td style="width: 100%;">
      <img src="Images/PBT223-command-write.png" style="max-width: 100%; height: auto; margin: 10px 10px;">
    </td>
  </tr>
</table>


### 故障信息
<table style="width:100%; text-align:center;">
  <tr>
    <td style="width: 100%;">
      <img src="Images/PBT223-command-error.png" style="max-width: 100%; height: auto; margin: 10px 10px;">
    </td>
  </tr>
</table>



### EEPROM数据映射
<table style="width:100%; text-align:center;">
  <tr>
    <td style="width: 100%;">
      <img src="Images/PBT223-EEPROM-map.png" style="max-width: 100%; height: auto; margin: 10px 10px;">
    </td>
  </tr>
</table>



## 图纸
### 2D图纸
[2D图纸：下载链接](https://altita-tech.com/wp-content/uploads/PBT223/PBT223%202D.zip)

<table style="width:100%; text-align:center;">
  <tr>
    <td style="width: 45%;">
      <img src="Images/PBT223-fixed-2D-with-dimension.png" style="width: 100%; height: auto; margin: 10px 10px;">
    </td>
    <td style="width: 45%;">
      <img src="Images/PBT223-ADJ-2D-with-dimension.png" style="width: 100%; height: auto; margin: 10px 10px;">
    </td>
  </tr>
</table>



### 3D模型
[3D模型：下载链接](https://altita-tech.com/wp-content/uploads/PBT223/PBT223%203D.zip)

<table style="width:100%; text-align:center;">
  <tr>
    <td style="width: 45%;">
      <img src="Images/PBT223-fixed-with-OLED.png" style="width: 100%; height: auto; margin: 10px 10px;">
    </td>
    <td style="width: 45%;">
      <img src="Images/PBT223-ADJ-with-OLED.png" style="width: 100%; height: auto; margin: 10px 10px;">
    </td>
  </tr>
  <tr>
    <td style="width: 45%;">
      <img src="Images/PBT223-fixed-side-view.png" style="width: 100%; height: auto; margin: 10px 10px;">
    </td>
    <td style="width: 45%;">
      <img src="Images/PBT223-ADJ-side-view.png" style="width: 100%; height: auto; margin: 10px 10px;">
    </td>
  </tr>
</table>


## 功能方框图
<table style="width:100%; text-align:center;">
  <tr>
    <td style="width: 100%;">
      <img src="Images/PBT223-block-diagram.png" style="max-width: 100%; height: auto; margin: 10px 10px;">
    </td>
  </tr>
</table>


## 联系我们
<div style="display: flex; justify-content: space-between; align-items: flex-start;">
  <div>
    <ul style="list-style-type: disc; padding-left: 20px; margin: 0;">
      <li><strong>公司官网：</strong> <a href="https://altita-tech.com/">https://altita-tech.com/</a></li>
      <li><strong>销售：</strong> <a href="mailto:sales@altita-tech.com">sales@altita-tech.com</a></li>
      <li><strong>技术支持：</strong> <a href="mailto:tech@altita-tech.com">tech@altita-tech.com</a></li>
    </ul>
  </div>
</div>

<table style="width:100%; text-align:center;">
  <tr>
    <td style="width: 100%;">
      <img src="Images/Altita&Logo.png" style="max-width: 100%; height: auto; margin: 10px 10px;">
    </td>
  </tr>
</table>
