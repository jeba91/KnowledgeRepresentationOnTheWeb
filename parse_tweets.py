import os
import pandas as pd
import sys
import nltk
from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import word_tokenize
import re

df = pd.read_csv('tweets/ratings.dat',names=["user","nconst","rating","userid"], sep="::", header=None, engine='python')
df['nconst'] = df['nconst'].astype(str)
max_length = 7
df.nconst = df.nconst.apply(lambda x: "0"*(max_length - len(x)) + x)

export_csv = df.to_csv("csv_file/tweets_ratings.csv", index = None, header=True)
