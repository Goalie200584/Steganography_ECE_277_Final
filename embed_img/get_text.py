def get_text() -> tuple:
    '''
        Retrieves the text that we need to encode
        
        Inputs: N/A
        Outputs: binary_text, length_binary_text
    '''
    return input("What are the words/sentences you'd like to encode? ")


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
    binary_text = []
    for num in int_text: 
        binary_text.append(f"{num:08b}")
    length_binary_text = len(binary_text)*8
    return binary_text, length_binary_text



