################## Linear Support Vector Machine - 82% #######################

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
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
import seaborn as sns
from sklearn.pipeline import make_pipeline
from sklearn.metrics import confusion_matrix, accuracy_score
csv.field_size_limit(sys.maxsize)
from sklearn.svm import LinearSVC
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline

text_data = []
with open('/home/vanitha/Mining_pastebin/Supervised/Large_data/Dataset_labeled_shuffled_large.csv', 'r') as text_data_file:
    csv_reader = csv.reader(text_data_file, delimiter=',')

    next(csv_reader)

    for line in csv_reader:
        text_data.append(line)

#converting list into dataframe
df = DataFrame(text_data,columns=['category','pasteContent'])
print(df.head())

#term document frequency     
tf_idf = TfidfVectorizer(max_features=5500)
features = tf_idf.fit_transform(df['pasteContent']).toarray()
#features = df.pasteContent
labels = df.category
# #print(features.shape)

model = LinearSVC()
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.25, random_state=4000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(y_pred)
print(classification_report(y_test, y_pred))
print("The accuracy is {}".format(accuracy_score(y_test, y_pred)))

######################
# sgd = Pipeline([('vect', CountVectorizer()),('tfidf', TfidfTransformer()),('clf', SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, random_state=42, max_iter=5, tol=None)),])
# sgd.fit(X_train.tolist(), y_train.tolist())
# y_pred = sgd.predict(X_test)
# print('accuracy %s' % accuracy_score(y_pred, y_test))

# from sklearn.svm import SVC
# from sklearn.ensemble import BaggingClassifier
# from sklearn.datasets import make_classification

# clf = BaggingClassifier(base_estimator=SVC(),n_estimators=100, random_state=0).fit(X_train, y_train)
# y_pred = clf.predict(X_test)
# print(classification_report(y_test, y_pred))
# print("The accuracy is {}".format(accuracy_score(y_test, y_pred)))

# T = tfidfconverter.transform(['Hi, hello, I am vanitha \nint a,b,c; a=10; b=20; c=a+b; printf (%d,c);']).toarray()
# y_pred1 = classifier.predict(T)
# print(y_pred1)
