import pandas as pd
import pickle


with open("bits_data.pkl", "rb") as f:
    df = pickle.load(f)

sampled_df = df.sample(n=1000, random_state=42)


output_file = "random.pkl"
with open(output_file, "wb") as f:
    pickle.dump(sampled_df, f)


    