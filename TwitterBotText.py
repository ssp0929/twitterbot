#!/usr/bin/env python
import sys
from time import localtime, strftime
from twython import Twython

# CONSTANTS
CONSUMER_KEY='P105USm5vwonG8PDCiuMPbDea'
CONSUMER_SECRET='mL2X18a7tViSFiUUw33DoWj652La4tQl0vmcen6x2lH5HSkVV9'
ACCESS_TOKEN='921503207616065539-mU9LOrWaopR3Mj6azxssXuA22flUPht'
ACCESS_SECRET='CEkjmeHwGHsctjDs7LPSyaiNu9vLnYDsyzZgjZW4sufrS'

#Create a copy of the Twython object with all our keys and secrets to allow eas$
api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_SECRET)

#Using our newly created object, utilize the update_status to send in the text $
time = strftime("%m-%d-%Y %H:%M:%S", localtime())
date, _time = time.split(' ')
api.update_status(status=sys.argv[1]+'\nCurrent time is ' + _time + '\nCurrent date is ' + date)

