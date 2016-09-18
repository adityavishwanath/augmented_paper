# This code reads the data being printed out to the serial
# The data is the processed ***

import serial #Import Serial Library

arduinoSerialData = serial.Serial('com4', 115200)

# read in text file with hard coded values


# if the average of the last five values obtained from the arduino is within 1 cm of one of the coordinates on the file, do a google search on that word and return the first link

while (1==1):
    if (arduinoSerialData.inWaiting()>0):
        myData = arduinoSerialData.readline()
        print myData
