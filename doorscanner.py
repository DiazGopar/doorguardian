#!/usr/bin/python3 -u
""" doorscanner stub file.
This module process the serial scanner to send the readed information to Web Servies and act with doors.
"""
import serial
import serial.threaded
import time
import logging as log
import doorwebrequest as wr
import doorphysical as phy
import doorparameters as parameters



class ProcessInput(serial.threaded.LineReader):
    """ProcessInput get a a Serial Threaded and process.
    We can add a callback function with addCallback() to process every input readed.
    And with function set_way() we can set with sense is associated with taht serial line (True=IN, False=OUT)."""
    
    cb = ()
    way = True
    #TERMINATOR = b'\r\n'
    
    def add_callback(self, callback: callable):
        self.cb = callback

    def set_way(self, value):
        self.way = value
    
    def connection_made(self, transport):
        super(ProcessInput, self).connection_made(transport)
        log.debug('port opened')
        

    def handle_line(self, data):
        log.debug('Data: {}'.format(repr(data)))
        #print(self.transport.getName())
        #print(self.way)
        response = wr.getWebResponse(data, self.way)
        log.debug(response)
        if response:
            self.cb(response)
        
        #print('line received: {}\n'.format(repr(data)))
        ##Call a function with Serial Number, User Code'''

    def connection_lost(self, exc):
        (self.way)
        if exc:
            print(exc)
            #traceback.print_exc(exc)
        log.debug('port closed')


#LOG related
log.basicConfig(
    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',
    #datefmt='%d-%b-%y %H:%M:%S',
    #filename='app.log',
    #filemode='a',
    level=log.DEBUG)
log.info('Iniciando DoorGuardian...')


#Serial Port assign
ser = serial.Serial(parameters.CONFIG_SYSTEM["scanner1"]["port"])
ser2 = serial.Serial(parameters.CONFIG_SYSTEM["scanner2"]["port"])

def func(data):
    log.info('Abriendo puerta 1 para entrada')
    phy.openWay("scanner1")
    return True

def func2(data):
    log.info('Abriendo puerta 1 para salida')
    phy.openWay("scanner2")
    return True

with serial.threaded.ReaderThread(ser, ProcessInput) as protocol1:
    protocol1.add_callback(func)
    protocol1.set_way(parameters.CONFIG_SYSTEM["scanner1"]["way"])
    with serial.threaded.ReaderThread(ser2, ProcessInput) as protocol2:
        protocol2.add_callback(func2)
        protocol2.set_way(parameters.CONFIG_SYSTEM["scanner2"]["way"])
        while True:
            time.sleep(1)

log.info('Saliendo de DoorGuardian.')