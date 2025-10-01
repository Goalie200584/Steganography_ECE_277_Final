def file_convert(decoded_message, file_type):
    file_path = "../output_files/"

    if file_type == "text":
        file_path += "text_output.txt"
        with open(file_path, "wb") as file:
            file.write(decoded_message)
    
    elif file_type == "pdf":
        file_path += "pdf_output.pdf"
    
    try :
        if file_path != "../output_files/":
            return file_path
    except Exception as e:
        print(f"Error Saving File: {e}")



        
