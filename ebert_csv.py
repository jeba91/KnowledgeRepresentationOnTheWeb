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
reviews = pandas.read_pickle('reviews_with_tconst.pkl')
content = pandas.read_pickle('ebert_content.pkl')
reviews['score'] = reviews.apply(lambda x: edit_distance(x['primaryTitle'],x['Title']), axis=1)
content['tconst'] = reviews['tconst']
idx = reviews['score']<2

content['URL'] = content['URL'].str.replace(" ","")

reviews = reviews.loc[idx]
content = content.loc[idx]

content = content.astype(str)
content['Rating'] = content['Rating'].str.replace("(b\')|\'", "")
content['Runtime'] = content['Runtime'].str.replace("(b\')|\'", "")


rogertebert = pd.concat([reviews[['Title', 'EbertStars', 'Year', 'URL', 'tconst','score']],content[['Rating','Runtime','Review']]],axis=1)

reviews.to_pickle("reviewsEbertCleanTconst.pkl")
