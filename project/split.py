# ~/n8n-server/project/split.py
import sys
import os
from PyPDF2 import PdfReader, PdfWriter

filename = sys.argv[1]
input_pdf = os.path.join('/home/node/doc', filename)
output_dir = '/home/node/output_pages'
os.makedirs(output_dir, exist_ok=True)

reader = PdfReader(input_pdf)

for i in range(len(reader.pages)):
    writer = PdfWriter()
    writer.add_page(reader.pages[i])
    output_file = os.path.join(output_dir, f'page_{i+1}.pdf')
    with open(output_file, 'wb') as f:
        writer.write(f)

print(filename)
