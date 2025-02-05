import os
from PyPDF2 import PdfMerger

# Get a list of PDF pdf_files
pdf_files = [os.path.join("meals", file) for file in os.listdir("meals")]
print (pdf_files)


# Merge all PDF files into a single PDF
merger = PdfMerger()
for pdf in pdf_files:
    merger.append(pdf)
merger.write("bank-f-meals.pdf")
merger.close()

# Clean up temporary PDF files
for pdf in pdf_files:
    os.remove(pdf)
