File structure.

- brands_models.py  
(dictionary with the meter's brands, models and other infos)

- languages.py
(dictionary with the messages in several languages)

- obis_codes.py
(The list os the obis_codes)

- setup.py
(The software setup parameters)

- meter.py
(The core class of the system)

- main.py
(The main execution file, this is the one that must be runned)
    
- readme.md
(this file)



How to Setup

- Import pyserial library and pandas library
  (responsable for interaction with the /dev/ttyUSBx COM port and CSV export, respectively)

    ```pip3 install pyserial```
    ```pip3 install pandas```

- Set permissions to do /dev/ttyUSBx COM

   ```sudo chmod 666 /dev/ttyUSB0```


The IEC 62054-21 also know as IEC 1107, is an  ASCII protocol and It's easier to work with.
Problem is that there are lots of variations between different meters.

If you do not need anything special you can try to get readout from the meter.

Set serial port baudrate to 300, Data bits: 7, Parity: Even and StopBits: 1.
Then send the string '/?!\r\n' to the port, the meter sound response with something

    \x2F\x3F\x21\x0D\x0A


cuteCom its a good test propose tool to send and receive data, from serial COM, to install run:

    ```sudo apt-get update```
    ```sudo apt-get install cutecom```



link
(Manual do equipamento)

https://www.yumpu.com/en/document/read/39649016/me172-technical-description-iskraemeco-uk


link uteis
https://github.com/openhab/openhab1-addons/wiki/IEC-62056---21-Meter-Binding
https://www.youtube.com/watch?v=fMvP2U-2cs4

(importante)
https://www.gurux.fi/node/5508


Iskra ME 172 is not supporting DLMS. It's using IEC 62054-21 also know as IEC 1107.
IEC 62054-21 is ASCII protocol and It's easier. Problem is that there are lots of variations between different meters. If you do not need anything special you can try to get readout from the meter.
(I'm not sure is this meter supporting it, but you can try).

Set serial port baudrate to 300 and Data bits: 7, Parity: Even and StopBits: 1.
Then send /?!r\n to the port. Meter should response and send some information.
If you wait more usually Mode A is used and meter send readout.


