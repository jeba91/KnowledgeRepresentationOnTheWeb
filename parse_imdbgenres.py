import os
import pandas as pd
import sys
import nltk
from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import word_tokenize
import re

df = pd.read_csv('IMDB/title.basics.tsv', sep='\t')

type_list = ['short','movie','tvMovie']
df = df[df['titleType'].isin(type_list)]
df = df[["tconst","genres"]]

dftemp = df["genres"].str.split(',', expand=True)

df1 = pd.concat([df[["tconst"]], dftemp[0]], axis=1)
df2 = pd.concat([df[["tconst"]], dftemp[1]], axis=1)
df3 = pd.concat([df[["tconst"]], dftemp[2]], axis=1)

df1.columns = ["tconst","genres"]
df2.columns = ["tconst","genres"]
df3.columns = ["tconst","genres"]

df1 = df1[~df1['genres'].isnull()]
df2 = df2[~df2['genres'].isnull()]
df3 = df3[~df3['genres'].isnull()]

df1['genres'].loc[df1['genres'] == r"\N"] = "unknown"

df1.to_csv("csv_file/parsed_imdbgenres1.csv", index = None, header=True)
df2.to_csv("csv_file/parsed_imdbgenres2.csv", index = None, header=True)
df3.to_csv("csv_file/parsed_imdbgenres3.csv", index = None, header=True)
