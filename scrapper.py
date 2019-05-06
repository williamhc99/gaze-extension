import httplib2
import requests
import cv2
import wget
import os
import io
from bs4 import BeautifulSoup, SoupStrainer
from io import BytesIO
from PIL import Image
from google.cloud import storage
from tempfile import TemporaryFile
from google.cloud import vision
from google.cloud.vision import types

client = storage.Client()
bucket = client.get_bucket('gaze_pictures_test')
basewidth = 1920
http = httplib2.Http()
status, response = http.request('https://apod.nasa.gov/apod/archivepix.html')
counter = 0
startIndex = 0
goodLabels = open('src/imagelabels.txt').read().splitlines()
client = vision.ImageAnnotatorClient()
for imageLink in BeautifulSoup(response, "lxml", parse_only=SoupStrainer('a')):
# for i in range(9):
    if counter >= 100:
        break
    if hasattr(imageLink, 'href') and str(imageLink['href']).startswith('ap'):
        # imagePage , content = http.request('https://apod.nasa.gov/apod/ap19020' + str(i+1) + '.html')
        imagePage , content = http.request('https://apod.nasa.gov/apod/' + str(imageLink['href']))
        for link in BeautifulSoup(content, "lxml", parse_only=SoupStrainer('a')):
            try:
                if hasattr(link, 'href') and str(link['href']).startswith('image') and str(link['href']).endswith('.jpg'):
                    url = 'https://apod.nasa.gov/apod/' + str(link['href'])
                    wget.download(url)
                    
                    filename = str(link['href'])[11:]

                    img = Image.open(filename)
                    width, height = img.size
                    if (3 * width < 4 * height) or (9 * width > 16 * height):
                        print('too long/too short gang')
                        os.remove(filename)
                        break
                    if height < 1080 or width < 1920:
                        print('low res gang')
                        os.remove(filename)
                        break
                    elif height > 1080 and width > 1920:
                        wpercent = (basewidth/float(width))
                        hsize = int(float(height)*float(wpercent))
                        img_resized = img.resize((basewidth,hsize), Image.ANTIALIAS)
                        img_resized.save(filename)
                    
                    if height >= 1080 and width >= 1920:
                        img = Image.open(filename)
                        width, height = img.size                  

                    file_name = os.path.join(
                        os.path.dirname(__file__),
                        filename)

                    with io.open(file_name, 'rb') as image_file:
                        content = image_file.read()

                    image = types.Image(content=content)
                    response = client.label_detection(image=image)
                    labels = response.label_annotations

                    score = 0
                    for label in labels:
                        if (label.description in goodLabels):
                            score+=1
                    
                    percentage = score/len(labels)
                    print(percentage)

                    if (percentage > 0.6):
                        blob = bucket.blob('pic'+str(counter)+'.jpg')
                        blob.upload_from_filename(filename)
                        counter += 1

                    os.remove(filename)

            except Exception as e:
                print(e)
                print('### some weird shit going on w this file')

print(goodLabels)
