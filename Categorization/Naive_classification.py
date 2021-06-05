################## Naive classification - 78% #######################

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
text_data = []
#df = pd.read_csv('/home/vanitha/Mining_pastebin/Supervised/Dataset_labeled.csv')

with open('/home/vanitha/Mining_pastebin/Supervised/Large_data/Dataset_labeled_shuffled_large.csv', 'r') as text_data_file:
    csv_reader = csv.reader(text_data_file, delimiter=',')

    next(csv_reader)

    for line in csv_reader:
        text_data.append(line)

    print(text_data[9])

#converting list into dataframe
df = DataFrame(text_data,columns=['category','pasteContent'])
print(df.head())

# plotting the number of paste contents in each classes
# fig = plt.figure(figsize=(8,6))
# df.groupby('category').pasteContent.count().plot.bar(ylim=0)
# plt.show()

#term document frequency     
tf_idf = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='latin-1', ngram_range=(1, 2))
features = tf_idf.fit_transform(df['pasteContent']).toarray()
labels = df.category
print(features.shape)

X_train, X_test, y_train, y_test = train_test_split(df['pasteContent'],df['category'],  test_size=0.3, random_state = 100)
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(X_train)
#print(X_train_counts)
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

#model = make_pipeline(TfidfVectorizer(), MultinomialNB())
clf = MultinomialNB().fit(X_train_tfidf, y_train)   
y_pred = clf.predict(count_vect.transform(X_test))  
print("train_data_count ",X_train.count())
print("test_data_count ",X_test.count())

print("The accuracy is {}".format(accuracy_score(y_test, y_pred)))

