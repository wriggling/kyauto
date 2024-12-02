import asyncio, time
import requests as r
import os
from keep_alive import keep_alive
import websocket
from colorama import Fore, init
import requests
import random
import time

init()

token = os.getenv("token")
channel_id = os.getenv("channel_id")
messages = ['i agree', 'true', 'real', 'fax dude', 'yeah', 'exactly', 'true af', 'definitely', 'definitely true', 'fax', 'indeed', 'for sure', 'totally', 'could be', 'maybe', 'i disagree', 'probably', 'probably not', 'idk', 'cool', 'not true', 'incorrect', 'definitely not', 'nah', 'wrong', 'lol', 'okay', 'ok', 'k', 'bruh', 'unreal', 'nope', 'no', 'ikr']
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Authorization': token
}

userinfo = requests.get('https://canary.discordapp.com/api/v9/users/@me', headers=headers).json()
username = userinfo["username"]
discriminator = userinfo["discriminator"]
userid = userinfo["id"]

print(f'''
{Fore.CYAN}

╦╔═╦ ╦╔═╗╦ ╦╔╦╗╔═╗
╠╩╗╚╦╝╠═╣║ ║ ║ ║ ║
╩ ╩ ╩ ╩ ╩╚═╝ ╩ ╚═╝{Fore.RESET}
------------------------------
{Fore.GREEN}USER INFO:
Username: @{username}
User ID: {userid} {Fore.RESET}
''')

while True:
    wait_time = random.randint(70, 200)

    message = random.choice(messages)
    json_data = {
        'content': message
    }
    r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=json_data)
    print(f'            {Fore.YELLOW}[%] {Fore.YELLOW}[{r.status_code}] {Fore.LIGHTBLACK_EX}[Waiting {str(wait_time)} seconds or {str(wait_time/60)[0:4]} minutes...] {Fore.RESET} Sent message > {message}')
    time.sleep(wait_time)
keep_alive()
