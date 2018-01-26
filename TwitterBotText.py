#!/usr/bin/env python
import sys
from time import localtime, strftime
from twython import Twython

# CONSTANTS
def main():
    with open('tokens.txt', 'r') as readfile:
        CONSUMER_KEY= readfile.readline().strip()
        CONSUMER_SECRET= readfile.readline().strip()
        ACCESS_TOKEN= readfile.readline().strip()
        ACCESS_SECRET= readfile.readline().strip()

    #Create a copy of the Twython object with all our keys and secrets to allow eas$
    api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_SECRET)

    #Using our newly created object, utilize the update_status to send in the text $
    time = strftime("%m-%d-%Y %H:%M:%S", localtime())
    date, _time = time.split(' ')
    api.update_status(status=sys.argv[1]+'\nCurrent time is ' + _time + '\nCurrent date is ' + date)

if __name__ == '__main__':
    main()
