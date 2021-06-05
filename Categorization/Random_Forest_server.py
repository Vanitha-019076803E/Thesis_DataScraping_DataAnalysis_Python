import glob
import gzip, io
import csv

contents = []

#patoolib.extract_archive("/mnt/ssd1/pastebin/circl_data/codepad.org/2015/10.tar",outdir="/home/vanitha/codepad_org_2015")

ZIPFILES='/home/vanitha/codepad_org_2015/home/rommelfs/pystemon/archive/codepad.org/2015/10/14/*'

filelist = glob.glob(ZIPFILES)

for gzfile in filelist:
    print("#Starting " + gzfile) 
    with gzip.open(gzfile, 'r') as f:
        contents.append(f.read())

#patoolib.extract_archive("/mnt/ssd1/pastebin/circl_data/codepad.org/2015/12.tar",outdir="/home/vanitha/codepad_org_2015")
i = 16
n = 32

while i < n:
    ZIPFILES1='/home/vanitha/codepad_org_2015/home/rommelfs/pystemon/archive/codepad.org/2015/12/'+str(i)+'/*'
    filelist1 = glob.glob(ZIPFILES1)
    for gzfile in filelist1:
        print("#Starting " + gzfile) 
        with gzip.open(gzfile, 'r') as f:
            contents.append(f.read())
    i = i+1

m = 0
contents_filtered = []
while m < len(contents):
    contents_filtered.append(contents[m].replace("\r\n", " "))
    m = m+1
################## Random forest classifier - 91.38% ####################
import pandas as pd
import numpy as np
import csv
import sys
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import seaborn as snssklearn
from sklearn.metrics import confusion_matrix, accuracy_score
csv.field_size_limit(sys.maxsize)
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier

text_data = []
with open('/home/vanitha/Dataset_labeled.csv', 'r') as text_data_file:
    csv_reader = csv.reader(text_data_file, delimiter=',')

    next(csv_reader)

    for line in csv_reader:
        text_data.append(line)

#converting list into dataframe
df = DataFrame(text_data,columns=['category','pasteContent'])
print(df.head())

# # plotting the number of paste contents in each classes
# fig = plt.figure(figsize=(8,6))
# df.groupby('category').pasteContent.count().plot.bar(ylim=0)
# plt.show()

#term document frequency     
tfidfconverter = TfidfVectorizer(max_features=4000, min_df=1, max_df=0.7)
features = tfidfconverter.fit_transform(df['pasteContent']).toarray()
labels = df.category

X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=800)

#########for displaying predicted values ########3

T = tfidfconverter.transform(contents[:2000])
classifier = RandomForestClassifier(n_estimators=1000, random_state=42)
classifier.fit(X_train, y_train) 
y_pred = classifier.predict(T)

zip_of_predictions = zip(contents,y_pred)
list_of_predictions = list(zip_of_predictions)
print(list_of_predictions[0])

fields = ['pasteContent', 'category'] 
with open('/home/vanitha/prediction.csv', 'w') as f:    
    # using csv.writer method from CSV package
    write = csv.writer(f)     
    write.writerow(fields)
    write.writerows(list_of_predictions)

################ for only with 50 predictions to know whether it is working fine ######

T1 = tfidfconverter.transform(contents[:50]).toarray()
y_pred1 = classifier.predict(T1)

test_data = []

### take 50 pastes and its predictions in testData.csv file
with open('/home/vanitha/testData.csv', 'r') as f:    
    # using csv.writer method from CSV package
    csv_reader = csv.reader(f,delimiter=',')
    next(csv_reader)
    for line in csv_reader:
        test_data.append(line[1])
    print(len(test_data))
   
print(confusion_matrix(test_data,y_pred1))
print(classification_report(test_data,y_pred1))
print(accuracy_score(test_data, y_pred1))

