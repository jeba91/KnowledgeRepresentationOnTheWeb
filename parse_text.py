import os
import pandas as pd
import sys
import nltk
from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import word_tokenize
import re

# Run commands for parsing all files
# python parse_text.py kaggle/test/pos/ kaggle/test/urls_pos.txt "csv_file/pos_test.csv"
# python parse_text.py kaggle/train/pos/ kaggle/train/urls_pos.txt "csv_file/pos_train.csv"
# python parse_text.py kaggle/test/neg/ kaggle/test/urls_neg.txt "csv_file/neg_test.csv"
# python parse_text.py kaggle/train/neg/ kaggle/train/urls_neg.txt "csv_file/neg_train.csv"

sid = SentimentIntensityAnalyzer()
rdf_triples = pd.DataFrame(columns = ['nconst' , 'rating' , 'sent_word'])
map_path = sys.argv[1]
lsorted = sorted(os.listdir(map_path), key=lambda x: int(str(x).split("_")[0]))
links = [line.rstrip('\n') for line in open(sys.argv[2])]
links = [url[:-13] for url in links]

rows_list = []

for idx, reviews in enumerate(lsorted):
    pos_word_list=[]
    neg_word_list=[]

    splitted = re.split("[._]+", reviews)
    sentence = open(map_path + reviews, 'r').read()
    tokenized_sentence = word_tokenize(sentence)

    for word in tokenized_sentence:
        if (sid.polarity_scores(word)['compound']) >= 0.1:
            pos_word_list.append(word)
        elif (sid.polarity_scores(word)['compound']) <= -0.1:
            neg_word_list.append(word)

    pos_word_list = [x.lower() for x in pos_word_list]
    neg_word_list = [x.lower() for x in neg_word_list]
    pos_word_list = [re.sub(r"[^a-zA-Z0-9]+", '', x) for x in pos_word_list]
    neg_word_list = [re.sub(r"[^a-zA-Z0-9]+", '', x) for x in neg_word_list]
    pos_word_list = list(set(pos_word_list))
    neg_word_list = list(set(neg_word_list))

    for word in pos_word_list:
        dict1 = {"nconst":links[idx], "rating":splitted[1], "sent_word":word}
        rows_list.append(dict1)
    for word in neg_word_list:
        dict1 = {"nconst":links[idx], "rating":splitted[1], "sent_word":word}
        rows_list.append(dict1)

df = pd.DataFrame(rows_list)
export_csv = df.to_csv (sys.argv[3], index = None, header=True)
print(df[0:5])
