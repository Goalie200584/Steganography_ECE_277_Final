import codecs
def get_pdf_bytes(pdf_path):
    datafile = open(pdf_path, "rb")
    pdfdatab = datafile.read()
    datafile.close()

    b64PDF = codecs.encode(pdfdatab, "base64")

    Sb64PDF = b64PDF.decode("utf-8")

    bit_stream  = ["00000010"]
    for byte in Sb64PDF:
        byte = ord(byte)
        bit_stream.append(f"{byte:08b}")
    
    return bit_stream, len(bit_stream)*8