def embed_message(text_bin:list, img_bin:list) -> list:
    """
    Embeds a secret message into the binary lists of the picture
    Inputs: text_bin, img_bin
    Outputs: embedded_pic
    """
    #1. Formats and embeds all binary numbers from text
    for i in text_bin:
        i = list(i)
        del i[1]
        i = "".join(i)
        for j in i:
            #needs to replace the LSB from each squential binary number from the img