import pandas as pd
import glob
import csv
import random
############# Text file to csv ##############

# read_files = glob.glob("/home/vanitha/Mining_pastebin/Supervised/Large_data/Dataset/Zkl/*")
# content = []
# for f in read_files:
#     with open(f, "r") as source_file:
#             content.append(source_file.read())
# print(len(content))

# fields = ['content']
# with open('/home/vanitha/Mining_pastebin/Supervised/Large_data/Dataset/Zkl.csv', 'w') as target_file: 
#     write = csv.writer(target_file)     
#     write.writerow(fields)
#     for val in content:
#         write.writerow([val])

############# Multiple csv to one single csv ################

# path = "/home/vanitha/Mining_pastebin/Supervised/Large_data" # use your path

# all_files = glob.glob(path + "/Dataset/*.csv")

# # Combine all CSV files using the concat method
# merged = pd.concat([pd.read_csv(f) for f in all_files])
# # Export to csv
# merged.to_csv(path+"/Merged_Language_dataset.csv", index=False, encoding='utf-8-sig')
# data = pd.read_csv(path+"/Merged_Language_dataset.csv") 
# print(data.head(5))

############ Shuffling dataset ###############
# text_data = []
# with open('/home/vanitha/Mining_pastebin/Supervised/Merged_Language_dataset.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')

#     next(csv_reader)

#     for line in csv_reader:
#         text_data.append(line)
#     random.shuffle(text_data)
#     print(len(text_data))

#     print(text_data[0])

# fields = ['Code','Language']
# with open('/home/vanitha/Mining_pastebin/Supervised/Merged_Language_dataset_shuffled.csv', 'w') as f:
#     # using csv.writer method from CSV package
#     write = csv.writer(f)    
#     write.writerow(fields)
#     write.writerows(text_data)

############ Language Detection Tool ########################

import random
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
import seaborn as sns
from sklearn.metrics import confusion_matrix, accuracy_score
csv.field_size_limit(sys.maxsize)
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

text_data = []
with open('/home/vanitha/Mining_pastebin/Supervised/Merged_Language_dataset_shuffled.csv', 'r') as text_data_file:
    csv_reader = csv.reader(text_data_file, delimiter=',')

    next(csv_reader)

    for line in csv_reader:
        text_data.append(line)

#converting list into dataframe
df = DataFrame(text_data,columns=['Code','Language'])
print(df.head())

print('\n')
print('It is running...')
print('\n')

#term document frequency     
tfidfconverter = TfidfVectorizer(max_features=6500, min_df=1, max_df=0.7)
features = tfidfconverter.fit_transform(df['Code']).toarray()
labels = df.Language

X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.1, random_state=400)

classifier = RandomForestClassifier(n_estimators=400, random_state=42) #42
classifier.fit(X_train, y_train) 
y_pred = classifier.predict(X_test)
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

# x = 'Hi, hello, I am vanitha \nint a,b,c; a=10; b=20; c=a+b; printf (%d,c);'
# Tr = tfidfconverter.transform([x])
# y_pred1 = classifier.predict(Tr)
# print(y_pred1)
#print(x)

