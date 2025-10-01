import codecs
def file_convert(bit_stream, file_path, file_type):
    
    if file_type == "text":
        file_path += "/StegTextOutput.txt"
        try:
            with open(file_path, "x") as file:
                file.write(bit_stream)
        except FileExistsError:

            with open(file_path, "w+") as file:
                file.write(bit_stream) 
    
    elif file_type == "pdf":
        file_path += "/StegPDFOutput.pdf"  
        output = ""
        for i in bit_stream:
            integer_val = int(i, 2)
            ascii = chr(integer_val)
            output += ascii

        b64PDF = output.encode("utf-8")
        pdf_output = codecs.decode(b64PDF, "base64")

        try: 
            with open(file_path, "xb") as file: 
                file.write(pdf_output)
        except FileExistsError:
            with open(file_path, "wb") as file:
                file.write(pdf_output)

        
