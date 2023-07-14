import pandas as pd
import torch


path = "bits_data.pkl"

data = pd.read_pickle(path)

print(data.columns)


print(data['assigned_category'].unique())