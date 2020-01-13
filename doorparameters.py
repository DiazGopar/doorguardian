'''API END_POINT'''
CENTER_CODE = 'PUT YOUR CENTER CODE HERE!!!!'
API_ENDPOINT = "PUT YOUR URL HERE!!!!"
URL_TIMEOUT = 3

'''QR Scanners config'''
IN_SCANNER = '/dev/ttyUSB0'
OUT_SCANNER = '/dev/ttyUSB1'
WAIT_SECONDS_BLOCK_DOOR = 2.5
NUM_SCANNERS = 2

'''I2C Bus Options'''
DEVICE_BUS = 1
PHY_DOORS_NUMBERS = 1
DEVICE_ADDR_DOOR_1_OPEN = 0x10
DEVICE_ADDR_DOOR_1_CLOSE = 0x10
CODE_DOOR_1_OPEN = 0x01
CODE_DOOR_1_CLOSE = 0x02
ENABLE_DOOR = 0xFF
DISABLE_DOOR = 0x00
NO_DEVICE_ADDR = 0x00

'''Door Logic'''
CONFIG_SYSTEM = {
    "scanner1" : {
        "port"        : IN_SCANNER,
        "dev_addr_op" : DEVICE_ADDR_DOOR_1_OPEN,
        "dev_addr_cl" : DEVICE_ADDR_DOOR_1_CLOSE,
        "open_code"   : CODE_DOOR_1_OPEN,
        "close_code"  : CODE_DOOR_1_OPEN,
        "way"         : True #'''True: WayIN'''
    },  
    "scanner2" : {
        "port"        : OUT_SCANNER,
        "dev_addr_op" : DEVICE_ADDR_DOOR_1_OPEN,
        "dev_addr_cl" : DEVICE_ADDR_DOOR_1_CLOSE,
        "open_code"   : CODE_DOOR_1_OPEN,
        "close_code"  : CODE_DOOR_1_OPEN,
        "way"         : False #'''False: WayOut'''
    }
}

#print(CONFIG_SYSTEM)