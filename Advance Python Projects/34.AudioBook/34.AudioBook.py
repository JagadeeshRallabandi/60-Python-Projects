import PyPDF2
import pyttsx3

# Initialize the text-to-speech engine
speaker = pyttsx3.init()

# Open the PDF file
pdf_file = open('file.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(pdf_file)

# Iterate through each page in the PDF
full_text = ""
for page_num in range(len(pdfReader.pages)):
    page = pdfReader.pages[page_num]
    text = page.extract_text()
    full_text += text

# Convert the full text to speech
speaker.say(full_text)
speaker.runAndWait()

# Stop the speaker
speaker.stop()

# Save the text to an audio file
speaker.save_to_file(full_text, 'audio.mp3')
speaker.runAndWait()

# Close the PDF file
pdf_file.close()
