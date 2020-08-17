# Auto Master (/visit /join /bots)
# Chris Crypto Gaming & Financials
# Youtube Channel : http://bit.ly/RCCYTC
# Website : http://bit.ly/RealChrisCrypto
# E-mail : chriscryptogaming@gmail.com 
# ETH Donations : 0xf410dCC5b41BF683390aCF0d6D2f0CCb198f3f86 
# BTC Donations : 19JEQQ3FbwBbgJToqeaS96SUv9rdJDcQaY 
# Doge Donations : DFAZXeBAqnmcLzi3feWFRcdvXUfQbtdH1R 
# ZEC Donations : t1S3drdqhXuPy98AYyyFxMbELxrJzWo8PTd 
# LTC Donations : LcvCV8myf1zSNwV6WCcfR1Tg6RcFv8nHZU 
# BCH Donations : qq95y380apm20xhrjtrc29y6vetuv8qgrvy8p3nwaf 
# LTC Clickbot : http://bit.ly/2yOlhbx 
# Doge Clickbot :http://bit.ly/3eAeQbb 
# ZEC Clickbot : http://bit.ly/2XGncqW 
# BTC Clickbot : http://bit.ly/2TVPDQB 
# BCH Clickbot : http://bit.ly/2B9DqBd 
# Support us on Brave! : http://bit.ly/3dgZ98w
# Download Cryptotab : http://bit.ly/36pmJN


#Imports
import asyncio
import logging
import re
import time
import os
import sys
import requests

logging.basicConfig(level=logging.ERROR)

from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from datetime import datetime
from colorama import Fore, init as color_ama
from bs4 import BeautifulSoup
from telethon.tl.types import UpdateShortMessage,ReplyInlineMarkup,KeyboardButtonUrl

color_ama(autoreset=True)

header_object={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}

os.system('cls' if os.name=='nt' else 'clear')

# my.telegram.org values, get your own there
api_id = 800812
api_hash = 'db55ad67a98df35667ca788b97f771f5'

# Set for which option you want
dogeclick_channel = 'Bitcoinclick_bot'

# Date & Time Header
def print_msg_time(message):
    print('[' + Fore.YELLOW + f'{datetime.now().strftime("%H:%M:%S")}' + Fore.RESET + f'] {message}')

#Personalized Message
async def main():

    print(Fore.RED       + '       )  (    (    (              (        )  (               ) ')     
    print(Fore.RED       + ' (    ( /(  )\ ) )\ ) )\ )      (    )\ )  ( /(  )\ )  *   )  ( /( ')       
    print(Fore.RED       + '  )\   )\())(()/((()/((()/(      )\  (()/(  )\())(()/(` )  /(  )\()) ')    
    print(Fore.YELLOW    + ' (((_) ((_)\  /(_))/(_))/(_))   (((_)  /(_))((_)\  /(_))( )(_))((_)\ ')
    print(Fore.YELLOW    + ') )\___  _((_)(_)) (_)) (_))     )\___ (_))  __ ((_)(_)) (_(_()) ((_) ')
    print(Fore.YELLOW    + ')((/ __|| || || _ \|_ _|/ __|   ((/ __|| _ \ \ \ / /| _ \|_   _| / _ \ ')
    print(Fore.BLUE      + ' )| (__ | __ ||   / | | \__ \    | (__ |   /  \ V / |  _/  | |  | (_) |')
    print(Fore.BLUE      + '  \____||_||_||_|_\|___||___/     \___||_|_\   |_|  |_|    |_|   \___/ \n' + Fore.RESET)
    print(Fore.BLUE   + '                      BY :CHRIS CRYPTO GAMING \n' + Fore.RESET)
    print(Fore.BLUE   + '                  YT Channel : http://bit.ly/RCCYTC  \n' + Fore.RESET)                        
    print(Fore.BLUE   + '                Join Channels Script BITCOIN Clickbot \n' + Fore.RESET)  
    # Check if phone number is not specified
    if len(sys.argv) < 2:
        print('Usage: python start.py phone_number')
        print('-> Input number in international format (example: +12223334444)\n')
        e = input('Press any key to exit...')
        exit(1)
    
    phone_number = sys.argv[1]

    if not os.path.exists("session"):
        os.mkdir("session")
   
    # Connect to client
    client = TelegramClient('session/' + phone_number, api_id, api_hash)
    await client.start(phone_number)
    me = await client.get_me()

    # Current account & username
    print(Fore.GREEN + f'               Current account: {me.first_name}({me.username})\n' + Fore.RESET)
    print_msg_time('Sending /join command')
    # Start command /join
    await client.send_message(dogeclick_channel, '/join')
  
    # Join channel
    time.sleep(5)
    @client.on(events.NewMessage(chats=dogeclick_channel, incoming=True))
    async def join_start(event):
        message = event.raw_text
        if 'You must join' in message:
            channel_name = re.search(r'You must join @(.*?) to earn', message).group(1)
            print_msg_time(f'Joining @{channel_name}...')
      
      
            # Verifying Join
            await client(JoinChannelRequest(channel_name))
            print_msg_time(f'Verifying... Please wait up to 30s due to Timeout\Spam Join Prevention...')
     
      
            # Clicks joined button
            time.sleep(7)
            await client(GetBotCallbackAnswerRequest(
                peer=dogeclick_channel,
                msg_id=event.message.id,
                data=event.message.reply_markup.rows[0].buttons[1].data
            ))
            time.sleep(7)
      
    # Print waiting hours
    @client.on(events.NewMessage(chats=dogeclick_channel, incoming=True))
    async def wait_hours(event):
        message = event.raw_text
        if 'You must stay' in message:  
            waiting_hours = re.search(r'at least (.*?) to earn', message).group(1)
            print_msg_time(Fore.GREEN + f'Verified Success! Please wait {waiting_hours} to earn reward\n' + Fore.RESET)
            time.sleep(12)
      
    # No more ads
    @client.on(events.NewMessage(chats=dogeclick_channel, incoming=True))
    async def no_ads(event):
        message = event.raw_text
        if 'Alerts for new join task' in message:
            print_msg_time(Fore.CYAN + f'No click ads available.' + Fore.RESET)
            print_msg_time('Sending /balance command')
            await client.send_message(dogeclick_channel, '/balance')

        if 'Available balance:' in message:
            print_msg_time(Fore.GREEN + f'{message}\n' + Fore.RESET)

            exit(1)    
    await client.run_until_disconnected()
	
asyncio.get_event_loop().run_until_complete(main())
    