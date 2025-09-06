def get_text():
    return input("What are the words/sentences you'd like to encode? ")


def convert_text_to_binary():
    text = get_text()
    int_text = []
    for i in text:
        int_text.append(ord(i))
    print(int_text)
    binary_text = []
    for num in int_text: 
        binary_text.append(bin(num))
    return binary_text, len(binary_text)

