
def get_pdf_bytes():
    with open("./PDFs/test.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()
        print(pdf_bytes)
