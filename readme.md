## File structure. ##

- **brands_models.py** (dictionary with the meter's brands, models and other infos)
- **languages.py**(dictionary with the messages in several languages)
- **obis_codes.py** (The list os the obis_codes)
- **setup.py**(The software setup parameters)
- **meter.py** (The core class of the system)
- **main.py** (The main execution file, this is the one that must be runned)
- **readme.md**
(this file)

## How to Setup. ##

- Import pyserial library and pandas library
  (responsable for interaction with the /dev/ttyUSBx COM port and CSV export, respectively)

        pip3 install pyserial
        pip3 install pandas

- Set permissions to do /dev/ttyUSBx COM

        sudo chmod 666 /dev/ttyUSB0


The **IEC 62054-21*** also know as **IEC 1107***, is an  ASCII protocol and It's easier to work with. The problem is that **there are lots*** of variations between different meters.

If you do not need anything special you can **try to get readouts*** from the meter.

Set serial port to:

    baudrate: 300
    Data bits: 7
    Parity: Even
    StopBits: 1

Then send the string '/?!\r\n' to the port, the meter sound response with something

    hex initString -> \x2F\x3F\x21\x0D\x0A

cuteCom its a good test propose tool to send and receive data, from serial COM, to install run:

    sudo apt-get update
    sudo apt-get install cutecom

## Suported Models so far ##

(see brands_models.py)

## Usefull links ##

(Manual do equipamento)
https://www.yumpu.com/en/document/read/39649016/me172-technical-description-iskraemeco-uk

https://github.com/openhab/openhab1-addons/wiki/IEC-62056---21-Meter-Binding
https://www.youtube.com/watch?v=fMvP2U-2cs4

(importante)
https://www.gurux.fi/node/5508

## Packed with ##

https://pyinstaller.org/en/stable/man/pyinstaller.html
https://realpython.com/pyinstaller-python/

pyinstaller main.py --onefile --name meterReader

## Regex ##

Regex expressions used

    re.findall("[\*]([0-9]+)", collected_data) # retrive factor
    re.findall("\(([\s:.0-9a-zA-Z^-]+|[\s0-9:]*\))", collected_data) #retrive values

    re.search("(^[0-9]+[-][0-9]+)", collected_data)  # X-Y
    re.findall("^[cC][.][0-9]+[.][0-9]+", collected_data) # C.X.Y 
    re.findall("^[0-9]*[.][0-9]*[.][0-9]*", collected_data) # XX.YY.ZZ

    re.search("[:]([0-9CF]*[.][0-9F]*[.][0-9F]*)", collected_data) # retrieve subcodes


## OBIS Code ##
https://onemeter.com/docs/device/obis/




