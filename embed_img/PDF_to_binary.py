def get_pdf_bytes(pdf_path):
    #Creates bit_stream which is intialized with an indicator so the dislodger knows its a pdf file that is embedded
    bit_stream = ["00000010"]
    with open(pdf_path, "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

        for byte in pdf_bytes:
            bit_stream.append(f"{byte:08b}")
        
    return bit_stream, len(bit_stream) * 8