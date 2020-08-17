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
dogeclick_channel = 'Litecoin_click_bot'

# Date & Time Header
def print_msg_time(message):
    print('[' + Fore.YELLOW + f'{datetime.now().strftime("%H:%M:%S")}' + Fore.RESET + f'] {message}')

def get_response(url, method='GET', data=None):
    response = requests.request(method, url, data=data, headers=header_object, timeout=15, allow_redirects=False)
    text_response = response.text
    status_code = response.status_code
    return[status_code, text_response]
    
def log(message, addnewline=False):
    if not addnewline:
        print('[' + Fore.YELLOW + f'{datetime.now().strftime("%H:%M:%S")}' + Fore.RESET + f'] {message}')
    else:
        print('[' + Fore.YELLOW + f'{datetime.now().strftime("%H:%M:%S")}' + Fore.RESET + f'] {message}', end='\n\n')

def wait_for(seconds):
    for x in range(0, seconds + 1):
        sys.stdout.write('[%s] Waiting %s seconds! %d\r' % (datetime.now().strftime("%H:%M:%S"), seconds, x))
       
        
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
    print(Fore.BLUE   + '                Visit Sites Script LITECOIN Clickbot \n' + Fore.RESET)

    
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
    print_msg_time('Sending /visit command...')


    # Start command /visit  
    await client.send_message(dogeclick_channel, '/visit')

    # Start visiting the ads
    @client.on(events.NewMessage(chats=dogeclick_channel, incoming=True))
    async def visit_ads(event):
        original_update = event.original_update
        if type(original_update)is not UpdateShortMessage:
            if hasattr(original_update.message,'reply_markup') and type(original_update.message.reply_markup) is ReplyInlineMarkup:
                url = event.original_update.message.reply_markup.rows[0].buttons[0].url
                
                if url is not None:
                    log('Clicking Go To Website...')
                    log(Fore.CYAN + f'Please Wait. . . . ' + Fore.RESET)
                    max_loops=15
                    current_loops=1

                while True:
                    (status,text_response) = get_response(url)
                    parse_data = BeautifulSoup(text_response,'html.parser')
                    captcha = parse_data.find('div',{'class':'g-recaptcha'})
                    headbar = parse_data.find('div',{'id':'headbar'})
                    
                    if status==302:
                        sys.stdout.write(Fore.CYAN +'[%s] STATUS: %s (%d)\r'%(datetime.now().strftime("%H:%M:%S"),'FALSE' if captcha is not None else 'Timer Verified', current_loops))
                        break

                    
                        if status==200 and captcha is None:
                            code=headbar.get('data-code')
                            wait_time=headbar.get('data-timer')
                            token=headbar.get('data-token')
                            wait_for(int(wait_time))
                            requests.post('url', data={'code':code,'token':token}, headers=header_object, allow_redirects=False)
                            break
                                
                    elif captcha is not None:
                        log(Fore.RED + 'Captcha detected!!! Skipping ads...\n') 

                    # Clicks the skip
                        await client(GetBotCallbackAnswerRequest(
                            peer=dogeclick_channel,
                            msg_id=event.message.id,
                            data=event.message.reply_markup.rows[1].buttons[1].data
                        ))
                    

                    elif max_loops==current_loops:
                        current_loops+=0
                                              

                # Print earned money
                @client.on(events.NewMessage(chats=dogeclick_channel, incoming=True))
                async def wait_hours(event):
                    message = event.raw_text

                    if 'You earned' in message:	
                        log(Fore.GREEN + f'{message}\n' + Fore.RESET)

        # No more ads
        @client.on(events.NewMessage(chats=dogeclick_channel, incoming=True))
        async def no_ads(event):
            message = event.raw_text
            if 'Alerts for new click task' in message:
                print_msg_time(Fore.CYAN + f'No click ads available.' + Fore.RESET)
                print_msg_time('Sending /balance command')
                await client.send_message(dogeclick_channel, '/balance')

            if 'Available balance:' in message:
                print_msg_time(Fore.GREEN + f'{message}\n' + Fore.RESET)

                exit(1)    
    await client.run_until_disconnected()
	
asyncio.get_event_loop().run_until_complete(main())