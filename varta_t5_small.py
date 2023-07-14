from articles import text_data
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("rahular/varta-t5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("rahular/varta-t5-small")

embeddings = []
count = 0
if torch.cuda.is_available():
    device = torch.device("cuda")
    model.to(device)
else:
    device = torch.device("cpu")

for text in text_data:
    text_chunks = [text[i:i+512] for i in range(0, len(text), 512)]
    chunk_embeddings = []

    for chunk in text_chunks:
        encoded_input = tokenizer(chunk, return_tensors="pt", padding=True, truncation=True, max_length=512).to(device)
        with torch.inference_mode():
            model_output = model.generate(
                input_ids=encoded_input["input_ids"],
                attention_mask=encoded_input["attention_mask"],
                num_beams=4,
                max_length=512,
                early_stopping=True
            )
        vector_embedding = model_output[0].float().mean(dim=0).squeeze()
        chunk_embeddings.append(vector_embedding.to(device))

    final_embedding = torch.stack(chunk_embeddings).mean(dim=0)
    count = count + 1
    if count == 2:
        print("Done with another 1000")
        break
    embeddings.append(final_embedding)


embeddings_cpu = [embedding.cpu() for embedding in embeddings]


