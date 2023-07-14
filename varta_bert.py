from articles import text_data
import torch
from transformers import AutoTokenizer, AutoModelForMaskedLM


tokenizer = AutoTokenizer.from_pretrained("rahular/varta-bert")
model = AutoModelForMaskedLM.from_pretrained("rahular/varta-bert")


embeddings = []
count = 0

if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

for text in text_data:
    text_chunks = [text[i:i+512] for i in range(0, len(text), 512)]
    chunk_embeddings = []
    
    
    for chunk in text_chunks:
        encoded_input = tokenizer(chunk, return_tensors="pt").to(device)
        with torch.inference_mode():
            model_output = model(**encoded_input)
        vector_embedding = model_output[0].mean(dim=1).squeeze()
        chunk_embeddings.append(vector_embedding)
    
    
    final_embedding = torch.stack(chunk_embeddings).mean(dim=0)
    count = count + 1
    if count == 10:
        print("Done with first 10")
    embeddings.append(final_embedding)
    

embeddings = embeddings.cpu()   
