import torch
import keras
import keras_nlp
import os
from transformers import AutoTokenizer, AutoModelForCausalLM

# pip install accelerate
os.environ["HF_TOKEN"] = 'insert your token'
access_token = 'your token'

tokenizer = AutoTokenizer.from_pretrained("google/gemma-2b", token = access_token)
model = AutoModelForCausalLM.from_pretrained("google/gemma-2b", token = access_token)"

tokenizer = AutoTokenizer.from_pretrained("google/gemma-7b-it")
model = AutoModelForCausalLM.from_pretrained("google/gemma-7b-it", device_map="auto")

input_text = "Write me a poem about Machine Learning."
input_ids = tokenizer(input_text, return_tensors="pt").to("cuda")

outputs = model.generate(**input_ids)
print(tokenizer.decode(outputs[0]))
