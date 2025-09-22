from PIL import Image
import numpy as np

def save_img(img_path:str, img_bin:list):
    '''
        Used to save our new image as a PNG
        
        Inputs: img_path, img_binary
        Outputs: N/A
    '''

    # print(img_bin)
    #1. Convert rows from binary back to RGB
    original = Image.open(img_path)
    original = np.array(original.convert("RGB"))
    num_pixel_rows = len(img_bin)
    RGB_rows = []
    for row in range(num_pixel_rows):
        RGB_rows.append([]) 
        for pixel in range(len(img_bin[row])):
            RGB_rows[row].append([])
            for z in img_bin[row][pixel]: RGB_rows[row][pixel].append(int(z, 2)) 
        original[row] = list(RGB_rows[row])
    

    temp_path = img_path.split("/")[:-1]
    temp_path.append("embedded_img.png")
    print(temp_path)
    img_output_path = "/".join(temp_path)

    embedded_image = Image.fromarray(original)
    embedded_image.save(img_output_path)

    return img_output_path
    
