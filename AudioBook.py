import pyttsx3
import PyPDF2
book = open('1st Syllabus 2021.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
#for num in range(3,pages):
page = pdfReader.getPage(0)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()
