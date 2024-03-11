import torch
import keras
import keras_nlp
import os
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModel

prompt = "The best recipe for pasta is" 
checkpoint = "models/Qwen/" 
tokenizer = AutoTokenizer.from_pretrained(checkpoint) 
model = AutoModelForCausalLM.from_pretrained(checkpoint, torch_dtype=torch.float16, device_map="cuda") 
inputs = tokenizer(prompt, return_tensors="pt").to('cuda') 
outputs = model.generate(**inputs, do_sample=True, max_new_tokens=150) 
result = tokenizer.decode(outputs[0], skip_special_tokens=True) 
print(result)
