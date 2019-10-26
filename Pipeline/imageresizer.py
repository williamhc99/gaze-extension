import os
import wget
from PIL import Image

directory = '../data/Train/SpaceWallpaper'
smallFiles = '../data/small'
basewidth = 1920
targetheight = 1080
left = 0
right = basewidth

for filename in os.listdir(directory):
    print(filename)
    filepath = directory + '/' + filename
    with Image.open(filepath) as img:
        width, height = img.size
    
    # filter small images out
    if (width < basewidth):
        print(height, width)
        print('too narrow')
        destination = smallFiles + '/' + filename
        try:
            os.rename(filepath, destination)
        except:
            print('image already filtered')
            os.remove(filepath)
        continue
    
    # resize images that are too large
    if (width > basewidth):
        wpercent = (basewidth/float(width))
        hsize = int(float(height)*float(wpercent))
        with Image.open(filepath) as img:
            img_resized = img.resize(
                (basewidth, hsize), Image.ANTIALIAS)
        img_resized.save(filepath)
        print('resized')

    if (height < targetheight):
        print(height, width)
        print('too short')
        destination = smallFiles + '/' + filename
        try:
            os.rename(filepath, destination)
        except:
            print('image already filtered')
            os.remove(filepath)

    if (height > targetheight):
        margin = height - targetheight
        toRemove = margin/2
        top = toRemove
        bottom = height - toRemove 
        with Image.open(filepath) as img:
            img_cropped = img.crop((left, top, right, bottom))
        img_cropped.save(filepath)
        print('cropped')
