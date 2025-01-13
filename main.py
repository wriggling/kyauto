import asyncio, time
import requests as r
import os
from keep_alive import keep_alive
import websocket
import colorama
from colorama import Fore, init
import requests
import random
import time

token = os.getenv("token")
channel_id = os.getenv("channel_id")
messages = ['@silent i agree', '@silent true', '@silent real', '@silent fax dude', '@silent yeah', '@silent exactly', '@silent true af', '@silent definitely', '@silent definitely true', '@silent fax', '@silent indeed', '@silent for sure', '@silent totally', '@silent could be', '@silent maybe', '@silent i disagree', '@silent probably', '@silent probably not', '@silent idk', '@silent cool', '@silent not true', '@silent incorrect', '@silent definitely not', '@silent nah', '@silent wrong', '@silent lol', '@silent okay', '@silent ok', '@silent k', '@silent bruh', '@silent unreal', '@silent nope', '@silent fs', '@silent fs bro', '@silent feels good being 6 figs', '@silent who tryna go b4b', '@silent b4b?', '@silent f4f?', '@silent ugly asl', '@silent nigga what', '@silent nigga', '@silent brother', '@silent we doin the opps so bad ts so sad i promise it ain even funny', '@silent when you see me dont blink or stare', '@silent muwop got head tapped n he had to shave his hair', '@silent im bored', '@silent im bored asl', '@silent tired', '@silent im sleepy', '@silent tired asf', '@silent horny asl', '@silent horny', '@silent clown', '@silent yo what', '@silent ignored', '@silent test', '@silent finna smoke', '@silent finna flame sum sh up', '@silent high asl', '@silent who got roblox?', '@silent who got bo6?', '@silent who got brawl?', '@silent eating', '@silent eating some mc donalds rn', '@silent my house cost 7 figs', '@silent big 2025', '@silent no', '@silent ikr']
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Authorization': token
}

userinfo = requests.get('https://canary.discordapp.com/api/v9/users/@me', headers=headers).json()
username = userinfo["username"]
discriminator = userinfo["discriminator"]
userid = userinfo["id"]

print(f'''
{Fore.RED}╦╔═╦ ╦╔═╗╦ ╦╔╦╗╔═╗
{Fore.RED}╠╩╗╚╦╝╠═╣║ ║ ║ ║ ║
{Fore.RED}╩ ╩ ╩ ╩ ╩╚═╝ ╩ ╚═╝
{Fore.RESET}-----------------------
{Fore.RESET}USER INFO:
{Fore.GREEN}User: @{username}
{Fore.YELLOW}ID: {userid}
{Fore.BLUE}Channel: {channel_id}
''')

while True:
    wait_time = random.randint(10, 20)

    message = random.choice(messages)
    json_data = {
        'content': message
    }
    r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=json_data)
    print(f'{Fore.RESET}[@{Fore.YELLOW}KYAUTO{Fore.RESET}] [Waiting {Fore.RED}{str(wait_time)} seconds...{Fore.RESET}] {Fore.GREEN}Sent message {Fore.RESET}> {Fore.MAGENTA}{message}{Fore.RESET}')
    keep_alive()
    time.sleep(wait_time)
