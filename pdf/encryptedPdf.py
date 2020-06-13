# coding: utf-8
import PyPDF2
pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
pdfReader.isEncrypted

pdfReader.decrypt('rosebud')
pdfReader.getPage(0)

pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
pdfReader.decrypt('rosebud')
pageObj = pdfReader.getPage(0)
pageObj
