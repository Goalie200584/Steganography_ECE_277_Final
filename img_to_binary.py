from PIL import Image
def convert():
    img = Image.open("image.png")
    img = img.convert("RGB") 
    r,g,b = img.getpixel((1,1))

    print(r,g,b)
convert()