#!/usr/bin/env python

# This code reads the data being printed out to the serial
# The data is the processed ***

# DETERMINE ABC COORDINATE USING SONAR

import serial #Import Serial Library
import json

X_OFFSET = 0
Y_OFFSET = 0
X_FACTOR = 0.0
Y_FACTOR = 0.0

# read in text file with hard coded values
# create a map of text to the web
#f = open('new_map.txt', 'r')
#nextline = f.readline()

# read in json file with EVERYTHING
with open('output.json') as json_data:
    response = json.load(json_data)

for item in response['responses'][0]['textAnnotations']:
    if item['description'] != None:
        if item['description'] == 'ABC':
            coordinates = item['boundingPoly']['vertices']
            X_OFFSET = int(coordinates[0]['x'])
            Y_OFFSET = int(coordinates[0]['y'])
            X_FACTOR = (abs(int(coordinates[0]['x']) - int(coordinates[1]['x'])) + abs(int(coordinates[2]['x']) - int(coordinates[3]['x'])))/2.0
            Y_FACTOR = (abs(int(coordinates[0]['y']) - int(coordinates[2]['y'])) + abs(int(coordinates[1]['y']) - int(coordinates[3]['y'])))/2.0
            #print "DONE WITH COMPUTER VISION. PLEASE PLACE THE PAPER ON THE CARDBOARD."
            break

# create a dictionary mapping text to coordinates
#my_coordinates = {}
#coordinate = [0, 0]

#while (nextline):
#    dummyvalues = nextline.split(",")
#    item = dummyvalues[0]
#    coordinate[0] = float(dummyvalues[1])
#    coordinate[1] = float(dummyvalues[2])
#    my_coordinates[item] = coordinate;
#    nextline = f.readline()

# if the average of the last five values obtained from the arduino is within 1 cm of one of the coordinates on the file, do a google search on that word and return the first link

last_five_x = [0,0,0,0,0]
last_five_y = [0,0,0,0,0]
x_left = 0
y_top = 0
x_right = 0
y_bot = 0

# set the baudrate and serial port
arduinoSerialData = serial.Serial('com4', 115200)

# reading from serial
while (1==1):
    if (arduinoSerialData.inWaiting()>0):
        myData = arduinoSerialData.readline()
        if (myData):
            data = myData.split(",")
            del last_five_x[0]
            del last_five_y[0]
            last_five_x.append(float(data[0]))
            last_five_y.append(float(data[1]))
            avg_x = (sum(last_five_x) / 5) * X_FACTOR # add shift
            avg_y = (sum(last_five_y) / 5) * Y_FACTOR # add shift
            for item in response['responses'][0]['textAnnotations']:
                coordinates = item['boundingPoly']['vertices']
                x_left = (int(coordinates[0]['x']) + int(coordinates[3]['x']))/2
                x_right = (int(coordinates[1]['x']) + int(coordinates[2]['x']))/2
                y_top = (int(coordinates[0]['y']) + int(coordinates[1]['y']))/2
                y_bot = (int(coordinates[2]['y']) + int(coordinates[3]['y']))/2
                if avg_x > x_left and avg_x < x_right and avg_y > y_bot and avg_y < y_top:
                    print key
