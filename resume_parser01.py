import spacy
import pickle
import random
import warnings
import sys, fitz, os

# print(spacy.__version__)

warnings.filterwarnings("ignore", category=UserWarning)
# nlp_model = spacy.load('E:\\Nandu\Smartbox\pythonProject\Gsm_testing\output\model-last')
folder_path = 'Resume_folder'
path = os.path.join("new_output")
print(path)
nlp_model = spacy.load(path+'\\model-last')
fname = "Resume_folder\\Mohini Isalkar_2.6_Automotive_14-08-2023.pdf"

files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]
pdf_paths = [os.path.join(folder_path, file) for file in files]
print(pdf_paths)


def get_resume_detailes(file_name):
    doc = fitz.open(file_name)
    text = ""

    for page in doc:
        text = text + str(page.get_text())

    tx = "".join(text.split('\n'))
    doc = nlp_model(tx)

    for entity in doc.ents:
        line = f"{entity.label_.upper():{20}}- {entity.text}"
        print(f'{entity.label_.upper():{20}}- {entity.text}')
        # with open("extracted_details.txt", "a+",  encoding="utf-8") as f:
        #     f.write(f"\n{line}")




# for fname in pdf_paths:
#     get_resume_detailes(fname)
#     # with open("extracted_details.txt", "a+", encoding="utf-8") as f:
#     #     f.write(f"\n******%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%********")
#     print('******************************************************************************************************')
get_resume_detailes(fname)
