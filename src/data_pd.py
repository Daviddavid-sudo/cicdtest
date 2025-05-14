import pandas as pd

data = pd.read_csv('data/dataset.csv')
data.drop_duplicates(inplace=True, ignore_index=True)