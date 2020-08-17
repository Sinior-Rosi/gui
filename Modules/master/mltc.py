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
color_ama(autoreset=True)

os.system('cls' if os.name=='nt' else 'clear')

# Get your own values from my.telegram.org
api_id = 1127509
api_hash = '7919be907884f1d388803b03f1994d78'


dogeclick_channel = 'Litecoin_click_bot'

# Date & Time Header
def print_msg_time(message):
	print('[' + Fore.YELLOW + f'{datetime.now().strftime("%H:%M:%S")}' + Fore.RESET + f'] {message}')

async def main():
	
	print(Fore.RED       + '       )  (    (    (              (        )  (               ) ')     
	print(Fore.RED       + ' (    ( /(  )\ ) )\ ) )\ )      (    )\ )  ( /(  )\ )  *   )  ( /( ')       
	print(Fore.RED       + '  )\   )\())(()/((()/((()/(      )\  (()/(  )\())(()/(` )  /(  )\()) ')    
	print(Fore.YELLOW    + ' (((_) ((_)\  /(_))/(_))/(_))   (((_)  /(_))((_)\  /(_))( )(_))((_)\ ')
	print(Fore.YELLOW    + ') )\___  _((_)(_)) (_)) (_))     )\___ (_)) __ ((_)(_)) (_(_())  ((_) ')
	print(Fore.YELLOW    + ')((/ __|| || || _ \|_ _|/ __|   ((/ __|| _ \ \ \ / /| _ \|_   _| / _ \ ')
	print(Fore.BLUE      + ' )| (__ | __ ||   / | | \__ \    | (__ |   /  \ V / |  _/  | |  | (_) |')
	print(Fore.BLUE      + '  \____||_||_||_|_\|___||___/     \___||_|_\   |_|  |_|    |_|   \___/ \n' + Fore.RESET)
	print(Fore.BLUE   + '                      BY :CHRIS CRYPTO GAMING \n' + Fore.RESET)
	print(Fore.BLUE   + '                  YT Channel : http://bit.ly/RCCYTC  \n' + Fore.RESET)                        
	print(Fore.BLUE   + '                 Visit Bots Script LITECOIN Clickbot \n' + Fore.RESET) 		


                      
	# Check if phone number is not specified
	if len(sys.argv) < 2:
		print('Usage: python start.py phone_number')
		print('-> Input number in international format (example: +11234567890)\n')
		e = input('Press any key to exit...')
		exit(1)
		
	phone_number = sys.argv[1]
	
	if not os.path.exists("session"):
		os.mkdir("session")
   
	# Connect to client
	client = TelegramClient('session/' + phone_number, api_id, api_hash)
	await client.start(phone_number)
	me = await client.get_me()
	
	print(Fore.GREEN + f'               Current account: {me.first_name}({me.username})\n' + Fore.RESET)
	print_msg_time('Sending /bots command')
	
	# Start command /bots
	await client.send_message(dogeclick_channel, '/bots')
	
	# Message the bot
	@client.on(events.NewMessage(chats=dogeclick_channel, incoming=True))
	async def join_start(event):
		message = event.raw_text
		if 'Forward a message to' in message:	
			channel_msg = event.original_update.message.reply_markup.rows[0].buttons[0].url
			print_msg_time(f'URL @{channel_msg}')
			
			if '?' in channel_msg:
				channel_name = re.search(r't.me\/(.*?)\?', channel_msg).group(1)
			elif '?' not in channel_msg:
				channel_name = re.search(r't.me\/(.*?)', channel_msg).group(1)
			
			print_msg_time(f'Messaging @{channel_name}...')
			await client.send_message(channel_name, '/start')
			
			# Forward the bot message
			@client.on(events.NewMessage(chats=channel_name, incoming=True))
			async def earned_amount(event):
				msg_id = event.message.id,
				await client.forward_messages(dogeclick_channel, msg_id, channel_name)
	
	# Print earned amount
	@client.on(events.NewMessage(chats=dogeclick_channel, incoming=True))
	async def earned_amount(event):
		message = event.raw_text
		if 'You earned' in message:	
			print_msg_time(Fore.GREEN + event.raw_text + '\n' + Fore.RESET)
			
	# No more ads
	@client.on(events.NewMessage(chats=dogeclick_channel, incoming=True))
	async def no_ads(event):
		message = event.raw_text
		if 'no new ads available' in message:	
			print_msg_time(Fore.RED + 'Sorry, there are no new ads available\n' + Fore.RESET)


			
	# No more ads - balance inquiry - close
	@client.on(events.NewMessage(chats=dogeclick_channel, incoming=True))
	async def no_ads(event):
		message = event.raw_text
		if 'Sorry, there are no' in message:	
			await client.send_message(dogeclick_channel, '/balance')
		if 'Available balance:' in message:
			print_msg_time(Fore.GREEN + event.raw_text + '\n' + Fore.RESET)



			exit(1)
			
	await client.run_until_disconnected()
	
asyncio.get_event_loop().run_until_complete(main())
    
    
    