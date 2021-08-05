import requests
from bs4 import BeautifulSoup
import csv
import urllib.request
import json
import re
from datetime import datetime
import schedule
import time

def codepad_data_extraction():
    pastes = []
    urls_storage = []
    dict = {}
    time_now = datetime.now().strftime("%Y-%m-%d %H-%M")
    for n in range(1, 2):
        try:
            urllib.request.urlopen("https://codepad.co/snippets?sortBy=popular&filterTime=all&page="+str(n)).getcode() == 200
            reqs = requests.get("https://codepad.co/snippets?sortBy=popular&filterTime=all&page="+str(n)).text
            soup = BeautifulSoup(reqs, 'lxml')
            art = soup.find('div',class_='list')
            print("Loading...")
            for l in art.find_all('h3'):
                for link in l.find_all('a', href=True): 
                    urls_storage.append(link.get('href'))
    
            print("Pastes downloading...")
            for url in urls_storage:
                source = requests.get(url).text
                soup1 = BeautifulSoup(source, 'lxml')
                art1 = soup1.find('div',class_='code')
                tit = soup1.find('h1')
                date = soup1.find('li', class_='date')
                dict = {'paste_title':tit.text, 'paste_date':date.text, 'paste_content': art1.text}
                pastes.append(dict)
        
        except:
            print("nothing")

    data = {}
    data['codepad'] = []
    for paste in pastes:
        data['codepad'].append(paste)

    with open('/home/vanitha/scraped/codepad_data_'+time_now+'.json', 'w') as fp:
            json.dump(data, fp)

#codepad_data_extraction()

schedule.every(15).seconds.do(codepad_data_extraction)
#schedule.every().day.at("10.30").do(codepad_data_extraction)
#write_to_JSON_file(path,file_name,data)        
while 1:
    schedule.run_pending()
    time.sleep(1)
   
