import os
import wget
from PIL import Image

directory = '../data/SpaceWallpaper'
smallFiles = '../data/SpaceWallpaper/small'
basewidth = 1920

for filename in os.listdir(directory):
    print(filename)
    filepath = directory + '/' + filename
    with Image.open(filepath) as img:
        width, height = img.size
    
    # filter small images out
    if (width < basewidth):
        print(height, width)
        print('too small')
        destination = smallFiles + '/' + filename
        os.rename(filepath, destination)
    
    # resize images that are too large
    if (width > basewidth):
        wpercent = (basewidth/float(width))
        hsize = int(float(height)*float(wpercent))
        with Image.open(filepath) as img:
            img_resized = img.resize(
                (basewidth, hsize), Image.ANTIALIAS)
        img_resized.save(filepath)
        print('resized')

    