import pandas as pd


path = "bits_data.pkl"

data = pd.read_pickle(path)
text_data = []

for index, row in data.iterrows():
    combined_text = row["html_chunk1"] + row["html_chunk2"]
    text_data.append(combined_text)

