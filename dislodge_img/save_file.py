

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
        byte_values = [int(byte, 2) for byte in decoded_message]
        file_bytes = bytes(byte_values)

        try: 
            with open(file_path, "xb") as file: 
                file.write(file_bytes)
        except FileExistsError:
            with open(file_path, "wb+") as file:
                file.write(file_bytes)

        
