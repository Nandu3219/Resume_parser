import spacy
import pickle
import random

import sys, fitz

print(spacy.__version__)
nlp_model = spacy.load('nlp_model')


fname = "CV_NandeeshaBS_03.pdf"
doc = fitz.open(fname)
text = ""

for page in doc:
    text = text + str(page.get_text())

tx = "".join(text.split('\n'))
# print(tx)

doc = nlp_model(tx)

for entity in doc.ents:
    print(f'{entity.label_.upper():{15}}- {entity.text}')

