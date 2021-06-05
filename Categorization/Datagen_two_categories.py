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
#df = pd.read_csv('/home/vanitha/Mining_pastebin/Train_data.csv')
#print(df)
print("Pastes downloading...")
num = 210
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
            art1 = soup1.find('div',class_='code')
                #tit = soup1.find('h1')
                #date = soup1.find('li', class_='date')
                #dict = {'paste_title':tit.text, 'paste_date':date.text, 'paste_content': art1.text}
            pastes_raw.append(art1.text)
        print(len(pastes_raw))
        urls_storage = []
        n = n+1
        
    except:
        print(error)

pastes = []
g = 0
while(g < len(pastes_raw)):
    #s = re.sub(re.compile("#.*?\n" ) ,"" ,pastes_raw[g])  
    s = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,pastes_raw[g]) # remove all occurrences streamed comments (/*COMMENT */) from string
    s = re.sub(re.compile("//.*?\n" ) ,"" ,s) # remove all occurrence single-line comments (//COMMENT\n ) from string
    s = re.sub(re.compile("<!--.*?-->" ) ,"" ,s) 
    s = re.sub(re.compile("///.*?\n" ) ,"" ,s) 
    s = re.sub(re.compile("<%--.*?--%>" ) ,"" ,s) 
    s = re.sub(re.compile("{\*.*?\*}" ) ,"" ,s) 
    s = re.sub(re.compile("(\*.*?\*)" ) ,"" ,s) 
    s = re.sub(re.compile("{-.*?-}" ) ,"" ,s) 
    text = os.linesep.join([i for i in s.splitlines() if i])
    pastes.append(text)
    g = g+1

with open('/home/vanitha/Mining_pastebin/Supervised/Large_data/Text_data_spam_text.csv', 'r') as text_data_file:
    csv_reader = csv.reader(text_data_file, delimiter=',')

    next(csv_reader)

    for line in csv_reader:
        text_data.append(line[0])
    print(len(text_data))

r  = int((len(pastes)+ len(text_data[:8401]))/2)
print(r)

def append_row(file_name, list_of_elements):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elements)

p = 0
s = 1050
while p < s:
    #final_data.append(['code and text',pastes[p]+text_data[p]])
    row_contents = ['other',pastes[p]+'\n'+text_data[p]]
    append_row('/home/vanitha/Mining_pastebin/Supervised/Large_data/Dataset_labeled_two.csv', row_contents)
    p = p+1

q = s
w = 2100
while  q < w:
    #final_data.append(['code and text',pastes[p]+text_data[p]])
    row_contents = ['other',text_data[q]+'\n'+pastes[q]]
    append_row('/home/vanitha/Mining_pastebin/Supervised/Large_data/Dataset_labeled_two.csv', row_contents)
    q = q+1

i = w
k = 6300
while i < k:
    # List of strings
    row_contents = ['code only',pastes[i]]
    # Append a list as new line to an old csv file
    append_row('/home/vanitha/Mining_pastebin/Supervised/Large_data/Dataset_labeled_two.csv', row_contents)
    row_contents = ['other',text_data[i]]
    append_row('/home/vanitha/Mining_pastebin/Supervised/Large_data/Dataset_labeled_two.csv', row_contents)
    i = i+1














        