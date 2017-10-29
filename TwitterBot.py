#!/usr/bin/env python
import os
from time import localtime, strftime
from twython import Twython

# CONSTANTS
CONSUMER_KEY='P105USm5vwonG8PDCiuMPbDea'
CONSUMER_SECRET='mL2X18a7tViSFiUUw33DoWj652La4tQl0vmcen6x2lH5HSkVV9'
ACCESS_TOKEN='921503207616065539-mU9LOrWaopR3Mj6azxssXuA22flUPht'
ACCESS_SECRET='CEkjmeHwGHsctjDs7LPSyaiNu9vLnYDsyzZgjZW4sufrS'

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
