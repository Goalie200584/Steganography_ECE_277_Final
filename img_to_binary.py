from PIL import Image
import numpy as np
from get_text import convert_text_to_binary
import math
def convert_img_to_binary(text_length:int) -> list:
    """function takes in an image and the text length, and provides
        the nessacery amount of pixels converted to binary numbers

        Inputs: text_length
        Outputs: binary_list
    """
    # 1. Import our image and converting to RGB and a NumPy array
    img = Image.open("image.png")
    img_array = np.array(img.convert("RGB"))
    img_width = img.size[0]

    #2. determine the amount of rows of pixels needed to enscribe 
    num_pixel_rows = math.ceil(text_length/img_width)

    #3. Convert each needed row to binary
    output_binary = (num_pixel_rows, [])
    for i in range(num_pixel_rows):
        output_binary[1].append([])        
        for c, x in enumerate(img_array[i]):
            output_binary[1][i].append([])  
            for z in img_array[i][c]: output_binary[1][i-1][c].append(bin(z))
    
    return output_binary