################## Random forest classifier - 91.38% ####################33
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

text_data = []
with open('/home/vanitha/Mining_pastebin/Supervised/Large_data/Dataset_labeled.csv', 'r') as text_data_file:
    csv_reader = csv.reader(text_data_file, delimiter=',')

    next(csv_reader)

    for line in csv_reader:
        text_data.append(line)

#converting list into dataframe
df = DataFrame(text_data,columns=['category','pasteContent'])
print(df.head())

#term document frequency     
tfidfconverter = TfidfVectorizer(max_features=4000, min_df=1, max_df=0.7)
features = tfidfconverter.fit_transform(df['pasteContent']).toarray()
labels = df.category

X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=800)

classifier = RandomForestClassifier(n_estimators=1000, random_state=42) #42
classifier.fit(X_train, y_train) 
y_pred = classifier.predict(X_test)
#y_pred2 = classifier.predict(X_train)
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))
#print(accuracy_score(y_train, y_pred))

x = 'Hi, hello, I am vanitha \nint a,b,c; a=10; b=20; c=a+b; printf (%d,c);'
Tr = tfidfconverter.transform([x])
y_pred1 = classifier.predict(Tr)
print(y_pred1)
#print(x)

############################

# rfc = RandomForestClassifier()
# parameters = {
#     "n_estimators":[2500,3000,3500,4000],
#     "random_state":[20,30,42,None]   
# }

# cv = GridSearchCV(rfc,parameters,cv=5)
# cv.fit(X_train, y_train)

# def display(results):
#     print(f'Best parameters are: {results.best_params_}')
#     print("\n")
#     mean_score = results.cv_results_['mean_test_score']
#     std_score = results.cv_results_['std_test_score']
#     params = results.cv_results_['params']
#     for mean,std,params in zip(mean_score,std_score,params):
#         print(f'{round(mean,3)} + or -{round(std,3)} for the {params}')

# display(cv)