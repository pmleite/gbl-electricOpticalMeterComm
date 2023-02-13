from meter import *
import time


def runProg():

    intro()
    hasPorts = get_serial_ports()

    if (hasPorts):
        # Create a meter object
        meter = meter(init_device())
        timeStamp = str(time.time()).replace('.','_')

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
        print_message("NO_PORTS")
        print_message("CHECK")


if __name__ == "__main__":
    runProg()

