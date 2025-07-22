import pdfplumber

import os
# print(os.getcwd())

# Get the absolute path to the script file
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create path to the PDF file relative to the script
pdf_path = os.path.join(script_dir, "MS_Entries.pdf")

with pdfplumber.open(pdf_path) as pdf:
    first_page = pdf.pages[0]
    text = first_page.extract_text()
    # print(text)

output_file_path = os.path.join(script_dir, 'gentelmens_singles_entry_list.txt')
with open(output_file_path, 'w') as f:
    f.write(text)
