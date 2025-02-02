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
messages = ['i agree', 'true', 'real', 'fax dude', 'yeah', 'exactly', 'true af', 'definitely', 'definitely true', 'fax', 'indeed', 'for sure', 'totally', 'could be', 'maybe', 'i disagree', 'probably', 'probably not', 'idk', 'cool', 'not true', 'incorrect', 'definitely not', 'nah', 'wrong', 'lol', 'okay', 'ok', 'k', 'bruh', 'unreal', 'nope', 'fs', 'fs bro', 'feels good being 6 figs', 'who tryna go b4b', 'b4b?', 'f4f?', 'ugly asl', 'nigga what', 'nigga', 'brother', 'we doin the opps so bad ts so sad i promise it ain even funny', 'when you see me dont blink or stare', 'muwop got head tapped n he had to shave his hair', 'im bored', 'im bored asl', 'tired', 'im sleepy', 'tired asf', 'horny asl', 'horny', 'clown', 'yo what', 'ignored', 'test', 'finna smoke', 'finna flame sum sh up', 'high asl', 'who got roblox?', 'who got bo6?', 'who got brawl?', 'eating', 'eating some mc donalds rn', 'my house cost 7 figs', 'big 2025', 'no', 'ikr', 'sunshine lollipops and rainbows', 'show your eth wallet', 'jvc', 'ur a furry', 'yo wassup bro', 'nigga stfu', 'igh bro', 'wtf you talking about', 'yap', 'sing me a song', 'cuminnabun', 'be my cumslut', 'u got 6 fingers', 'wheres your dad?', 'gah dam', 'you look good twin', 'ALL I WANT FOR CHRISTMASSSSS', 'im back', 'nigga what the fuck', 'you do not have a arc', 'you are a loner', 'bro no stop it', 'stop touching me pls', 'oh my god we dont care', 'stupid', 'dickhead', 'idiot', 'clown', 'yappatron', 'stop yapping', 'im here', 'get more active than me son', 'show your btc wallet', 'show your dogecoin', 'get of exodus skid', 'stake loner', 'send me 1k so i can gamble and lose', 'hahahaha', 'LOL', 'XD', 'LMAO', 'LO', 'OL', 'LOOOLOLOOLL','LMAOOOOOOOOO', 'stfu LMAO', 'ah shucks', 'wow', 'loser', 'random', 'what the hell?', 'talking nonsense', 'bruh', 'tryna help me with my jerk off session?', 'how?', 'thats cool', 'show a band', 'pooron', 'trash ass username', 'nigga', 'bro what', 'dude is a health pack', 'hop on fortnite', 'get on roblox', 'bro got sniped', 'you funny asf', 'bros not the mc', 'bro mad', 'cornball', 'smoking rn', 'jerking rn', 'horny rn', 'whos tryna be my good slut', 'im rich', 'ur poor', 'come die', 'i make too much money', 'im a 7 fig warrior', '????', 'stop talking', 'come suck this 7 inch cock', 'harassment', 'im a comboy', 'im too sexy', 'slick', 'hi im kyuu', ':/', ':)', ':(', ';(', '):', '(:', 'c:', ':c', '>:c', 'c:<', '>:(', '(:<', '>;)', '(;<', '>;c', 'c;<', 'UwU', 'T-T', 'money is my life', 'i work a 9-5', 'you sexy?']
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
    wait_time = random.randint(2, 4)

    message = random.choice(messages)
    json_data = {
        'content': message
    }
    r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=json_data)
    print(f'{Fore.RESET}[@{Fore.YELLOW}KYAUTO{Fore.RESET}] [Waiting {Fore.RED}{str(wait_time)} seconds...{Fore.RESET}] {Fore.GREEN}Sent message {Fore.RESET}> {Fore.MAGENTA}{message}{Fore.RESET}')
    keep_alive()
    time.sleep(wait_time)
