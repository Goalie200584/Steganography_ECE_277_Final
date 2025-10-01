from PIL import Image
import numpy as np
from embed_img.get_text import convert_text_to_binary
import math
def convert_img_to_binary(img_path:str, text_length:int) -> list:
    '''
        Converts the necessary img into binary with the apropriate amount of rows depending on text length

        Inputs: text_length
        Outputs: binary_list
    '''
    # 1. Import our image and converting to RGB and a NumPy array
    img = Image.open(img_path)
    img_array = np.array(img.convert("RGB"))
    img_width = img.size[0]


    #2. determine the amount of rows of pixels needed to enscribe
    bits_to_embed = text_length + 16
    num_pixel_rows = math.ceil(bits_to_embed/(img_width *3))
    img_area = img.size[0] * img.size[1]

    #Makes sure the text has enough room to fit into all pixels in the image
    #img_area * 3 to account for all RGB values in each pixel, since we can embed 3 bits per pixel
    print(img_area*3)
    print(bits_to_embed)
    if img_area * 3 < bits_to_embed:
        print("File too large to fit into this image, Crashing...")
        quit()

    #3. Convert each needed row to binary
    output_binary = (num_pixel_rows, [])
    for i in range(num_pixel_rows):
        output_binary[1].append([])      
        for c, x in enumerate(img_array[i]):
            output_binary[1][i].append([])  
            for z in img_array[i][c]: output_binary[1][i][c].append(f"{z:08b}") 
    
    return output_binary