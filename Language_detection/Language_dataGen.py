import requests
from bs4 import BeautifulSoup
import csv
import urllib.request
import pandas as pd
from csv import writer
import re
import os
import time

codes_raw = []
urls_storage = []
text_data = []
final_data = []

print("Codes downloading...")
n = 6
m = 8
while n <= m:
    print("n = ", n)
    try:
        time.sleep(20)
        link = "https://stackoverflow.com/questions/tagged/groovy?tab=votes&page=" + \
            str(n)+"&pagesize=50"
        print(link)
        urllib.request.urlopen(link).getcode() == 200
        reqs = requests.get(link).text
        time.sleep(35)
        soup = BeautifulSoup(reqs, 'lxml')
        # art =
        for s in soup.find_all('div', class_='summary'):
            l = s.find('h3')
            li = l.find('a', href=True)
            # print(li)
            if li not in urls_storage:
                urls_storage.append(li.get('href'))

        new_url_storage = []
        for url in urls_storage:
            if 'https' not in url:
                new_url_storage.append("https://stackoverflow.com"+url)
            else:
                new_url_storage.append(url)

        for e in new_url_storage:
            print(e)

        for h in new_url_storage:
            source = requests.get(h).text
            soup1 = BeautifulSoup(source, 'lxml')
            if(soup1.find_all('pre')):
                for art1 in soup1.find_all('pre'):
                    for t in art1.find_all('code'):
                        codes_raw.append(t.text)

        print(len(codes_raw))
        print(len(urls_storage))

        urls_storage = []
        new_url_storage = []
        n = n+1

    except:
        print("error")

fields = ["code"]
with open('/home/vanitha-latitudee5520/Mining_pastebin/Supervised/Large_data/Groovy2.csv', 'w') as f:
    # using csv.writer method from CSV package
    write = csv.writer(f)
    write.writerow(fields)
    for val in codes_raw:
        write.writerow([val])

# https://stackoverflow.com/questions/tagged/pascal?tab=newest&page=5&pagesize=15
# https://stackoverflow.com/questions/tagged/pascal?tab=newest&page=5&pagesize=15
