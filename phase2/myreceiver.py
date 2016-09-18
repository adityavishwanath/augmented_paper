#!/usr/bin/env python

# This code reads the data being printed out to the serial
# The data is the processed ***

import serial #Import Serial Library

# set the baudrate and serial port
arduinoSerialData = serial.Serial('com4', 115200)

# read in text file with hard coded values
# create a map of text to the web
f = open('new_map.txt', 'r')
nextline = f.readline()

# create a dictionary mapping text to coordinates
my_coordinates = {}
coordinate = [0, 0]

while (nextline):
    dummyvalues = nextline.split(",")
    item = dummyvalues[0]
    coordinate[0] = float(dummyvalues[1])
    coordinate[1] = float(dummyvalues[2])
    my_coordinates[item] = coordinate;
    nextline = f.readline()

# if the average of the last five values obtained from the arduino is within 1 cm of one of the coordinates on the file, do a google search on that word and return the first link

last_five_x = [0,0,0,0,0]
last_five_y = [0,0,0,0,0]

# reading from serial
while (1==1):
    if (arduinoSerialData.inWaiting()>0):
        myData = arduinoSerialData.readline()
        print myData
        if (myData):
            data = myData.split(",")
            del last_five_x[0]
            del last_five_y[0]
            last_five_x.append(float(data[0]))
            last_five_y.append(float(data[1]))
            avg_x = sum(last_five_x) / 5
            avg_y = sum(last_five_y) / 5
            for key in my_coordinates:
                if avg_x > (my_coordinates[key][0] - 2) and avg_x < (my_coordinates[key][0] + 2) and avg_y > (my_coordinates[key][1] - 2) and avg_y < (my_coordinates[key][1] + 2):
                    print key
