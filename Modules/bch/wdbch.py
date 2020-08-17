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

from telethon.tl.types import UpdateShortMessage,ReplyInlineMarkup,KeyboardButtonUrl
from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from datetime import datetime
from colorama import Fore, init as color_ama
from bs4 import BeautifulSoup

color_ama(autoreset=True)

header_object={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}

os.system('cls' if os.name=='nt' else 'clear')

# my.telegram.org values, get your own there
api_id = 800812
api_hash = 'db55ad67a98df35667ca788b97f771f5'

# Set for which option you want
dogeclick_channel = 'BCH_clickbot'

# Date & Time Header
def print_msg_time(message):
	print('[' + Fore.YELLOW + f'{datetime.now().strftime("%H:%M:%S")}' + Fore.RESET + f'] {message}')

def get_response(url, method='GET'):
	response = requests.request(method, url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}, timeout=15)
	text_response = response.text
	status_code = response.status_code
	return[status_code, text_response]
	
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
    print(Fore.BLUE   + '                Withdrawal Script BITCOINCASH Clickbot \n' + Fore.RESET)  
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
    print(Fore.GREEN + f'               Current account: {me.first_name}({me.username})\n\n' + Fore.RESET)
    print_msg_time(Fore.CYAN +f'Script Started... Starting withdrawal...\n' + Fore.RESET)



# Starting Visit Sites
    await client.send_message(dogeclick_channel, '/withdraw')
    
# Balance at minimum withdrawal - Requesting withdrawal
    @client.on(events.NewMessage(chats=dogeclick_channel, incoming=True))
    async def wait_hours(event):
        message = event.raw_text
        if 'To withdraw, enter your' in message:
            waiting_hours = re.search(r'Your balance: (.*?) BCH', message).group(1)
            print_msg_time(Fore.GREEN + f'Verified Success! Withdrawing {waiting_hours} BCH\n' + Fore.RESET)
            await client.send_message(dogeclick_channel, 'qq95y380apm20xhrjtrc29y6vetuv8qgrvy8p3nwaf')
            time.sleep(3)
            
            await client.send_message(dogeclick_channel, waiting_hours)

# Withdrawal balance too small
        elif 'Minimum withdrawal:' in message:
            print_msg_time(Fore.CYAN + f'Available balance is to small for withdrawal...\n' + Fore.RESET)
            print_msg_time(Fore.RED + f'Script Complete... Goodbye...\n\n' + Fore.RESET)

            exit(1)
            
# Confirming withdrawal - Script sleep
    @client.on(events.NewMessage(chats=dogeclick_channel, incoming=True))
    async def wait_hours2(event):
        message = event.raw_text
        if 'Your balance:' in message:
            waiting_hours = re.search(r'Your balance: (.*?) BCH', message).group(1)
            print_msg_time(Fore.CYAN + f'Success... Withdrawal of {waiting_hours} BCH Complete!!!\n' + Fore.RESET)
            
        if 'Are you sure you want to send' in message:
            print_msg_time(Fore.CYAN + f'Sending Confirmation...\n' + Fore.RESET)
            await client.send_message(dogeclick_channel, '/confirm')
            print_msg_time(Fore.RED + f'Script Complete... Goodbye...\n\n' + Fore.RESET)


    
            exit(1)
    await client.run_until_disconnected()
    
asyncio.get_event_loop().run_until_complete(main())