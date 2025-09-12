def embed_message(text_bin:list, img_bin:list) -> list:
    '''
        Embeds a secret message into the binary lists of the picture
        Inputs: text_bin, img_bin
        Outputs: embedded_pic
    '''
    text_stuff = []
    #1. Formats all binary numbers from text
    total_count = 0
    row_count = 0
    pixel_count = 0 
    RGB_count = 0
    #1.5. Encodes the end of my 
    text_bin.append("10101010")
    text_bin.append("10101010")
    # print(text_bin)
    for letter in text_bin:
        # print(letter)
        #2. Identifies and embeds all Binary numbers from text
        for bit in letter:
            #3. Replaces the LSB in our RGB value with the next sequential binary number from text
            img_bin[row_count][pixel_count][RGB_count] = img_bin[row_count][pixel_count][RGB_count][:7] + bit
            #4. Tracks the index we are on for the img binary
            if RGB_count == 2:
                RGB_count = 0
                if pixel_count == len(img_bin[0])-1:
                    pixel_count = 0
                    row_count += 1
                else:
                    pixel_count += 1
                  
            else: 
                RGB_count += 1
            
            
            total_count += 1
    return img_bin


