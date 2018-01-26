#!/usr/bin/env python

# pylint: disable=C0301, C0111, R0914, E0401

import json
from coinmarketcap import Market
from twython import Twython

# Constants
def main():

    ''' Run the tweet script '''

    with open('tokens.txt', 'r') as readfile:
        consumer_key = readfile.readline().strip()
        consumer_secret = readfile.readline().strip()
        access_token = readfile.readline().strip()
        access_secret = readfile.readline().strip()

    # Create a copy of the Twython object with all our keys and secrets to allow eas$
    api = Twython(consumer_key, consumer_secret, access_token, access_secret)

    market = Market()
    crypto = market.ticker(limit=200)
    coins_to_tweet = []
    positive_percent_threshold = 20.0
    negative_percent_threshold = -20.0

    for currency in crypto:
        hourly_percent = currency.get('percent_change_1h', '0.0')
        if hourly_percent:
            hourly_percent = float(hourly_percent)
            if hourly_percent >= positive_percent_threshold or hourly_percent <= negative_percent_threshold:
                name = currency.get('name', 'null')
                symbol = currency.get('symbol', 'null')
                url = 'https://coinmarketcap.com/currencies/' + currency.get('id', 'null')
                hourly_percent = format(hourly_percent, ',.2f') + '%'
                coins_to_tweet.append([name, symbol, str(hourly_percent), url])

    # Format: [name, symbol, hourly_percent, url] all strings
    for coin in coins_to_tweet:
        api.update_status(status=coin[0] + '(' + coin[1] + ') has changed ' + coin[2] + ' in the last hour!\n\n' + coin[3])

if __name__ == '__main__':
    main()
