from meterReadings import *
from urllib.request import urlopen

# Create a meter object
meter = meter(init_device())

if(MODE=='READ'):

    # Start hand_shake
    meter.start_comm()

    # Read device info
    meter.device_info()
    print(f'Marca.....: {meter.brand}')
    print(f'Modelo....: {meter.model}')
    print(f'ID........: {meter.id}')

    meter.read_data()
    export_data('csv', 'data.csv')

else:
    print_message('TEST')
    meter.start_comm()
    meter.test_read()
