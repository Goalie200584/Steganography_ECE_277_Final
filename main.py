import get_text 
import img_to_binary
import embed

if __name__ == "__main__":
    path = int(input("Do you want to 1. embed a secret, or 2. discover a secret? "))
    if path == 1:
        text = get_text.get_text()
        text_bin, text_length = get_text.convert_text_to_binary(text)
        num_of_rows, img_bin = img_to_binary.convert_img_to_binary(text_length)
        embed.embed_message(text_bin, img_bin)


