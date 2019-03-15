#!/usr/bin/env python3

"""
    Dependencies:
    
    Chrome
    Chromedriver
    python-selenium

"""
import glob
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x800')
browser = webdriver.Chrome(options=options)

# https://stackoverflow.com/a/3277516
with open("list.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
print(len(content))

archived = [a[:-4].split('\\')[1] for a in glob.glob('archived/*.png')]
print(archived[:3])

# https://stackoverflow.com/a/7406369
keepcharacters = (' ', '.', '_', "-")
savestring = lambda line: "".join(c for c in line.replace("/", "_") if c.isalnum() or c in keepcharacters).rstrip()

if (not os.path.exists("./archived/")):
    os.makedirs("./archived/")

c = 0
t1 = time.time()
for i, line in enumerate(content):
    try:
        if (line != "" and not str(line).startswith("#")):
            if savestring(line) in archived:
                continue
            print("(" + str(i + 1) + "/" + str(len(content)) + ") " + str(line), flush=True)
            print("loading...", flush=True, end="")
            browser.get(line)
            print("done", flush=True)
            print("calculating size...", flush=True, end="")
            h = browser.execute_script("return Math.max(document.body.scrollHeight, document.body.offsetHeight );")
            if (h == 0):
                print("\nError getting page length\n")
                continue
            browser.set_window_size(width=1920, height=h)
            print("done", flush=True)
            print("shooting...", flush=True, end="")
            f = savestring(line)
            browser.get_screenshot_as_file("./archived/" + str(f) + ".png")
            print("done\n", flush=True)
            browser.set_window_size(width=1920, height=800)
            c += 1
        else:
            print("(" + str(i + 1) + "/" + str(len(content)) + ") skipping\n")
    except Exception as e:
        print(e)
t2 = time.time()
t = t2 - t1
if (c > 0):
    print("saved", c, "items in", round(t, 2), "seconds (" + str(round(t / c, 2)), "seconds per item)")
browser.quit()
