from meter import *
import time

# Create a meter object
meter = meter(init_device())
timeStamp = str(time.time()).replace('.','_')

if(MODE=='READ'):
    # Start hand_shake
    meter.start_comm()

    # Read device info
    meter.device_info()
    print(f'\n{INFO_MESSAGES[LANGUAGE]["BRAND"]}\t: {meter.brand}')
    print(f'{INFO_MESSAGES[LANGUAGE]["MODEL"]}\t: {meter.model}')
    print(f'{INFO_MESSAGES[LANGUAGE]["ID"]}\t: {meter.id}\n')

    meter.read_data()

    # Export data to csv
    fileName = f'{meter.brand}_{meter.model}_{timeStamp}.csv'
    export_data('csv', fileName)

else:
    print_message('TEST')
    meter.start_comm()
    meter.test_read()
