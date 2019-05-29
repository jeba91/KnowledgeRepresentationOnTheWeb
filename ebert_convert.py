import pandas
import os
import pandas as pd
import sys
import nltk
from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import word_tokenize
import re
from fuzzywuzzy import process
from nltk.metrics import edit_distance
import time

start = time.time()
reviews = pandas.read_pickle('ebert_reviews.pkl')
df = pd.read_csv('IMDB/title.basics.tsv', sep='\t')
type_list = ['short','movie','tvMovie']
df = df[df['titleType'].isin(type_list)]
df = df[['tconst','primaryTitle']]
reviews["tconst"] = ""
reviews["primaryTitle"] = ""
end = time.time()
print(start-end)

for index, row in reviews.iterrows():
    start = time.time()
    dfcopy = df.copy(deep=True)
    dfcopy = dfcopy[dfcopy['primaryTitle'].apply(lambda x: len(x) == len(row['Title']))]
    dfcopy['score'] = dfcopy['primaryTitle'].apply(lambda x: edit_distance(x,row['Title']))
    dfcopy = dfcopy.sort_values(by=['score'])
    reviews.at[index, "tconst"] = dfcopy["tconst"].iloc[0]
    reviews.at[index, "primaryTitle"] = dfcopy['primaryTitle'].iloc[0]
    end = time.time()
    print(index, row['Title'], dfcopy['primaryTitle'].iloc[0], start-end)

reviews.to_pickle("reviews_with_tconst.pkl")


# results = df.loc[:, ["primaryTitle", "column2"]].apply(lambda x: edit_distance(*x), axis=1)
# print(df.assign(Output=[process.extract(i, df['primaryTitle'], limit=1) for i in reviews['Title']]))
# print(df)
