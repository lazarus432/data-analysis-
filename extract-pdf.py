import PyPDF2

newfile = open('pdf.txt', 'w')
file = open('C:\Users\Nicolas\Desktop\data-analysis\pdf-ex.pdf', 'rb')
pdfreader = PyPDF2.PdfFileReader(file)
# print(pdfreader.getNumPages())
pageobj = pdfreader.getPage(6)
newfile.write(pageobj.extractText())
file.close()
newfile.close()
# print("Your file has been extracted to txt")
