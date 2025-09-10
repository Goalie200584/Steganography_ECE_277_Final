from PIL import Image
import numpy as np
def convert_img_to_binary(img_path:str)-> list:
    """
    Converts embedded image into all binary bits
    Inputs: img_path
    Outputs:  
    """
    img = Image.open(img_path)
    img = np.array(img.convert("RGB"))

    

    output_binary = []
    for i in range(len(img)):
        output_binary.append([])      
        for c, x in enumerate(img[i]):
            output_binary[i].append([])  
            for z in img[i][c]: output_binary[i-1][c].append(f"{z:08b}") 
    
    return output_binary

    