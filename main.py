import embed_img.get_text as get_text 
import img_to_binary
import embed_img.embed as embed
import embed_img.save_img as save_img

img_path = "./images/image.png"
if __name__ == "__main__":
    path = int(input("Do you want to 1. embed a secret, or 2. discover a secret? "))
    if path == 1:
        text = get_text.get_text()
        text_bin, text_length = get_text.convert_text_to_binary(text)
        num_of_rows, img_bin = img_to_binary.convert_img_to_binary(img_path, text_length)
        embed.embed_message(text_bin, img_bin)
        save_img.save_img(img_path, img_bin)



