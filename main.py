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
messages = ['i agree', 'true', 'real', 'fax dude', 'yeah', 'exactly', 'true af', 'definitely', 'definitely true', 'fax', 'indeed', 'for sure', 'totally', 'could be', 'maybe', 'i disagree', 'probably', 'probably not', 'idk', 'cool', 'not true', 'incorrect', 'definitely not', 'nah', 'wrong', 'lol', 'okay', 'ok', 'k', 'bruh', 'unreal', 'nope', 'fs', 'fs bro', 'feels good being 6 figs', 'who tryna go b4b', 'b4b?', 'f4f?', 'ugly asl', 'nigga what', 'nigga', 'brother', 'we doin the opps so bad ts so sad i promise it ain even funny', 'when you see me dont blink or stare', 'muwop got head tapped n he had to shave his hair', 'im bored', 'im bored asl', 'tired', 'im sleepy', 'tired asf', 'horny asl', 'horny', 'clown', 'yo what', 'ignored', 'test', 'finna smoke', 'finna flame sum sh up', 'high asl', 'who got roblox?', 'who got bo6?', 'who got brawl?', 'eating', 'eating some mc donalds rn', 'my house cost 7 figs', 'big 2025', 'no', 'ikr']
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
    wait_time = random.randint(5, 10)

    message = random.choice(messages)
    json_data = {
        'content': message
    }
    r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=json_data)
    print(f'{Fore.RESET}[@{Fore.YELLOW}KYAUTO{Fore.RESET}] [Waiting {Fore.RED}{str(wait_time)} seconds...{Fore.RESET}] {Fore.GREEN}Sent message {Fore.RESET}> {Fore.MAGENTA}{message}{Fore.RESET}')
    keep_alive()
    time.sleep(wait_time)
