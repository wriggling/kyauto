import asyncio, time
import requests as r
import os
from keep_alive import keep_alive
import websocket
from colorama import Fore, init
import requests
import random
import time

token = os.getenv("token")
channel_id = os.getenv("channel_id")

async def main():
print(f'Loading....')

messages = ['loser', 'random', 'what the hell?', 'talking nonsense', 'bruh', 'tryna help me with my jerk off session?', 'how?', 'thats cool', 'show a band', 'pooron', 'trash ass username', 'nigga', 'bro what', 'dude is a health pack', 'hop on fortnite', 'get on roblox', 'bro got sniped', 'you funny asf', 'bros not the mc', 'bro mad', 'cornball', 'smoking rn', 'jerking rn', 'horny rn', 'whos tryna be my good slut', 'im rich', 'ur poor', 'come die', 'i make too much money', 'im a 7 fig warrior', '????', 'stop talking', 'come suck this 7 inch cock', 'harassment', 'im a comboy', 'im too sexy', 'slick', 'hi im kyuu', ':/', ':)', ':(', ';(', '):', '(:', 'c:', ':c', '>:c', 'c:<', '>:(', '(:<', '>;)', '(;<', '>;c', 'c;<', 'UwU', 'T-T', 'money is my life', 'i work a 9-5', 'you sexy?', 'i agree', 'true', 'real', 'fax dude', 'yeah', 'exactly', 'true af', 'definitely', 'definitely true', 'fax', 'indeed', 'for sure', 'totally', 'could be', 'maybe', 'i disagree', 'probably', 'probably not', 'idk', 'cool', 'not true', 'incorrect', 'definitely not', 'nah', 'wrong', 'lol', 'okay', 'ok', 'k', 'bruh', 'unreal', 'nope', 'no', 'ikr']
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Authorization': token
}

userinfo = requests.get('https://canary.discordapp.com/api/v9/users/@me', headers=headers).json()
username = userinfo["username"]
discriminator = userinfo["discriminator"]
userid = userinfo["id"]
def run():

print(f'''

{Fore.RED}╦╔═╦ ╦╔═╗╦ ╦╔╦╗╔═╗
{Fore.RED}╠╩╗╚╦╝╠═╣║ ║ ║ ║ ║
{Fore.RED}╩ ╩ ╩ ╩ ╩╚═╝ ╩ ╚═╝{Fore.RESET}
{Fore.BLUE}-------------------------
{Fore.BLUE}USER INFO:
{Fore.BLUE}Username: @{username}
{Fore.BLUE}ID: {userid} {Fore.RESET}
''')
asyncio.run(main())
while True:
    wait_time = random.randint(17, 20)

    message = random.choice(messages)
    json_data = {
        'content': message
    }
    r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=json_data)
    print(f'            {Fore.YELLOW}[%] {Fore.YELLOW}[{r.status_code}] {Fore.GREEN}[Waiting {str(wait_time)} seconds...] {Fore.RESET} Sent message > {message}')
    time.sleep(wait_time)

run()
keep_alive()
