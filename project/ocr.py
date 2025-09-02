# ~/n8n-server/project/ocr.py
import sys
import os
from typhoon_ocr import ocr_document

os.environ['TYPHOON_OCR_API_KEY'] = 'sk-exG2quLki26LNGCwBOySDtqlkaMNvxPbFaXVX5MnFsdWYW00'

sys.stdout.reconfigure(encoding='utf-8')

input_path = sys.argv[1]
text = ocr_document(input_path)
print(text)
