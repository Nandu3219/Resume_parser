import spacy
import pickle
import random
import warnings
import sys, fitz, os
import re

# print(spacy.__version__)

warnings.filterwarnings("ignore", category=UserWarning)
# nlp_model = spacy.load('E:\\Nandu\Smartbox\pythonProject\Gsm_testing\output\model-last')
nlp_model = spacy.load('E:\\Nandu\Smartbox\pythonProject\Gsm_testing\data_from_Resume\\backup_Output\model-last')
fname = "E:\\Nandu\Smartbox\pythonProject\Gsm_testing\data_from_Resume\Resume_folder\\Naukri_AdityaKumar[5y_2m].pdf"
# folder_path = 'Resume_folder'
# files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]
# pdf_paths = [os.path.join(folder_path, file) for file in files]
# print(pdf_paths)
# req_skill_list=['C', 'Embedded C', 'Canoe', 'python','IPC','Multithreading']
# req_tech_list= ['Linux','AUTOSAR', 'Automotive', 'Embedded SW', 'Embedded Systems', 'embedded', 'JIRA', 'Linux Device Drivers']
# req_protocol_list = ['CAN', 'UART', 'SPI', 'I2C', 'UDS']

user_input = input("enter the req skills, technolgies, protocols by seperating space : ")
user_input = user_input.split()
req_skill_list = list(user_input)
print(req_skill_list)


def get_resume_detailes(file_name):
    doc = fitz.open(file_name)
    text = ""
    skills_list = []
    tech_list = []
    protocol_list = []

    for page in doc:
        text = text + str(page.get_text())

    tx = "".join(text.split('\n'))
    doc = nlp_model(tx)

    for entity in doc.ents:
        # line = f"{entity.label_.upper():{20}}- {entity.text}"
        # print(f'{entity.label_.upper():{20}}- {entity.text}')
        if entity.label_.upper() == "SKILLS":
            skills_list.append(entity.text)

        if entity.label_.upper() == "PROTOCOLS":
            skills_list.append(entity.text)

        if entity.label_.upper() == "TECHNOLOGIES":
            skills_list.append(entity.text)
        # with open("extracted_details.txt", "a+",  encoding="utf-8") as f:
        #     f.write(f"\n{line}")

    skill_pattern = re.compile(r'\b(?:' + '|'.join(req_skill_list) + r')\b', re.IGNORECASE)
    # tech_pattern = re.compile(r'\b(?:' + '|'.join(req_tech_list) + r')\b', re.IGNORECASE)
    # protocol_pattern = re.compile(r'\b(?:' + '|'.join(req_protocol_list) + r')\b', re.IGNORECASE)

    matches_skills = re.findall(skill_pattern, tx)
    # matches_technologies = re.findall(tech_pattern, tx)
    # matches_protocols = re.findall(protocol_pattern, tx)

    skills_ratio = len(set(map(str.lower, matches_skills)).intersection(map(str.lower, req_skill_list))) / len(req_skill_list)
    # technologies_ratio = len(set(matches_technologies).intersection(req_tech_list)) / len(req_tech_list)
    # protocols_ratio = len(set(matches_protocols).intersection(req_protocol_list)) / len(req_protocol_list)

    print(f"Skills Comparison Ratio: {round(skills_ratio, 2) * 100} %")
    # print("Technologies Comparison Ratio:", round(technologies_ratio, 3), tech_list)
    # print("Protocols Comparison Ratio:", round(protocols_ratio), protocol_list)

# for fname in pdf_paths:
#     get_resume_detailes(fname)
#     with open("extracted_details.txt", "a+", encoding="utf-8") as f:
#         f.write(f"\n******%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%********")
#     print('******************************************************************************************************')


get_resume_detailes(fname)




