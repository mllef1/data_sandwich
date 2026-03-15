#! /usr/bin/env python3


import requests
import threading
import time
import random
from bs4 import BeautifulSoup

max_threads = 10
amm = 0

words = list(open('words.txt'))
tlds = list(open("tlds.txt", "r"))

def doshit(site, tld):
    try:
        site = site.strip()
        tld = tld.strip()
        req = requests.get(f"https://{site}{tld}", timeout=20)

        html = req.text.lower()
        start_index = html.find("<title>")
        end_index = html.find("</title>")

        if start_index != -1 and end_index != -1 and end_index > start_index:
            title = req.text[start_index + len("<title>"):end_index].strip()

        else:
            title = " "



        if ("$" in html or "lander" in html) or ("cleanpeppermintblack" in html or "sale" in html):
            print(f"\033[0;34mhttps://{site}{tld} [{title}]\033[0m                   ")
        else:
            print(f"\033[92mhttps://{site}{tld} [{title}]\033[0m                     ")
        
    except:
        pass
words = list(open('words.txt'))
tlds = list(open("tlds.txt", "r"))
while True:
    while threading.active_count() >= max_threads:
        time.sleep(1)
    site=random.choice(words)
    site = site.strip()
    tld=random.choice(tlds)
    tld = tld.strip()
    
    amm+=1
    thread = threading.Thread(target=doshit, args=(site, tld))
    thread.start()
    print(f"requests sent: {amm}. current: {site}{tld}                          ", end="\r")
    time.sleep(0.1)