from PIL import Image
import numpy as np
def convert_img_to_binary(img_path:str)-> list:
    """
    Converts embedded image into all binary bits
    Inputs: img_path
    Outputs:  
    """
    img = Image.open(img_path)
    img = np.array(img.conert("RGB"))

    bin_arr = []

    for c,i in enumerate(img):
        bin_arr.append([])
        for e, x in enumerate(i):
            bin_arr[c].append([])
            for z in x:
                bin_arr[c][e].append([])
                bin_arr[c][e].append(f"{z:08b}")
    print(bin_arr)