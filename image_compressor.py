from PIL import Image
from pathlib import Path


def compress(image_path, minimum_original_size, compression_percent):
    # get image size
    size = Path(image_path).stat().st_size
    if size >= minimum_original_size:
        # Open image
        img = Image.open(image_path)
        x = img.size[0]*compression_percent/100
        y = img.size[1]*compression_percent/100
        img = img.resize((int(x),int(y)), Image.ANTIALIAS)
        img.save(image_path, optimize=True, quality=95)
        img.close()



