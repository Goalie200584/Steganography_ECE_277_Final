def convert_to_text(bin_text):
    message = ""
    bin_text = bin_text[:-1]
    for num in bin_text:
        message += chr(int(num, 2))
    return message
