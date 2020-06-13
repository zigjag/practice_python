import PyPDF2
import os

pdfFiles = []
pdfWriter = PyPDF2.pdfWriter()

for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.pdfReader(pdfFileObj)

    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

resultPdf = open('allminutes.pdf', 'wb')
pdfWriter.write(resultPdf)
resultPdf.close()
