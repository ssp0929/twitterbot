#!/usr/bin/env python

# pylint: disable=C0301, C0111, R0914, E0401, C0103

import json
import discord
from discord.ext import commands
from coinmarketcap import Market
from twython import Twython

# define bot + data
bot = commands.Bot(command_prefix="?")
coins_to_tweet = []

@bot.event
async def on_ready():
    if coins_to_tweet:
        text = '```https://twitter.com/cmccryptoalerts\n\n'
        for coin in coins_to_tweet:
            text += coin[0] + ' (' + coin[1] + ') ' + coin[2] + ' this hour (' + coin[3] + ' today)\n$' + coin[5] + ' | ' + coin[6] + ' BTC | ' + coin[7] + ' ETH\n\n'
        text += '```'
        await bot.send_message(bot.get_channel('406328703304335371'), text)
    await bot.logout()

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
    positive_percent_threshold = 15.0
    negative_percent_threshold = -15.0

    for currency in crypto:
        hourly_percent = currency.get('percent_change_1h', '0.0')
        if hourly_percent:
            hourly_percent = float(hourly_percent)
        daily_percent = currency.get('percent_change_24h', '0.0')
        if daily_percent:
            daily_percent = float(daily_percent)

        if hourly_percent >= positive_percent_threshold or hourly_percent <= negative_percent_threshold:
            name = currency.get('name', 'null')
            symbol = currency.get('symbol', 'null')
            url = 'https://coinmarketcap.com/currencies/' + currency.get('id', 'null')
            usd = float(currency.get('price_usd', '0.0'))
            usd_ = usd
            btc = format(float(currency.get('price_btc', '0.0')), ',f')
            eth = market.ticker('ethereum')[0].get('price_usd')
            hourly_percent = format(hourly_percent, ',.2f') + '%'
            daily_percent = format(daily_percent, ',.2f') + '%'
            if usd >= 1.0:
                usd = format(float(usd), ',.2f')
            elif usd < 1.0:
                usd = format(float(usd), ',f')
            if usd != 0:
                eth = format(float(usd_)/float(eth), ',f')
            coins_to_tweet.append([name, symbol, str(hourly_percent), str(daily_percent), url, str(usd), str(btc), str(eth)])

    with open('log.json', 'w') as outfile:
        json.dump(coins_to_tweet, outfile)

    # Format: [name, symbol, hourly_percent, url] all strings
    if coins_to_tweet:
        for coin in coins_to_tweet:
            hashtag = ''.join(coin[0].split(' '))
            if '-' in hashtag:
                hashtag = hashtag.replace('-', '')
            text = coin[0] + ' (' + coin[1] + ') ' + coin[2] + ' this hour (' + coin[3] + ' today)\n$' + coin[5] + ' | ' + coin[6] + ' BTC | ' + coin[7] + ' ETH\n#' + hashtag + ' #' + coin[1] + '\n' + coin[4]
            api.update_status(status=text)

    return coins_to_tweet

if __name__ == '__main__':
    coins_to_tweet = main()

    with open('discordcred.txt', 'r') as readfile:
        email = readfile.readline().strip()
        password = readfile.readline().strip()

    bot.run(email, password)
