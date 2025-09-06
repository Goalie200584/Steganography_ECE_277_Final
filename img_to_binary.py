from PIL import Image
import numpy as np
from get_text import convert_text_to_binary
import math
def convert(text_length):
    img = Image.open("image.png")
    img_array = np.array(img.convert("RGB"))
    img_width = img.size[0]

    count = 1
    num_rows_pixels = math.ceil(text_length/img_width)
    while count <= text_length:
        for i in range(num_rows_pixels):
            while count <= img_width:
                
                # print(img_array[2][0])
                # print(len(img_array[2])) Write code to transform these into Binary

                count += 1
        
convert(2)