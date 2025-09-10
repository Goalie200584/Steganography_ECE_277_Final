import embed_img.get_text as get_text 
import embed_img.img_to_binary as img_to_binary
import embed_img.embed as embed
import embed_img.save_img as save_img
import dislodge_img.convert_to_dislodge as convert_to_dislodge
import dislodge_img.uncover_binary as uncover_binary
import dislodge_img.convert_bin_to_text as convert_bin_to_text

original_img_path = "./images/image.png"
dislodge_path = "./images/embedded_image.png"
if __name__ == "__main__":
    path = int(input("Do you want to 1. embed a secret, or 2. discover a secret? "))
    if path == 1:
        text = get_text.get_text()
        text_bin, text_length = get_text.convert_text_to_binary(text)
        num_of_rows, img_bin = img_to_binary.convert_img_to_binary(original_img_path, text_length)   
        embed.embed_message(text_bin, img_bin)
        save_img.save_img(original_img_path, img_bin)
    if path == 2:
        img_bin_decode = convert_to_dislodge.convert_img_to_binary(dislodge_path)
        bin_text = uncover_binary.uncover_info(img_bin_decode)
        #Discover why the bin_text shows up as a none type when there are spaces in the embedded text
        decoded_message = convert_bin_to_text.convert_to_text(bin_text)

        print(f"Decoded Message: {decoded_message}")

        



