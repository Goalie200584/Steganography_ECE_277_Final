def XOR_cipher(text:str, key:str)-> str:
    processed_text = ""
    key_length = len(key)

    for i in range(len(text)):
        # Get the character from the text
        text_char_code = ord(text[i])
        
        # Get the corresponding character from the key, repeating the key if necessary
        key_char_code = ord(key[i % key_length])
        
        # Perform the XOR operation on the character codes
        encrypted_char_code = text_char_code ^ key_char_code
        
        # Convert the new character code back to a character and add it to the result
        processed_text += chr(encrypted_char_code)
        
    return processed_text




