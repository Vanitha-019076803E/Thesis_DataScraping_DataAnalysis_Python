import requests
from bs4 import BeautifulSoup
import csv
import urllib.request
import pandas as pd
from csv import writer
import re
import os

pastes_raw = []
urls_storage = []
text_data = []
final_data = []
print("Pastes downloading...")
num = 300
n = 1
while n <= num :
    print("n = ",n)
    try:
        urllib.request.urlopen("https://codepad.co/snippets?sortBy=most-recent&page="+str(n)).getcode() == 200
        reqs = requests.get("https://codepad.co/snippets?sortBy=most-recent&page="+str(n)).text
        soup = BeautifulSoup(reqs, 'lxml')
        art = soup.find('div',class_='list')
        for l in art.find_all('h3'):
            for link in l.find_all('a', href=True): 
                urls_storage.append(link.get('href'))
    
        for url in urls_storage:
            source = requests.get(url).text
            soup1 = BeautifulSoup(source, 'lxml')
            art1 = soup1.find('a',class_='lang')  
            #print(art1)
                #tit = soup1.find('h1')
                #date = soup1.find('li', class_='date')
                #dict = {'paste_title':tit.text, 'paste_date':date.text, 'paste_content': art1.text}
            if art1.text not in pastes_raw:
                pastes_raw.append(art1.text)
        print(len(pastes_raw))
        urls_storage = []
        n = n+1
        
    except:
        print(error)

print(pastes_raw[1])
fields = ['Languages']
with open('/home/vanitha/Mining_pastebin/Supervised/Large_data/Langs.csv', 'w') as f:
    # using csv.writer method from CSV package
    write = csv.writer(f)
    write.writerow(fields)
    for val in pastes_raw:
        write.writerow([val])












        