#Exercise 8 - Merge the PDF
import PyPDF2

input_files = ['MD Niamul Islam Ankon css2.pdf','Digital garage.pdf','MD Niamul Islam Ankon.pdf','MD Niamul Islam Ankon Python.pdf','MD Niamul Islam Ankon Html.pdf']  # List of PDF files to merge
output_file = 'merged.pdf'  # Name of the merged PDF file

pdf_merger = PyPDF2.PdfMerger()

for file in input_files:
    pdf_merger.append(file)

with open(output_file, 'wb') as output:
    pdf_merger.write(output)

print(f'{len(input_files)} PDF files merged into {output_file}.')