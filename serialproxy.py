import time, sys, serial
import collections
import re
from serial import SerialException
from termcolor import colored

SERIALPORT1 = "/dev/rfcomm0"  # the default com/serial port the receiver is connected to
BAUDRATE1 = 115200      # default baud rate we talk to Moteino

SERIALPORT2 = "/dev/ttyUSB0"  # the default com/serial port the receiver is connected to
BAUDRATE2 = 9600      # default baud rate we talk to Moteino


# MAIN()
if __name__ == "__main__":
    try:
        # open up the FTDI serial port to get data transmitted to Moteino
        ser1 = serial.Serial(SERIALPORT1, BAUDRATE1, timeout=1) #timeout=0 means nonblocking
        ser1.flushInput();
        print "\nCOM Port [", SERIALPORT1, "] found \n"
    except (IOError, SerialException) as e:
        print "\nCOM Port [", SERIALPORT1, "] not found, exiting...\n"
        exit(1)

    try:
        # open up the FTDI serial port to get data transmitted to Moteino
        ser2 = serial.Serial(SERIALPORT2, BAUDRATE2, timeout=1) #timeout=0 means nonblocking
        ser2.flushInput();
        print "\nCOM Port [", SERIALPORT2, "] found \n"
    except (IOError, SerialException) as e:
        print "\nCOM Port [", SERIALPORT2, "] not found, exiting...\n"
        exit(1)

    try:    

        while 1:
            ser1_waiting = ser1.inWaiting()
            if ser1_waiting > 0:
                #rx1 = ser1.read(ser1_waiting)
                rx1 = ser1.readline()
                ser2.write(rx1)
                print colored(rx1, 'red')
            ser2_waiting = ser2.inWaiting()
            if ser2_waiting > 0:
                #rx2 = ser2.read(ser2_waiting)
                rx2 = ser2.readline()
                ser1.write(rx2)
                print rx2       


    except IOError:
        print "Some IO Error found, exiting..." `

