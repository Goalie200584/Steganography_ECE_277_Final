import codecs
datafile = open("./PDFs/test.pdf", "rb")
pdfdatab = datafile.read()
datafile.close()

b64PDF = codecs.encode(pdfdatab, "base64")

Sb64PDF = b64PDF.decode("utf-8")

bit_stream  = []
for byte in Sb64PDF:
    byte = ord(byte)
    bit_stream.append(f"{byte:08b}")


output = ""
for i in bit_stream:
    integer_val = int(i, 2)
    ascii = chr(integer_val)
    output+= ascii

b64PDF = output.encode("utf-8")
pdf_output = codecs.decode(b64PDF, "base64")

datafile = open("./test_1.pdf", "xb")
datafile.write(pdf_output)
datafile.close()

if Sb64PDF == output:
    print("It Equals the output!")






