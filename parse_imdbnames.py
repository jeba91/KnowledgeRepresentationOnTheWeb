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
df = df.drop(columns="endYear")
df = df.drop(columns="genres")

df['startYear'] = df['startYear'].replace(r"\N", 1500)
# df = df['isAdult'].replace(r"\N", 0)
df['runtimeMinutes'] = df['runtimeMinutes'].replace(r"\N", 0)

df.to_csv("csv_file/parsed_imdbnames.csv", index = None, header=True)
