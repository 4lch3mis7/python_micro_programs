from PIL import Image

def compress(image_path, compression_percent):
    # Open image
    img = Image.open(image_path)
    print(img.size)  # (5760, 3240)
    x = img.size[0]*compression_percent/100
    y = img.size[1]*compression_percent/100
    img = img.resize((int(x),int(y)), Image.ANTIALIAS)
    img.save(image_path, optimize=True, quality=95)
    img.close()

if __name__ == '__main__':
    image_path = input('Image > ')
    percent = input('Compression Percentage > ') 
    compress(image_path, percent)


