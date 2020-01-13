import time as t
import smbus
import sys
import subprocess
import logging as log
import doorparameters as parameters

bus = smbus.SMBus(parameters.DEVICE_BUS)


def openWay(scanner):
    """ openWay(scanner) giving a scanner, send a signal through i2c to act with the door
    """

    try:
        bus.write_byte_data(
            parameters.CONFIG_SYSTEM[scanner]["dev_addr_op"],
            parameters.CONFIG_SYSTEM[scanner]["open_code"],
            parameters.ENABLE_DOOR
        )
        flag = 0 #to keep if all if correct
        t.sleep(parameters.WAIT_SECONDS_BLOCK_DOOR)
    
    except IOError:
        # Log the event a call i2cdetect to restart i2c system
        log.error('I2c writing error')
        flag = 1
        subprocess.call(['i2cdetect', '-y', '1'])


    finally:
        try:
            if parameters.CONFIG_SYSTEM[scanner]["close_code"] != 0:
                bus.write_byte_data(
                    parameters.CONFIG_SYSTEM[scanner]["dev_addr_cl"],
                    parameters.CONFIG_SYSTEM[scanner]["close_code"],
                    parameters.DISABLE_DOOR
                )
        except IOError:
            # Log the event and restart i2c
            log.error('I2c writing error')
            flag = 1
            subprocess.call(['i2cdetect', '-y', '1'])

    return flag # 0 = correct, 1 = error

    #bus.write_byte_data(parameters.DEVICE_ADDR_DOOR_1_OPEN, door, parameters.ENABLE_DOOR)
    # delay enough to block the door again
    #t.sleep(parameters.WAIT_SECONDS_BLOCK_DOOR)
    #bus.write_byte_data(parameters.DEVICE_ADDR_DOOR_1_CLOSE, door , parameters.DISABLE_DOOR)


##openWay(parameters.CODE_DOOR_1_OPEN)
##openWay(parameters.CODE_DOOR_1_CLOSE)
##openWay(3)
#openWay("scanner1")
#subprocess.call(['i2cdetect', '-y', '1'])