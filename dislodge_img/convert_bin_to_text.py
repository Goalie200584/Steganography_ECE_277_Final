def convert_to_text(bin_text:list)-> str:
    '''
        Converts any decoded binary message in list form with 1 byte per  index
        into an english human readable message
        
        Inputs: bin_text
        Outputs: message
    '''
    message = ""
    #1. Parses through our list of binary letters and uses chr(int(num, 2))  to convert each byte into a char
    # and adds each letter/character to our new message
    for num in bin_text:
        message += chr(int(num, 2))
    return message
