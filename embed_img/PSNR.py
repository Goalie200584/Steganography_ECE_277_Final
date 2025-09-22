import cv2

def get_psnr(img_path:str, embedded_img_path:str):
    og_img = cv2.imread(img_path)
    embedded_img = cv2.imread(embedded_img_path)

    psnr_val = cv2.PSNR(og_img, embedded_img)

    return psnr_val