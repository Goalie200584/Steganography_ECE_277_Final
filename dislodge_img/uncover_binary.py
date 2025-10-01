import numpy as np
def uncover_info(img_bin:np.array)-> list:
    '''
        Decodes the img array and unveils the hidden message behind the img
        
        Inputs: img_bin
        Outputs: bin_message 
    '''
    current_letter = ""
    bin_message = []
    file_type = ""
    #1. Parses through each RGB value in binary form and adds each 8 bit letter we encoded
    # from the end of our RGB value until we see our indicator to stop in this case it is 10 repeated 8 times.
    for row in img_bin:
        for pixel in row:
            for bin in pixel:
                if len(current_letter) < 8:
                    current_letter += bin[-1]
                    #2. Checks if our current letter is our indicator, as well as the last message was our indicator
                    # and returns the whole binary message 
                elif len(current_letter) == 8: 
                    if current_letter == "10101010" and bin_message[-1] == "10101010":
                        if bin_message[0] == "00000001":
                            file_type = "text"
                        elif bin_message[0] == "00000010":
                            file_type = "pdf"
                        print(file_type, "FILE_TYPE from UNCOVER_INFO")
                        return bin_message[1:-1], file_type
                    else:
                        bin_message.append(current_letter)
                        current_letter = bin[-1]
