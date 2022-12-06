import os
from pdf2image import convert_from_path

pdfs = [filename for filename in os.listdir() if ".pdf" in filename]
for filename in pdfs:
    if "resume" in filename:
        continue
    image = convert_from_path(filename)
    image[0].save(filename.replace(".pdf", ".png"), "PNG")
