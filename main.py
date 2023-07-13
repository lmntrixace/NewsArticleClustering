import json
import random

json_file_path = "train_en_1M.json"

data = []
with open(json_file_path, "r", encoding="utf-8") as json_file:
    for line in json_file:
        json_obj = json.loads(line)
        data.append(json_obj)


random_selection = random.sample(data, k=5)



urls = [json_obj["dh_url"] for json_obj in random_selection]

