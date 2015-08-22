from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
import os
import json
import numpy as np

root_dir = 'data/tweets/'

vectorizer = TfidfVectorizer(min_df=2, stop_words = 'english',\
                        strip_accents = 'unicode', lowercase=True, ngram_range=(1,2),\
                        norm='l2', smooth_idf=True, sublinear_tf=False, use_idf=True)

tweeps = []
tweets = []

files = os.listdir(root_dir)

for file in files:
    tweeps.append('@'+file)
    tweets.append(open(root_dir + file, 'r').read())

X = vectorizer.fit_transform(tweets)

D = -(X * X.T).todense() # Distance matrix: dot product between tfidf vectors

D = np.array(D).tolist()

print D

# print tweeps