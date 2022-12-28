from meter import *
from urllib.request import urlopen

decode_to_obis_code('0-0:C.51.2*255(0221212163024)')

# # Create a meter object
# meter = meter(init_device())

# if(MODE=='READ'):

#     # Start hand_shake
#     meter.start_comm()

#     # Read device info
#     meter.device_info()
#     print(f'Marca.....: {meter.brand}')
#     print(f'Modelo....: {meter.model}')
#     print(f'ID........: {meter.id}')

#     meter.read_data()
#     export_data('csv', 'data.csv')

# else:
#     print_message('TEST')
#     meter.start_comm()
#     meter.test_read()
