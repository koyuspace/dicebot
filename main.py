#!/usr/bin/python3
# -*- coding: utf-8 -*-

from mastodon import Mastodon, StreamListener
from PIL import Image, ImageDraw, ImageFont
from lxml import html
import os
import re
import creds
import datetime
import time
import random
import dicelib

if not os.path.exists("clientcred"):
    Mastodon.create_app(
     "dicebot",
     api_base_url = creds.instance,
     to_file = "clientcred"
    )

mastodon = Mastodon(
    client_id = "clientcred",
    api_base_url = creds.instance
)

mastodon.log_in(
    creds.username,
    creds.password,
    to_file = "usercred"
)

print("dicebot listening...")

class myListener(StreamListener):
    def on_notification(self, notification):
        if notification["type"] == "mention":
            toot = str(html.document_fromstring(notification["status"]["content"]).text_content())
            if "roll" in toot.lower():
                randnum = random.randint(1,6)
                numbers = re.findall(r'\b\d+\b', toot)
                maxnum = numbers[0]
                if numbers:
                    randnum = random.randint(1,maxnum)
                W, H = (527,296)
                im = Image.new("RGBA",(W,H),"#222233ff")
                draw = ImageDraw.Draw(im)
                fontAwesome = ImageFont.truetype("fontawesome.ttf", 72)
                w, h = draw.textsize(text=dicelib.fa(randnum, maxnum), font=fontAwesome)
                x = (W-w)/2
                y = (H-h)/2
                draw.text(xy=(x, y), text=dicelib.fa(randnum, maxnum), fill="#fe53e1", font=fontAwesome)
                im.save("dice.png", "PNG")
                print(notification["account"]["acct"]+" rolled a "+dicelib.words(randnum, maxnum))
                mastodon.status_post("@"+notification["account"]["acct"]+" You rolled a "+dicelib.words(randnum, maxnum)+" "+dicelib.emoji(randnum), in_reply_to_id=notification["status"]["id"], visibility=notification["status"]["visibility"], media_ids=mastodon.media_post("dice.png"))

listener = myListener()
mastodon.stream_user(listener)