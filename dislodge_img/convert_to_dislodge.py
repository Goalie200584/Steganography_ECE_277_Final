from PIL import Image
import numpy as np
def convert_img_to_binary(img_path:str)-> list:
    '''
        Converts embedded image into all binary bits
        
        Inputs: img_path
        Outputs: output_binary
    '''
    #1. Collects img data and ronvert to RGB format
    img = Image.open(img_path)
    img = np.array(img.convert("RGB"))
    #2. Parses through th numpy array img converting each element to 
    # 8 bit binary and adding each element to the output list
    output_binary = []
    for row_num in range(len(img)):
        output_binary.append([])      
        for pixel_num in range(len(img[row_num])):
            output_binary[row_num].append([])  
            for RGB in img[row_num][pixel_num]: output_binary[row_num][pixel_num].append(f"{RGB:08b}") 
            
    return output_binary

    