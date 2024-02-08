import os
import docx2txt
import fitz

current_directory = os.getcwd()


def pdf_to_txt(pdf_path, txt_path):
    try:
        with fitz.open(pdf_path) as pdf_document:
            text = ''
            for page_number in range(pdf_document.page_count):
                page = pdf_document.load_page(page_number)
                text += page.get_text()
            tx = " ".join(text.split('\n'))
            with open(txt_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(tx)
    except fitz.FileDataError:
        print(f"Error: {pdf_path} is a broken or corrupted document. Skipped.")


def convert_pdfs(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(input_directory, filename)
            txt_filename = os.path.splitext(filename)[0] + '.txt'
            txt_path = os.path.join(output_directory, txt_filename)
            pdf_to_txt(pdf_path, txt_path)
            print(f"Converted: {filename} -> {txt_filename}")


input_directory = os.path.join(current_directory, 'Resume_folder')
print(input_directory)
output_directory = os.path.join(current_directory, 'Txt_Resume_folder')
convert_pdfs(input_directory, output_directory)

