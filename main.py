from get_text import convert_text_to_binary
from img_to_binary import convert


if __name__ == "__main__":
    text_bin, text_length = convert_text_to_binary()
    img_bin = convert(text_length)