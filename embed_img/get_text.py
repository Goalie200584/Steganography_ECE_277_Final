def convert_text_to_binary(text) -> list:
    '''
        Converts text to binary utilizing ASCII
        Inputs: 
        Outputs: binary_text, length_binary_text
    '''
    #1. Converts all text into integers
    int_text = []
    for i in text:
        int_text.append(ord(i))
    #2. Converts integer values to binary
    binary_text = ["00000001"]
    # binary_text=[]
    for num in int_text: 
        binary_text.append(f"{num:08b}")
    length_binary_text = len(binary_text)*8
    return binary_text, length_binary_text

    