

def file_convert(decoded_message, file_path, file_type):
    
    if file_type == "text":
        file_path += "/StegTextOutput.txt"
        try:
            with open(file_path, "x") as file:
                file.write(decoded_message)
        except FileExistsError:

            with open(file_path, "w+") as file:
                file.write(decoded_message) 
    
    elif file_type == "pdf":
        file_path += "/StegPDFOutput.pdf"  
        try: 
            with open(file_path, "x") as file: 
                file.write(decoded_message)
        except FileExistsError:
            with open(file_path, "w+"):
                file.write(decoded_message)

        
