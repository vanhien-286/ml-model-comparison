import pandas as pd
df = pd.read_csv('data/spam.csv')

counts = df['label'].value_counts()
print(counts)