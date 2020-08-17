# Auto Master (/visit /join /bots)
# Chris Crypto Gaming & Financials
# Youtube Channel : http://bit.ly/RCCYTC
# Website : http://bit.ly/RealChrisCrypto
# E-mail : chriscryptogaming@gmail.com 
# ETH Donations : 0xf410dCC5b41BF683390aCF0d6D2f0CCb198f3f86 
# BTC Donations : 1C7SVC1mPBcXPYwq2jM765MKgQLm1S7DkY 
# Doge Donations : DDn8sexiCcpi4MSCA1NPGz3G6vJLFRUKQj 
# ZEC Donations : t1SgzYXhusasn7xaMzBhqE3Lfx4fBfrEFyF 
# LTC Donations : ltc1qqwzdz03z6h5y5382lgvyhsuykzcrz580mj89u9 
# BCH Donations : qqzjvgs0s2leev5gtam6cfm6fqch0kxw9q3narmjj4 
# LTC Clickbot : http://bit.ly/35ME9Cq 
# Doge Clickbot : http://bit.ly/35RO21J 
# ZEC Clickbot : http://bit.ly/37WdN2L 
# BTC Clickbot : http://bit.ly/2sAM1Zz 
# BCH Clickbot : http://bit.ly/2R9GymM 
# Support us on Brave! : http://bit.ly/CCGBrave 
# Download Cryptotab : http://bit.ly/27650966

#Imports
import asyncio
import logging
import re
import time
import os 
import sys
import requests
import random

logging.basicConfig(level=logging.ERROR)

from telethon.tl.types import UpdateShortMessage,ReplyInlineMarkup,KeyboardButtonUrl
from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from datetime import datetime
from colorama import Fore, init as color_ama
from bs4 import BeautifulSoup

color_ama(autoreset=True)
os.system('cls' if os.name=='nt' else 'clear')


def Die():
    print ("This program has stopped")

def print_menu():
#  print (Fore.YELLOW  + """************** Welcome to Chris Crypto Clickbot Scripts ***************""" + Fore.RESET)
  print (Fore.RED       + '       )  (    (    (        (    )  (         ) ')     
  print (Fore.RED       + ' (    ( /(  )\ ) )\ ) )\ )      (    )\ )  ( /(  )\ )  *   )  ( /( ')       
  print (Fore.RED       + '  )\   )\())(()/((()/((()/(      )\  (()/(  )\())(()/(` )  /(  )\()) ')    
  print (Fore.YELLOW    + ' (((_) ((_)\  /(_))/(_))/(_))   (((_)  /(_))((_)\  /(_))( )(_))((_)\ ')
  print (Fore.YELLOW    + ') )\___  _((_)(_)) (_)) (_))     )\___ (_))  __ ((_)(_)) (_(_()) ((_) ')
  print (Fore.YELLOW    + ')((/ __|| || || _ \|_ _|/ __|   ((/ __|| _ \ \ \ / /| _ \|_   _| / _ \ ')
  print (Fore.BLUE      + ' )| (__ | __ ||   / | | \__ \    | (__ |   /  \ V / |  _/  | |  | (_) |')
  print (Fore.BLUE      + '  \____||_||_||_|_\|___||___/     \___||_|_\   |_|  |_|    |_|   \___/ \n' + Fore.RESET)
  print (Fore.BLUE   + '    BY :CHRIS CRYPTO GAMING \n' + Fore.RESET)
  print (Fore.BLUE   + '    YT Channel : http://bit.ly/CCGYTC  \n' + Fore.RESET)       
  

  print (Fore.YELLOW + """******************************** MENU ********************************""" + Fore.RESET)
  print (Fore.GREEN + "1. DOGE Clickbot" + Fore.RESET)
  print (Fore.GREEN + "2. BTC Clickbot" + Fore.RESET)
  print (Fore.GREEN + "3. LTC Clickbot" + Fore.RESET)
  print (Fore.GREEN + "4. ZEC Clickbot" + Fore.RESET)
  print (Fore.GREEN + "5. BCH Clickbot" + Fore.RESET)
  print (Fore.GREEN + "6. All Clickbots (LTC > ZEC > DOGE > BCH > BTC" + Fore.RESET) 
  print (Fore.RED   + "7. Exit" + Fore.RESET)
  print (Fore.YELLOW + """**********************************************************************""")
    
def Doge_Menu():
    print (Fore.YELLOW  + """********** Welcome to Chris Crypto Doge Clickbot Scripts **************""" + Fore.RESET)
    print (Fore.RED       + '       )  (    (    (        (    )  (         ) ')     
    print (Fore.RED       + ' (    ( /(  )\ ) )\ ) )\ )      (    )\ )  ( /(  )\ )  *   )  ( /( ')       
    print (Fore.RED       + '  )\   )\())(()/((()/((()/(      )\  (()/(  )\())(()/(` )  /(  )\()) ')    
    print (Fore.YELLOW    + ' (((_) ((_)\  /(_))/(_))/(_))   (((_)  /(_))((_)\  /(_))( )(_))((_)\ ')
    print (Fore.YELLOW    + ') )\___  _((_)(_)) (_)) (_))     )\___ (_))  __ ((_)(_)) (_(_()) ((_) ')
    print (Fore.YELLOW    + ')((/ __|| || || _ \|_ _|/ __|   ((/ __|| _ \ \ \ / /| _ \|_   _| / _ \ ')
    print (Fore.BLUE      + ' )| (__ | __ ||   / | | \__ \    | (__ |   /  \ V / |  _/  | |  | (_) |')
    print (Fore.BLUE      + '  \____||_||_||_|_\|___||___/     \___||_|_\   |_|  |_|    |_|   \___/ \n' + Fore.RESET)
    print (Fore.BLUE   + '    BY :CHRIS CRYPTO GAMING \n' + Fore.RESET)
    print (Fore.BLUE   + '    YT Channel : http://bit.ly/CCGYTC  \n' + Fore.RESET)       

    print (Fore.YELLOW + """******************************** MENU ********************************""" + Fore.RESET)
    print (Fore.GREEN + "1. Doge - Visit Sites" + Fore.RESET) 
    print (Fore.GREEN + "2. Doge - Message Bots" + Fore.RESET) 
    print (Fore.GREEN + "3. Doge - Join Channels" + Fore.RESET) 
    print (Fore.GREEN + "4. Doge All 3 - (Visit Sites, Message Bot, Join Channels)" + Fore.RESET)
    print (Fore.GREEN + "5. Doge All 3 - (Visit Sites, Message Bot, Join Channels) + Withdrawal " + Fore.RESET)
    print (Fore.GREEN + "6. Doge - Withdrawal Only" + Fore.RESET)
    print (Fore.RED   + "7. Exit" + Fore.RESET)
    print (Fore.YELLOW + """**********************************************************************""")

def BTC_Menu():
    print (Fore.YELLOW  + """********** Welcome to Chris Crypto BTC Clickbot Scripts ***************""" + Fore.RESET)
    print (Fore.RED       + '       )  (    (    (        (    )  (         ) ')     
    print (Fore.RED       + ' (    ( /(  )\ ) )\ ) )\ )      (    )\ )  ( /(  )\ )  *   )  ( /( ')       
    print (Fore.RED       + '  )\   )\())(()/((()/((()/(      )\  (()/(  )\())(()/(` )  /(  )\()) ')    
    print (Fore.YELLOW    + ' (((_) ((_)\  /(_))/(_))/(_))   (((_)  /(_))((_)\  /(_))( )(_))((_)\ ')
    print (Fore.YELLOW    + ') )\___  _((_)(_)) (_)) (_))     )\___ (_))  __ ((_)(_)) (_(_()) ((_) ')
    print (Fore.YELLOW    + ')((/ __|| || || _ \|_ _|/ __|   ((/ __|| _ \ \ \ / /| _ \|_   _| / _ \ ')
    print (Fore.BLUE      + ' )| (__ | __ ||   / | | \__ \    | (__ |   /  \ V / |  _/  | |  | (_) |')
    print (Fore.BLUE      + '  \____||_||_||_|_\|___||___/     \___||_|_\   |_|  |_|    |_|   \___/ \n' + Fore.RESET)
    print (Fore.BLUE   + '    BY :CHRIS CRYPTO GAMING \n' + Fore.RESET)
    print (Fore.BLUE   + '    YT Channel : http://bit.ly/CCGYTC  \n' + Fore.RESET)       

    print (Fore.YELLOW + """******************************** MENU ********************************""" + Fore.RESET)
    print (Fore.GREEN + "1. BTC - Visit Sites" + Fore.RESET) 
    print (Fore.GREEN + "2. BTC - Message Bots" + Fore.RESET) 
    print (Fore.GREEN + "3. BTC - Join Channels" + Fore.RESET) 
    print (Fore.GREEN + "4. BTC All 3 - (Visit Sites, Message Bot, Join Channels)" + Fore.RESET)
    print (Fore.GREEN + "5. BTC All 3 - (Visit Sites, Message Bot, Join Channels) + Withdrawal" + Fore.RESET)
    print (Fore.GREEN + "6. BTC - Withdrawal Only" + Fore.RESET)
    print (Fore.RED   + "7. Exit" + Fore.RESET)
    print (Fore.YELLOW + """**********************************************************************""")

def LTC_Menu():
  print (Fore.YELLOW  + """********** Welcome to Chris Crypto LTC Clickbot Scripts ***************""" + Fore.RESET)
  print (Fore.RED       + '       )  (    (    (        (    )  (         ) ')     
  print (Fore.RED       + ' (    ( /(  )\ ) )\ ) )\ )      (    )\ )  ( /(  )\ )  *   )  ( /( ')       
  print (Fore.RED       + '  )\   )\())(()/((()/((()/(      )\  (()/(  )\())(()/(` )  /(  )\()) ')    
  print (Fore.YELLOW    + ' (((_) ((_)\  /(_))/(_))/(_))   (((_)  /(_))((_)\  /(_))( )(_))((_)\ ')
  print (Fore.YELLOW    + ') )\___  _((_)(_)) (_)) (_))     )\___ (_))  __ ((_)(_)) (_(_()) ((_) ')
  print (Fore.YELLOW    + ')((/ __|| || || _ \|_ _|/ __|   ((/ __|| _ \ \ \ / /| _ \|_   _| / _ \ ')
  print (Fore.BLUE      + ' )| (__ | __ ||   / | | \__ \    | (__ |   /  \ V / |  _/  | |  | (_) |')
  print (Fore.BLUE      + '  \____||_||_||_|_\|___||___/     \___||_|_\   |_|  |_|    |_|   \___/ \n' + Fore.RESET)
  print (Fore.BLUE   + '    BY :CHRIS CRYPTO GAMING \n' + Fore.RESET)
  print (Fore.BLUE   + '    YT Channel : http://bit.ly/CCGYTC  \n' + Fore.RESET)       

  print (Fore.YELLOW + """******************************** MENU ********************************""" + Fore.RESET)
  print (Fore.GREEN + "1. LTC - Visit Sites" + Fore.RESET) 
  print (Fore.GREEN + "2. LTC - Message Bots" + Fore.RESET) 
  print (Fore.GREEN + "3. LTC - Join Channels" + Fore.RESET) 
  print (Fore.GREEN + "4. LTC All 3 - (Visit Sites, Message Bot, Join Channels)" + Fore.RESET)
  print (Fore.GREEN + "5. LTC All 3 - (Visit Sites, Message Bot, Join Channels) + Withdrawal" + Fore.RESET)
  print (Fore.GREEN + "6. LTC - Withdrawal Only" + Fore.RESET)
  print (Fore.RED   + "7. Exit" + Fore.RESET)
  print (Fore.YELLOW + """**********************************************************************""")

def ZEC_Menu():
  print (Fore.YELLOW  + """********** Welcome to Chris Crypto ZEC Clickbot Scripts ***************""" + Fore.RESET)
  print (Fore.RED       + '       )  (    (    (        (    )  (         ) ')     
  print (Fore.RED       + ' (    ( /(  )\ ) )\ ) )\ )      (    )\ )  ( /(  )\ )  *   )  ( /( ')       
  print (Fore.RED       + '  )\   )\())(()/((()/((()/(      )\  (()/(  )\())(()/(` )  /(  )\()) ')    
  print (Fore.YELLOW    + ' (((_) ((_)\  /(_))/(_))/(_))   (((_)  /(_))((_)\  /(_))( )(_))((_)\ ')
  print (Fore.YELLOW    + ') )\___  _((_)(_)) (_)) (_))     )\___ (_))  __ ((_)(_)) (_(_()) ((_) ')
  print (Fore.YELLOW    + ')((/ __|| || || _ \|_ _|/ __|   ((/ __|| _ \ \ \ / /| _ \|_   _| / _ \ ')
  print (Fore.BLUE      + ' )| (__ | __ ||   / | | \__ \    | (__ |   /  \ V / |  _/  | |  | (_) |')
  print (Fore.BLUE      + '  \____||_||_||_|_\|___||___/     \___||_|_\   |_|  |_|    |_|   \___/ \n' + Fore.RESET)
  print (Fore.BLUE   + '    BY :CHRIS CRYPTO GAMING \n' + Fore.RESET)
  print (Fore.BLUE   + '    YT Channel : http://bit.ly/CCGYTC  \n' + Fore.RESET)       

  print (Fore.YELLOW + """******************************** MENU ********************************""" + Fore.RESET)
  print (Fore.GREEN + "1. ZEC - Visit Sites" + Fore.RESET) 
  print (Fore.GREEN + "2. ZEC - Message Bots" + Fore.RESET) 
  print (Fore.GREEN + "3. ZEC - Join Channels" + Fore.RESET) 
  print (Fore.GREEN + "4. ZEC All 3 - (Visit Sites, Message Bot, Join Channels)" + Fore.RESET)
  print (Fore.GREEN + "5. ZEC All 3 - (Visit Sites, Message Bot, Join Channels) + Withdrawal" + Fore.RESET)
  print (Fore.GREEN + "6. ZEC - Withdrawal Only" + Fore.RESET)
  print (Fore.RED   + "7. Exit" + Fore.RESET)
  print (Fore.YELLOW + """**********************************************************************""")

def BCH_Menu():
  print (Fore.YELLOW  + """********** Welcome to Chris Crypto BCH Clickbot Scripts ***************""" + Fore.RESET)
  print (Fore.RED       + '       )  (    (    (        (    )  (         ) ')     
  print (Fore.RED       + ' (    ( /(  )\ ) )\ ) )\ )      (    )\ )  ( /(  )\ )  *   )  ( /( ')       
  print (Fore.RED       + '  )\   )\())(()/((()/((()/(      )\  (()/(  )\())(()/(` )  /(  )\()) ')    
  print (Fore.YELLOW    + ' (((_) ((_)\  /(_))/(_))/(_))   (((_)  /(_))((_)\  /(_))( )(_))((_)\ ')
  print (Fore.YELLOW    + ') )\___  _((_)(_)) (_)) (_))     )\___ (_))  __ ((_)(_)) (_(_()) ((_) ')
  print (Fore.YELLOW    + ')((/ __|| || || _ \|_ _|/ __|   ((/ __|| _ \ \ \ / /| _ \|_   _| / _ \ ')
  print (Fore.BLUE      + ' )| (__ | __ ||   / | | \__ \    | (__ |   /  \ V / |  _/  | |  | (_) |')
  print (Fore.BLUE      + '  \____||_||_||_|_\|___||___/     \___||_|_\   |_|  |_|    |_|   \___/ \n' + Fore.RESET)
  print (Fore.BLUE   + '    BY :CHRIS CRYPTO GAMING \n' + Fore.RESET)
  print (Fore.BLUE   + '    YT Channel : http://bit.ly/CCGYTC  \n' + Fore.RESET)       

  print (Fore.YELLOW + """******************************** MENU ********************************""" + Fore.RESET)
  print (Fore.GREEN + "1. BCH - Visit Sites" + Fore.RESET) 
  print (Fore.GREEN + "2. BCH - Message Bots" + Fore.RESET) 
  print (Fore.GREEN + "3. BCH - Join Channels" + Fore.RESET) 
  print (Fore.GREEN + "4. BCH All 3 - (Visit Sites, Message Bot, Join Channels)" + Fore.RESET)
  print (Fore.GREEN + "5. BCH All 3 - (Visit Sites, Message Bot, Join Channels) + Withdrawal" + Fore.RESET)
  print (Fore.GREEN + "6. BCH - Withdrawal Only" + Fore.RESET)
  print (Fore.RED   + "7. Exit" + Fore.RESET)
  print (Fore.YELLOW + """**********************************************************************""")

def MSTR_Menu():
  print (Fore.YELLOW  + """********** Welcome to Chris Crypto BCH Clickbot Scripts ***************""" + Fore.RESET)
  print (Fore.RED       + '       )  (    (    (        (    )  (         ) ')     
  print (Fore.RED       + ' (    ( /(  )\ ) )\ ) )\ )      (    )\ )  ( /(  )\ )  *   )  ( /( ')       
  print (Fore.RED       + '  )\   )\())(()/((()/((()/(      )\  (()/(  )\())(()/(` )  /(  )\()) ')    
  print (Fore.YELLOW    + ' (((_) ((_)\  /(_))/(_))/(_))   (((_)  /(_))((_)\  /(_))( )(_))((_)\ ')
  print (Fore.YELLOW    + ') )\___  _((_)(_)) (_)) (_))     )\___ (_))  __ ((_)(_)) (_(_()) ((_) ')
  print (Fore.YELLOW    + ')((/ __|| || || _ \|_ _|/ __|   ((/ __|| _ \ \ \ / /| _ \|_   _| / _ \ ')
  print (Fore.BLUE      + ' )| (__ | __ ||   / | | \__ \    | (__ |   /  \ V / |  _/  | |  | (_) |')
  print (Fore.BLUE      + '  \____||_||_||_|_\|___||___/     \___||_|_\   |_|  |_|    |_|   \___/ \n' + Fore.RESET)
  print (Fore.BLUE   + '    BY :CHRIS CRYPTO GAMING \n' + Fore.RESET)
  print (Fore.BLUE   + '    YT Channel : http://bit.ly/CCGYTC  \n' + Fore.RESET)       

  print (Fore.YELLOW + """******************************** MENU ********************************""" + Fore.RESET)
  print (Fore.GREEN + "1. All Clickbots + Withdrawal (LTC > ZEC > DOGE > BCH > BTC Visit, Join, Bot)" + Fore.RESET) 
  print (Fore.GREEN + "2. All Clickbots - Withdrawal Only" + Fore.RESET) 
  print (Fore.GREEN + "3. All Clickbots - Visit Sites Only" + Fore.RESET) 
  print (Fore.GREEN + "4. All Clickbots - Message Bots Only" + Fore.RESET)
  print (Fore.GREEN + "5. All Clickbots - Join Channels Only" + Fore.RESET)
  print (Fore.RED   + "6. Exit" + Fore.RESET)
  print (Fore.YELLOW + """**********************************************************************""")



loop=True       
 
while loop:      ## While loop will keep going until loop = False
	print_menu()    ## Displays menu
	choice = input(Fore.GREEN + "Select Your Script [1-7], press enter : " + Fore.RESET)

# DOGE
	if choice == "1":     
		print (Fore.GREEN + "Doge Script Selected" + Fore.RESET)
		time.sleep (1)
		Doge_Menu()
		time.sleep (0.1)
		doge_choice = input(Fore.GREEN + "Select Your Doge Script [1-7], press enter : " + Fore.RESET)

		if doge_choice == "1":
			print (Fore.GREEN + "\nDoge Visit Sites Selected..." + Fore.RESET)
			time.sleep (2)
			print (Fore.GREEN + "Launching Doge Visit Sites...\n")
			time.sleep (2)
			phn_nm = input(Fore.GREEN + 'Enter your phone number, International format (example: +12223334444) : ' + Fore.RESET)
			print (Fore.GREEN + "Connecting to client... Checking valid phone number... Loading Script..." + Fore.RESET)
			os.system('cd Modules/doge/ && python vdoge.py ' + phn_nm)
	 
		if doge_choice == "2":
			print (Fore.GREEN + "\nDoge Message Bots Selected..." + Fore.RESET)
			time.sleep (2)
			print (Fore.GREEN + "Launching Doge Message Bots...\n")
			time.sleep (2)
			phn_nm = input(Fore.GREEN + 'Enter your phone number, International format (example: +12223334444) : ' + Fore.RESET)
			print (Fore.GREEN + "Connecting to client... Checking valid phone number... Loading Script..." + Fore.RESET)
			os.system('cd Modules/doge/ && python mdoge.py ' + phn_nm)
			
		if doge_choice == "3":
			print (Fore.GREEN + "\nDoge Join Channels Selected..." + Fore.RESET)
			time.sleep (2)
			print (Fore.GREEN + "Launching Doge Join Channels...\n")
			time.sleep (2)
			phn_nm = input(Fore.GREEN + 'Enter your phone number, International format (example: +12223334444) : ' + Fore.RESET)
			print (Fore.GREEN + "Connecting to client... Checking valid phone number... Loading Script..." + Fore.RESET)
			os.system('cd Modules/doge/ && python jdoge.py ' + phn_nm)

		if doge_choice == "4":
			print (Fore.GREEN + "\nDoge Master No Withdrawal Selected..." + Fore.RESET)
			time.sleep (2)
			print (Fore.GREEN + "Launching Doge Master No Withdrawal...\n")
			time.sleep (2)
			phn_nm = input(Fore.GREEN + 'Enter your phone number, International format (example: +12223334444) : ' + Fore.RESET)
			print (Fore.GREEN + "Connecting to client... Checking valid phone number... Loading Script..." + Fore.RESET)
			os.system('cd Modules/ltc/ && python vdoge.py ' + phn_nm + ';python mdoge.py ' + phn_nm + ';python jdoge.py ' + phn_nm)
			
		if doge_choice == "5":
			print (Fore.GREEN + "\nDoge Master + Withdrawal Selected..." + Fore.RESET)
			time.sleep (2)
			print (Fore.GREEN + "Launching Doge Master + Withdrawal...\n")
			time.sleep (2)
			phn_nm = input(Fore.GREEN + 'Enter your phone number, International format (example: +12223334444) : ' + Fore.RESET)
			print (Fore.GREEN + "Connecting to client... Checking valid phone number... Loading Script..." + Fore.RESET)
			os.system('cd Modules/ltc/ && python vdoge.py ' + phn_nm + ';python mdoge.py ' + phn_nm + ';python jdoge.py ' + phn_nm + ';python wddoge.py ' + phn_nm)

		if doge_choice == "6":
			print (Fore.GREEN + "\nDoge Withdrawal Script Selected..." + Fore.RESET)
			time.sleep (2)
			print (Fore.GREEN + "Launching Doge Withdrawal Script...\n")
			time.sleep (2)
			phn_nm = input(Fore.GREEN + 'Enter your phone number, International format (example: +12223334444) : ' + Fore.RESET)
			print (Fore.GREEN + "Connecting to client... Checking valid phone number... Loading Script..." + Fore.RESET)
			os.system('cd Modules/doge/ && python wddoge.py ' + phn_nm)

		if doge_choice == "7":
			print ("Exiting Script...")
			time.sleep (2)
			print ("Goodbye...")
			time.sleep (3)
			exit(1)

# BTC
	elif choice == "2":     
		print (Fore.GREEN + "btc Script Selected" + Fore.RESET)
		time.sleep (1)
		BTC_Menu()
		time.sleep (0.1)
		btc_choice = input(Fore.GREEN + "Select Your btc Script [1-7], press enter : " + Fore.RESET)

		if btc_choice == "1":
			print (Fore.GREEN + "\nBTC Visit Sites Selected..." + Fore.RESET)
			time.sleep (2)
			print (Fore.GREEN + "Launching BTC Visit Sites...\n")
			time.sleep (2)
			phn_nm = input(Fore.GREEN + 'Enter your phone number, International format (example: +12223334444) : ' + Fore.RESET)
			print (Fore.GREEN + "Connecting to client... Checking valid phone number... Loading Script..." + Fore.RESET)
			os.system('cd Modules/btc/ && python vbtc.py ' + phn_nm)
	 
		if btc_choice == "2":
			print (Fore.GREEN + "\nBTC Message Bots Selected..." + Fore.RESET)
			time.sleep (2)
			print (Fore.GREEN + "Launching BTC Message Bots...\n")
			time.sleep (2)
			phn_nm = input(Fore.GREEN + 'Enter your phone number, International format (example: +12223334444) : ' + Fore.RESET)
			print (Fore.GREEN + "Connecting to client... Checking valid phone number... Loading Script..." + Fore.RESET)
			os.system('cd Modules/btc/ && python mbtc.py ' + phn_nm)
			
		if btc_choice == "3":
			print (Fore.GREEN + "\nBTC Join Channels Selected..." + Fore.RESET)
			time.sleep (2)
			print (Fore.GREEN + "Launching BTC Join Channels...\n")
			time.sleep (2)
			phn_nm = input(Fore.GREEN + 'Enter your phone number, International format (example: +12223334444) : ' + Fore.RESET)
			print (Fore.GREEN + "Connecting to client... Checking valid phone number... Loading Script..." + Fore.RESET)
			os.system('cd Modules/btc/ && python jbtc.py ' + phn_nm)

		if btc_choice == "4":
			print (Fore.GREEN + "\nBTC Master No Withdrawal Selected..." + Fore.RESET)
			time.sleep (2)
			print (Fore.GREEN + "Launching BTC Master No Withdrawal...\n")
			time.sleep (2)
			phn_nm = input(Fore.GREEN + 'Enter your phone number, International format (example: +12223334444) : ' + Fore.RESET)
			print (Fore.GREEN + "Connecting to client... Checking valid phone number... Loading Script..." + Fore.RESET)
			os.system('cd Modules/ltc/ && python vbtc.py ' + phn_nm + ';python mbtc.py ' + phn_nm + ';python jbtc.py ' + phn_nm)
			
		if btc_choice == "5":
			print (Fore.GREEN + "\nBTC Master + Withdrawal Selected..." + Fore.RESET)
			time.sleep (2)
			print (Fore.GREEN + "Launching BTC Master + Withdrawal...\n")
			time.sleep (2)
			phn_nm = input(Fore.GREEN + 'Enter your phone number, International format (example: +12223334444) : ' + Fore.RESET)
			print (Fore.GREEN + "Connecting to client... Checking valid phone number... Loading Script..." + Fore.RESET)
			os.system('cd Modules/ltc/ && python vbtc.py ' + phn_nm + ';python mbtc.py ' + phn_nm + ';python jbtc.py ' + phn_nm + ';python btcwd.py ' + phn_nm)

		if btc_choice == "6":
			print (Fore.GREEN + "\nBTC Withdrawal Script Selected..." + Fore.RESET)
			time.sleep (2)
			print (Fore.GREEN + "Launching BTC Withdrawal Script...\n")
			time.sleep (2)
			phn_nm = input(Fore.GREEN + 'Enter your phone number, International format (example: +12223334444) : ' + Fore.RESET)
			print (Fore.GREEN + "Connecting to client... Checking valid phone number... Loading Script..." + Fore.RESET)
			os.system('cd Modules/btc/ && python wdbtc.py ' + phn_nm)

		if btc_choice == "7":
			print ("Exiting Script...")
			time.sleep (2)
			print ("Goodbye...")
			time.sleep (3)
			exit(1)

# LTC    
	elif choice == "3":
		print (Fore.GREEN + "ltc Script Selected" + Fore.RESET)
		time.sleep (1)
		LTC_Menu()
		time.sleep (0.1)
		ltc_choice = input(Fore.GREEN + "Select Your ltc Script [1-7], press enter : " + Fore.RESET)

		if ltc_choice == "1":
			print (Fore.GREEN + "\nLTC Visit Sites Selected..." + Fore.RESET)
			time.sleep (2)
			print (Fore.GREEN + "Launching LTC Visit Sites...\n")
			time.sleep (2)
			phn_nm = input(Fore.GREEN + 'Enter your phone number, International format (example: +12223334444) : ' + Fore.RESET)
			print (Fore.GREEN + "Connecting to client... Checking valid phone number... Loading Script..." + Fore.RESET)
			os.system('cd Modules/ltc/ && python vltc.py ' + phn_nm)
	 
		if ltc_choice == "2":
			print (Fore.GREEN + "\nLTC Message Bots Selected..." + Fore.RESET)
			time.sleep (2)
			print (Fore.GREEN + "Launching LTC Message Bots...\n")
			time.sleep (2)
			phn_nm = input(Fore.GREEN + 'Enter your phone number, International format (example: +12223334444) : ' + Fore.RESET)
			print (Fore.GREEN + "Connecting to client... Checking valid phone number... Loading Script..." + Fore.RESET)
			os.system('cd Modules/ltc/ && python mltc.py ' + phn_nm)
			
		if ltc_choice == "3":
			print (Fore.GREEN + "\nLTC Join Channels Selected..." + Fore.RESET)
			time.sleep (2)
			print (Fore.GREEN + "Launching LTC Join Channels...\n")
			time.sleep (2)
			phn_nm = input(Fore.GREEN + 'Enter your phone number, International format (example: +12223334444) : ' + Fore.RESET)
			print (Fore.GREEN + "Connecting to client... Checking valid phone number... Loading Script..." + Fore.RESET)
			os.system('cd Modules/ltc/ && python jltc.py ' + phn_nm)

		if ltc_choice == "4":
			print (Fore.GREEN + "\nLTC Visit Sites Selected..." + Fore.RESET)
			time.sleep (2)
			print (Fore.GREEN + "Launching LTC Visit Sites...\n")
			time.sleep (2)
			phn_nm = input(Fore.GREEN + 'Enter your phone number, International format (example: +12223334444) : ' + Fore.RESET)
			print (Fore.GREEN + "Connecting to client... Checking valid phone number... Loading Script..." + Fore.RESET)
			os.system('cd Modules/ltc/ && python vltc.py ' + phn_nm + ';python mltc.py ' + phn_nm + ';python jltc.py ' + phn_nm)
			
		if ltc_choice == "5":
			print (Fore.GREEN + "\nLTC Master + Withdrawal Selected..." + Fore.RESET)
			time.sleep (2)
			print (Fore.GREEN + "Launching LTC Master + Withdrawal...\n")
			time.sleep (2)
			phn_nm = input(Fore.GREEN + 'Enter your phone number, International format (example: +12223334444) : ' + Fore.RESET)
			print (Fore.GREEN + "Connecting to client... Checking valid phone number... Loading Script..." + Fore.RESET)
			os.system('cd Modules/ltc/ && python vltc.py ' + phn_nm + ';python mltc.py ' + phn_nm + ';python jltc.py ' + phn_nm + ';python wdltc.py' + phn_num)

		if ltc_choice == "6":
			print (Fore.GREEN + "\nLTC Withdrawal Script Selected..." + Fore.RESET)
			time.sleep (2)
			print (Fore.GREEN + "Launching LTC Withdrawal Script...\n")
			time.sleep (2)
			phn_nm = input(Fore.GREEN + 'Enter your phone number, International format (example: +12223334444) : ' + Fore.RESET)
			print (Fore.GREEN + "Connecting to client... Checking valid phone number... Loading Script..." + Fore.RESET)
			os.system('cd Modules/ltc/ && python wdltc.py' + phn_nm)

		if ltc_choice == "7":
			print ("Exiting Script...")
			time.sleep (2)
			print ("Goodbye...")
			time.sleep (3)
			exit(1)

# ZEC
	elif choice == "4":    
		print (Fore.GREEN + "zec Script Selected" + Fore.RESET)
		time.sleep (1)
		ZEC_Menu()
		time.sleep (0.1)
		zec_choice = input(Fore.GREEN + "Select Your zec Script [1-7], press enter : " + Fore.RESET)

		if zec_choice == "1":
			print (Fore.GREEN + "\nZEC Visit Sites Selected..." + Fore.RESET)
			time.sleep (2)
			print (Fore.GREEN + "Launching ZEC Visit Sites...\n")
			time.sleep (2)
			phn_nm = input(Fore.GREEN + 'Enter your phone number, International format (example: +12223334444) : ' + Fore.RESET)
			print (Fore.GREEN + "Connecting to client... Checking valid phone number... Loading Script..." + Fore.RESET)
			os.system('cd Modules/zec/ && python vzec.py ' + phn_nm)
	 
		if zec_choice == "2":
			print (Fore.GREEN + "\nZEC Message Bots Selected..." + Fore.RESET)
			time.sleep (2)
			print (Fore.GREEN + "Launching ZEC Message Bots...\n")
			time.sleep (2)
			phn_nm = input(Fore.GREEN + 'Enter your phone number, International format (example: +12223334444) : ' + Fore.RESET)
			print (Fore.GREEN + "Connecting to client... Checking valid phone number... Loading Script..." + Fore.RESET)
			os.system('cd Modules/zec/ && python mzec.py ' + phn_nm)
			
		if zec_choice == "3":
			print (Fore.GREEN + "\nZEC Join Channels Selected..." + Fore.RESET)
			time.sleep (2)
			print (Fore.GREEN + "Launching ZEC Join Channels...\n")
			time.sleep (2)
			phn_nm = input(Fore.GREEN + 'Enter your phone number, International format (example: +12223334444) : ' + Fore.RESET)
			print (Fore.GREEN + "Connecting to client... Checking valid phone number... Loading Script..." + Fore.RESET)
			os.system('cd Modules/zec/ && python jzec.py ' + phn_nm)

		if zec_choice == "4":
			print (Fore.GREEN + "\nZEC Master No Withdrawal Selected..." + Fore.RESET)
			time.sleep (2)
			print (Fore.GREEN + "Launching ZEC Master No Withdrawal...\n")
			time.sleep (2)
			phn_nm = input(Fore.GREEN + 'Enter your phone number, International format (example: +12223334444) : ' + Fore.RESET)
			print (Fore.GREEN + "Connecting to client... Checking valid phone number... Loading Script..." + Fore.RESET)
			os.system('cd Modules/zec/ && python zec.py ' + phn_nm)
			
		if zec_choice == "5":
			print (Fore.GREEN + "\nZEC Master + Withdrawal Selected..." + Fore.RESET)
			time.sleep (2)
			print (Fore.GREEN + "Launching ZEC Master + Withdrawal...\n")
			time.sleep (2)
			phn_nm = input(Fore.GREEN + 'Enter your phone number, International format (example: +12223334444) : ' + Fore.RESET)
			print (Fore.GREEN + "Connecting to client... Checking valid phone number... Loading Script..." + Fore.RESET)
			os.system('cd Modules/zec/ && python vzec.py ' + phn_nm + ';python mzec.py ' + phn_nm + ';python jzec.py ' + phn_nm)

		if zec_choice == "6":
			print (Fore.GREEN + "\nZEC Withdrawal Script Selected..." + Fore.RESET)
			time.sleep (2)
			print (Fore.GREEN + "Launching ZEC Withdrawal Script...\n")
			time.sleep (2)
			phn_nm = input(Fore.GREEN + 'Enter your phone number, International format (example: +12223334444) : ' + Fore.RESET)
			print (Fore.GREEN + "Connecting to client... Checking valid phone number... Loading Script..." + Fore.RESET)
			os.system('cd Modules/zec/ && python vzec.py ' + phn_nm + ';python mzec.py ' + phn_nm + ';python jzec.py ' + phn_nm + ';python wdzec.py ' + phn_nm)

		if zec_choice == "7":
			print ("Exiting Script...")
			time.sleep (2)
			print ("Goodbye...")
			time.sleep (3)
			exit(1)

# BCH    
	elif choice == "5":
		print (Fore.GREEN + "bch Script Selected" + Fore.RESET)
		time.sleep (1)
		BCH_Menu()
		time.sleep (0.1)
		bch_choice = input(Fore.GREEN + "Select Your bch Script [1-7], press enter : " + Fore.RESET)

		if bch_choice == "1":
			print (Fore.GREEN + "\nBCH Visit Sites Selected..." + Fore.RESET)
			time.sleep (2)
			print (Fore.GREEN + "Launching BCH Visit Sites...\n")
			time.sleep (2)
			phn_nm = input(Fore.GREEN + 'Enter your phone number, International format (example: +12223334444) : ' + Fore.RESET)
			print (Fore.GREEN + "Connecting to client... Checking valid phone number... Loading Script..." + Fore.RESET)
			os.system('cd Modules/bch/ && python vbch.py ' + phn_nm)
	 
		if bch_choice == "2":
			print (Fore.GREEN + "\nBCH Message Bots Selected..." + Fore.RESET)
			time.sleep (2)
			print (Fore.GREEN + "Launching BCH Message Bots...\n")
			time.sleep (2)
			phn_nm = input(Fore.GREEN + 'Enter your phone number, International format (example: +12223334444) : ' + Fore.RESET)
			print (Fore.GREEN + "Connecting to client... Checking valid phone number... Loading Script..." + Fore.RESET)
			os.system('cd Modules/bch/ && python mbch.py ' + phn_nm)
			
		if bch_choice == "3":
			print (Fore.GREEN + "\nBCH Join Channels Selected..." + Fore.RESET)
			time.sleep (2)
			print (Fore.GREEN + "Launching BCH Join Channels...\n")
			time.sleep (2)
			phn_nm = input(Fore.GREEN + 'Enter your phone number, International format (example: +12223334444) : ' + Fore.RESET)
			print (Fore.GREEN + "Connecting to client... Checking valid phone number... Loading Script..." + Fore.RESET)
			os.system('cd Modules/bch/ && python jbch.py ' + phn_nm)

		if bch_choice == "4":
			print (Fore.GREEN + "\nBCH Master No Withdrawal Selected..." + Fore.RESET)
			time.sleep (2)
			print (Fore.GREEN + "Launching BCH Master No Withdrawal...\n")
			time.sleep (2)
			phn_nm = input(Fore.GREEN + 'Enter your phone number, International format (example: +12223334444) : ' + Fore.RESET)
			print (Fore.GREEN + "Connecting to client... Checking valid phone number... Loading Script..." + Fore.RESET)
			os.system('cd Modules/bch/ && python vbch.py ' + phn_nm + ';python mbch.py ' + phn_nm + ';python jbch.py ' + phn_nm)
			
		if bch_choice == "5":
			print (Fore.GREEN + "\nBCH Master + Withdrawal Selected..." + Fore.RESET)
			time.sleep (2)
			print (Fore.GREEN + "Launching BCH Master + Withdrawal...\n")
			time.sleep (2)
			phn_nm = input(Fore.GREEN + 'Enter your phone number, International format (example: +12223334444) : ' + Fore.RESET)
			print (Fore.GREEN + "Connecting to client... Checking valid phone number... Loading Script..." + Fore.RESET)
			os.system('cd Modules/bch/ && python vbch.py ' + phn_nm + ';python mbch.py ' + phn_nm + ';python jbch.py ' + phn_nm + ';python wdbch.py ' + phn_nm)

		if bch_choice == "6":
			print (Fore.GREEN + "\nBCH Withdrawal Script Selected..." + Fore.RESET)
			time.sleep (2)
			print (Fore.GREEN + "Launching BCH Withdrawal Script...\n")
			time.sleep (2)
			phn_nm = input(Fore.GREEN + 'Enter your phone number, International format (example: +12223334444) : ' + Fore.RESET)
			print (Fore.GREEN + "Connecting to client... Checking valid phone number... Loading Script..." + Fore.RESET)
			os.system('cd Modules/bch/ && python wdbch.py ' + phn_nm)

		if bch_choice == "7":
			print ("Exiting Script...")
			time.sleep (2)
			print ("Goodbye...")
			time.sleep (3)
			exit(1)
# MSTR    
	elif choice == "5":
		print (Fore.GREEN + "Master Script Selected" + Fore.RESET)
		time.sleep (1)
		MSTR_Menu()
		time.sleep (0.1)
		bch_choice = input(Fore.GREEN + "Select Your bch Script [1-7], press enter : " + Fore.RESET)

		if bch_choice == "1":
			print (Fore.GREEN + "\nMaster All Clickbots + Withdrawal Selected..." + Fore.RESET)
			time.sleep (2)
			print (Fore.GREEN + "Launching All Clickbots Master...\n")
			time.sleep (2)
			phn_nm = input(Fore.GREEN + 'Enter your phone number, International format (example: +12223334444) : ' + Fore.RESET)
			print (Fore.GREEN + "Connecting to client... Checking valid phone number... Loading Script..." + Fore.RESET)
			os.system('cd Modules/master/ && python vltc.py ' + phn_nm + ';python mltc.py ' + phn_nm + ';python jltc.py ' + phn_nm + ';python vzec.py ' + phn_nm + ';python mzec.py ' + phn_nm + ';python jzec.py ' + phn_nm + ';python vdoge.py ' + phn_nm + ';python mdoge.py ' + phn_nm + ';python jdoge.py ' + phn_nm + ';python vbch.py ' + phn_nm + ';python mbch.py ' + phn_nm + ';python jbch.py ' + phn_nm + ';python vbtc.py ' + phn_nm + ';python mbtc.py ' + phn_nm + ';python jbtc.py ' + phn_nm + ';python wdltc.py ' + phn_nm + ';python wdzec.py ' + phn_nm + ';python wddoge.py ' + phn_nm + ';python wdbch.py ' + phn_nm + ';python wdbtc.py ' + phn_nm)
	 
		if bch_choice == "2":
			print (Fore.GREEN + "\nMaster All Clickbots Withdrawal Selected..." + Fore.RESET)
			time.sleep (2)
			print (Fore.GREEN + "Launching All Clickbots Withdrawal Master...\n")
			time.sleep (2)
			phn_nm = input(Fore.GREEN + 'Enter your phone number, International format (example: +12223334444) : ' + Fore.RESET)
			print (Fore.GREEN + "Connecting to client... Checking valid phone number... Loading Script..." + Fore.RESET)
			os.system('cd Modules/master/ && python wdltc.py ' + phn_nm + ';python wdzec.py ' + phn_nm + ';python wddoge.py ' + phn_nm + ';python wdbch.py ' + phn_nm + ';python wdbtc.py ' + phn_nm)
			
		if bch_choice == "3":
			print (Fore.GREEN + "\nMaster All Clickbots Visit Sites Selected..." + Fore.RESET)
			time.sleep (2)
			print (Fore.GREEN + "Launching All Clickbots Visit Sites Master...\n")
			time.sleep (2)
			phn_nm = input(Fore.GREEN + 'Enter your phone number, International format (example: +12223334444) : ' + Fore.RESET)
			print (Fore.GREEN + "Connecting to client... Checking valid phone number... Loading Script..." + Fore.RESET)
			os.system('cd Modules/master/ && python vltc.py ' + phn_nm + ';python vzec.py ' + phn_nm + ';python vdoge.py ' + phn_nm + ';python vbch.py ' + phn_nm + ';python vbtc.py ' + phn_nm)

		if bch_choice == "4":
			print (Fore.GREEN + "\nMaster All Clickbots Message Bots Selected..." + Fore.RESET)
			time.sleep (2)
			print (Fore.GREEN + "Launching All Clickbots Message Bots Master...\n")
			time.sleep (2)
			phn_nm = input(Fore.GREEN + 'Enter your phone number, International format (example: +12223334444) : ' + Fore.RESET)
			print (Fore.GREEN + "Connecting to client... Checking valid phone number... Loading Script..." + Fore.RESET)
			os.system('cd Modules/master/ && python mltc.py ' + phn_nm + ';python mzec.py ' + phn_nm + ';python mdoge.py ' + phn_nm + ';python mbch.py ' + phn_nm + ';python mbtc.py ' + phn_nm)
			
		if bch_choice == "5":
			print (Fore.GREEN + "\nMaster All Clickbots Join Channels Selected..." + Fore.RESET)
			time.sleep (2)
			print (Fore.GREEN + "Launching All Clickbots Join Channels Master...\n")
			time.sleep (2)
			phn_nm = input(Fore.GREEN + 'Enter your phone number, International format (example: +12223334444) : ' + Fore.RESET)
			print (Fore.GREEN + "Connecting to client... Checking valid phone number... Loading Script..." + Fore.RESET)
			os.system('cd Modules/master/ && python jltc.py ' + phn_nm + ';python jzec.py ' + phn_nm + ';python jdoge.py ' + phn_nm + ';python jbch.py ' + phn_nm + ';python jbtc.py ' + phn_nm)

		if bch_choice == "6":
			print ("Exiting Script...")
			time.sleep (2)
			print ("Goodbye...")
			time.sleep (3)
			exit(1)

		if bch_choice == "7":
			print ("Exiting Script...")
			time.sleep (2)
			print ("Goodbye...")
			time.sleep (3)
			exit(1)

# Exit
	elif choice == "6":
		print ("************************* You Quit :( ***********************)")
		time.sleep (2.8)
		loop = False # This will make the while loop to end as no value of loop is set to False

	# Exit
	elif choice == "7":
		print ("************************* You Quit :( ***********************)")
		time.sleep (2.8)
		loop = False # This will make the while loop to end as no value of loop is set to False

	# Wrong Entry
	else:
		# Any integer inputs other than values 1-7 will print an error message
		print("Wrong Input... Press any key to continue...")


	### End


		