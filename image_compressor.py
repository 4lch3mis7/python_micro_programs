from PIL import Image
from pathlib import Path


class ImageCompressor:
    def __init__(self):
        pass

    def percent_of_original(self, source_file, percentage, output_file):
        """Compress Image in percentage of size of original image"""
        img = Image.open(image_path)
        x = img.size[0]*percentage/100
        y = img.size[1]*percentage/100
        img = img.resize((int(x), int(y)), Image.ANTIALIAS)
        img.save(output_file, optimize=True, quality=95)
        img.close()


if __name__ == "__main__":
    image_path = '/home/prasant/Downloads/Montessori Photos/12-20-2020/IMG_9910.JPG'
    x = ImageCompressor()
    x.percent_of_original(image_path, 10, 'compressed.JPG')
