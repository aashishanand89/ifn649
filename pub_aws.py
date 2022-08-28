import serial
import time
import paho.mqtt.publish as publish
import string

ser = serial.Serial("/dev/rfcomm0", 9600)
ser.write(str.encode('Start\r\n'))

while True:
    if ser.in_waiting > 0:
        rawserial = ser.readline()
        serialOut = rawserial.decode('utf-8').strip('\r\n')
        print(serialOut)
        publish.single("ifn649", serialOut, hostname="18.142.96.176")
        print("Done")
