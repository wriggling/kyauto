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
messages = ['i agree', 'true', 'real', 'fax dude', 'yeah', 'exactly', 'true af', 'definitely', 'definitely true', 'fax', 'indeed', 'for sure', 'totally', 'could be', 'maybe', 'i disagree', 'probably', 'probably not', 'idk', 'cool', 'not true', 'incorrect', 'definitely not', 'nah', 'wrong', 'lol', 'okay', 'ok', 'k', 'bruh', 'unreal', 'nope', 'fs', 'fs bro', 'peekaboo', 'bro wtf r you talking about', 'hm', 'ugly asl', 'nigga what', 'nigga', 'brother', 'dang', 'xanax', 'hru?', 'im bored', 'im bored asl', 'tired', 'im sleepy', 'tired asf', 'air', 'clipped', 'clown', 'yo what', 'ignored', 'test', 'continuing on', 'nice', 'oh lol', 'wtf lol', 'jeez', 'thats crazy', 'crazy', 'wild asl', 'wild twin', 'big 2025', 'no', 'ikr', 'wild', 'oh shit', 'jvc', 'ur a furry', 'yo wassup bro', 'nigga stfu', 'igh bro', 'wtf you talking about', 'yap', 'heavy', 'cuminnabun', 'crazy as shit', 'insane', 'insane works', 'gah dam', 'twin', 'cover', 'im back', 'nigga what the fuck', 'goodness', 'loner', 'bro no stop it', 'yap', 'oh my god we dont care', 'stupid', 'dickhead', 'idiot', 'clown', 'yappatron', 'stop yapping', 'goodness', 'alright brother', 'dam brother', 'wsp brother', 'wtf brother', 'dam bro', 'yoooo', 'hahahaha', 'LOL', 'XD', 'LMAO', 'LO', 'OL', 'LOOOLOLOOLL','LMAOOOOOOOOO', 'stfu LMAO', 'ah shucks', 'wow', 'loser', 'random', 'what the hell?', 'talking nonsense', 'bruh', 'LMFAOOOOOO XD', 'ROFL', 'rofl', 'lmao', 'LMFAO', 'ok rofl', 'nigga', 'bro what', 'rofl xd', '🥱', '😶', '😂', '🤣🤣', '💀', '💀💀💀', '💔', '😭😭😭😭', '😭', '😭😭😭💔💔💔💔', '☠️', '☠️☠️', '🫡', '👋👋', 'great', 'thats amazing', '????', 'stop talking', '!?!??????!!?', '??????????????', '🤷‍♂️', '😹😹', 'hilarious brother', 'tip', ':/', ':)', ':(', ';(', '):', '(:', 'c:', ':c', '>:c', 'c:<', '>:(', '(:<', '>;)', '(;<', '>;c', 'c;<', 'UwU', 'T-T', 'yup', 'wow', 'y?']
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
    wait_time = random.randint(15, 20)

    message = random.choice(messages)
    json_data = {
        'content': message
    }
    r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=json_data)
    print(f'{Fore.RESET}[@{Fore.YELLOW}KYAUTO{Fore.RESET}] [Waiting {Fore.RED}{str(wait_time)} seconds...{Fore.RESET}] {Fore.GREEN}Sent message {Fore.RESET}> {Fore.MAGENTA}{message}{Fore.RESET}')
    keep_alive()
    time.sleep(wait_time)
