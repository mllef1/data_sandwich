#! /usr/bin/env python3


import requests
import threading
import time
import random
from bs4 import BeautifulSoup

max_threads = 10 #
amm = 0

words = list(open('words.txt'))
tlds = list(open("tlds.txt", "r"))

def doshit(site, tld):
    try:

        req = requests.get(f"https://{site}{tld}", timeout=20)

        #get title
        html = req.text.lower()
        start_index = html.find("<title>")
        end_index = html.find("</title>")

        if start_index != -1 and end_index != -1 and end_index > start_index: #validate if title exists
            title = req.text[start_index + len("<title>"):end_index].strip()

        else:
            title = " " #no title



        if req.status_code == 200: #only response code 200
            if ("$" in html or "lander" in html) or ("cleanpeppermintblack" in html or "sale" in html):

                #uncomment the bottom line if you wish to see selling domains
                #print(f"\033[0;34mhttps://{site}{tld} [{title}]\033[0m                                 ")
                pass #ignore all selling sites

            else:
                print(f"\033[92mhttps://{site}{tld} [{title}]\033[0m                                   ")

    except:
        pass
words = list(open('words.txt'))
tlds = list(open("tlds.txt", "r"))
while True:
    while threading.active_count() >= max_threads: #limit thread amount
        time.sleep(1)
    site=random.choice(words)
    site = site.strip() #no whitespace
    tld=random.choice(tlds)
    tld = tld.strip() #no whitespace

    amm+=1
    thread = threading.Thread(target=doshit, args=(site, tld))
    thread.start()
    print(f"requests sent: {amm}. threads: {str(threading.active_count())}/{str(max_threads)} current: {site}{tld}                 ", end="\r")
    time.sleep(0.02)
