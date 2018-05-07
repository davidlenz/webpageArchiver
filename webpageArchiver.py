#!/usr/bin/env python3

"""
    Dependencies:
    
    Chrome
    Chromedriver
    python-selenium

""" 
import time, os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x800')
browser = webdriver.Chrome(chrome_options=options)

# https://stackoverflow.com/a/3277516
with open("list.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

c = 0
t1 = time.time()
for i,line in enumerate(content):
    if(line != "" and not str(line).startswith("#")):
        print("("+str(i+1)+"/"+str(len(content))+") "+str(line),flush=True)
        print("loading...",flush=True,end="")
        browser.get(line)
        print("done",flush=True)
        print("calculating size...",flush=True,end="")
        h = browser.execute_script("return Math.max(document.body.scrollHeight, document.body.offsetHeight );")
        browser.set_window_size(width=1920, height=h)
        print("done",flush=True)
        print("shooting...",flush=True,end="")

        # https://stackoverflow.com/a/7406369
        keepcharacters = (' ','.','_',"-")
        f = "".join(c for c in line.replace("/", "_") if c.isalnum() or c in keepcharacters).rstrip()

        if (not os.path.exists("./archived/")):
            os.makedirs("./archived/")
        browser.get_screenshot_as_file("./archived/"+str(f)+".png")
        print("done\n",flush=True)
        browser.set_window_size(width=1920, height=800)
        c += 1
    else:
        print("("+str(i+1)+"/"+str(len(content))+") skipping\n")
t2 = time.time()
t = t2-t1
print("saved",c,"items in",round(t,2),"seconds ("+str(round(t/c,2)),"seconds per item)")
browser.quit()
