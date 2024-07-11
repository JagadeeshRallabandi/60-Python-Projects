import PyPDF2

# Open the PDF file
pdf_file_path = 'file.pdf'
pdf_file = open(pdf_file_path, 'rb')

# Initialize the PDF reader
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Extract text from each page
all_text = ""
for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    text = page.extract_text()
    all_text += text

# Close the PDF file
pdf_file.close()

# Print the extracted text
print(all_text)
