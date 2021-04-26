import torch
import fasttext
import os

model_path = '../../../../fastText/cc.de.300.bin'
model = fasttext.load_model(model_path)
print("model loaded")
model.get_word_vector("1984")
model.get_word_vector("2004")
model.get_word_vector("location")
model.get_word_vector("15345")
