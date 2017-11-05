#!/usr/bin/env python
import os
from time import localtime, strftime
from twython import Twython

# CONSTANTS
f = open("tokens.txt", "r")
CONSUMER_KEY= f.readline().strip()
CONSUMER_SECRET= f.readline().strip()
ACCESS_TOKEN= f.readline().strip()
ACCESS_SECRET= f.readline().strip()
f.close()

#Create a copy of the Twython object with all our keys and secrets to allow easy commands.
api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_SECRET)

# Celsius to Fahrenheit Converted
def ctof(temp):
	return str(float(temp)*(9/5)+32)

#Using our newly created object, utilize the update_status to send in the text passed in through CMD
cmd = '/opt/vc/bin/vcgencmd measure_temp'
line = os.popen(cmd).readline().strip()
temp = line.split('=')[1].split("'")[0]
tempf = ctof(temp)
time = strftime("%m-%d-%Y %H:%M:%S", localtime())
date, _time = time.split(' ')
api.update_status(status='CPU temperature is '+temp+' C | ' + tempf + ' F\n' + 'Current time is ' + _time  + '\nCurrent date is ' +  date)
