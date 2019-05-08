import pandas as pd
import sys

file_path = sys.argv[1]+'.tsv'
save_path = sys.argv[1]+'.csv'

print(sys.argv)
dfs = pd.read_csv(file_path, sep='\t', chunksize=50)
for df in dfs:
    df.to_csv(save_path, sep=',', mode='a')
