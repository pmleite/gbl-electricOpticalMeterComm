from time import sleep
from setup import *
from serial import Serial as serial
from obis_codes import *
import pandas as pd

class meter:

    # Contructor
    def __init__(self, device):

        self.device = device
        self.brand = ''
        self.model = ''
        self.id = ''

    # Handshake
    def start_comm(self):
        
        # Send init string
        self.device.write(ME172_INIT_STRING.encode('utf-8'))
        # Send Acknowledge
        print_message('START')
        self.device.write(ACK.encode('utf-8'))
        clear_buffer(self)


    # Read device info
    def device_info(self):

        # Check if it is a valid response
        response = self.device.readline().decode('utf-8').replace('\r\n','')
        
        # This method should be improved to handle more types of responses
        # Types of model responses
        # Manufacturer     type response            Manufacturer/Model       ID (I think!)  
        #   ISKRA          /ISk5MT174-0001           /ISk5MT174                 0001
        #   LANDIS         /LGZ4\\2ZMD3102400.B31    /LGZ4\\2ZMD3102400         B31

        if(response[0] == '/'):

            if '-' in response:
                data = response.split('-')
            if '.' in response:
                data = response.split('.')

            print_message('INFO')
            self.brand = BRANDS_MODELS[data[0]]["brand"]
            self.model = BRANDS_MODELS[data[0]]["model"]
            self.id    = data[1]
            clear_buffer(self)
            
        else:
            print_message('ERROR')
            self.device.close()
            exit()

    #Chekc STX
    def check_STX(self):
        response = self.device.read(1).decode('utf-8')

        if (response == STX):
            print_message('COLLECTING')
            return True
        else:
            print_message('STX_ERROR')
            self.device.close()
            exit()

    #Read device data
    def read_data(self):

        if (self.check_STX()):
            reading = True
           
            while(reading):
                response = self.device.readline().decode('utf-8').replace('\r\n','')
                if (response[0] == '!'): reading=False
                process_data(response)
                decode_obis_code(response)

            print_message('SUCCESS')
            self.device.close()
            
        else:
            print_message('ERROR')
            self.device.close()
            exit()
           
    # Read for test proposes
    def test_read(self):
        print_message('TEST')
        while True:
            response = self.device.readline().decode('utf-8').replace('\r\n','')
            print(response)

# Process data
def process_data(data):
    if (data[0] != '!'):
        list = data.split('(')
        list[1] = list[1].replace(')','')
        #Store data in a dictionary
        DATA_COLLECTED[list[0]]=list[1]
    else:
        print('')

# Print data
def print_data():
    print_message('COLLECTED')
    for key,value in DATA_COLLECTED.items():
        print(f'CODE: {key}\t  VALUE: {value}')

# Export data to CSV
def export_data(type, filename):

    if (type == 'csv'):
        df = pd.DataFrame(DATA_COLLECTED.items(), columns=['CODE', 'VALUE'])
        df.to_csv(filename, index=False)
        print_message('CSV')
    else:
        print_message('INVALID_TYPE')
    
# Create a serial port object
def init_device():
    comSettings = serial(DEVICE, BAUD, DATA, PARITY, timeout=TIMEOUT)
    return comSettings

# Clear the buffer
def clear_buffer(self):
    sleep(SLEEP_DELAY)
    self.device.reset_input_buffer()
    self.device.reset_output_buffer()

# Print Mess in the console
def print_message(msg):
    if (LANGUAGE == 'PT' or LANGUAGE == 'FR'):
        print(f'{INFO_MESSAGES[LANGUAGE][msg]}')
    else:
        print(f'{INFO_MESSAGES["EN"][msg]}')

