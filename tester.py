# import cv2
# from urllib.request import urlopen

# imageLinks = open("imageurl.txt")
# counter = 0
# for url in imageLinks:
#   if counter > 10:
#     break

#   with urlopen(url) as img:
#     with open(str(counter)+'pic.jpg', "w+") as file:
#       cv2.imwrite(file,img)

#   print(url) 
#   # wget.download(url)

#   # filename = str(link['href'])[11:]
#   # print(filename)
#   counter += 1

import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

file_name = os.path.join(
    os.path.dirname(__file__),
    'M82Magnet_SOFIA_2412.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

print('Labels:')
for label in labels:
    print(label.description)