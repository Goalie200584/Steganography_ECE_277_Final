def get_pdf_bytes(pdf_path):
    with open(pdf_path, "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

        bit_stream = []
        for byte in pdf_bytes:
            bit_stream.append(f"{byte:08b}")
        
    return bit_stream, len(bit_stream)