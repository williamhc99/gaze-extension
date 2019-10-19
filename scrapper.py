import httplib2
import requests
import cv2
import wget
import os
import io
import urllib.request
import numpy as np
from bs4 import BeautifulSoup, SoupStrainer
from io import BytesIO
from PIL import Image
from google.cloud import storage
from tempfile import TemporaryFile
from google.cloud import vision
from google.cloud.vision import types

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'C:/Users/w1l-y/Documents/Starchart/google_creds.json'
client = storage.Client()
bucket = client.get_bucket('gaze_pictures_test')
basewidth = 1920
http = httplib2.Http()
status, response = http.request('https://apod.nasa.gov/apod/archivepix.html')
counter = 0
startIndex = 0
goodLabels = open('imagelabels.txt').read().splitlines()
client = vision.ImageAnnotatorClient()
for imageLink in BeautifulSoup(response, "lxml", parse_only=SoupStrainer('a')):
    # for i in range(9):
    if counter >= 50:
        break
    if hasattr(imageLink, 'href') and str(imageLink['href']).startswith('ap'):
        # imagePage , content = http.request('https://apod.nasa.gov/apod/ap19020' + str(i+1) + '.html')
        imagePage, content = http.request(
            'https://apod.nasa.gov/apod/' + str(imageLink['href']))
        for link in BeautifulSoup(content, "lxml", parse_only=SoupStrainer('a')):
            try:
                if hasattr(link, 'href') and str(link['href']).startswith('image') and str(link['href']).endswith('.jpg'):
                    url = 'https://apod.nasa.gov/apod/' + str(link['href'])
                    wget.download(url)

                    filename = str(link['href'])[11:]

                    with Image.open(filename) as img:
                        width, height = img.size

                    # Check ratios
                    if not(width >= 1.25*height and width <= 1.75*height):
                    # if (3 * width < 4 * height) or (9 * width > 16 * height):
                        print('too long/too short gang')
                        print('width: ', width)
                        print('height: ', height)
                        os.remove(filename)
                        break

                    # Check resolutions
                    if height < 1080 or width < 1920:
                        print('low res gang')
                        print('width: ', width)
                        print('height: ', height)
                        os.remove(filename)
                        break
                    # Resolution too high, resize
                    elif height > 1080 and width > 1920:
                        wpercent = (basewidth/float(width))
                        hsize = int(float(height)*float(wpercent))
                        with Image.open(filename) as img:
                            img_resized = img.resize(
                                (basewidth, hsize), Image.ANTIALIAS)
                        img_resized.save(filename)
                        print('resized')
                    
                    # Update width and height
                    if height >= 1080 and width >= 1920:
                        with Image.open(filename) as img:
                            width, height = img.size
                    
                    # create cv2 image for HoughLines analysis
                    img = cv2.imread(filename)
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    edges = cv2.Canny(gray,90,150,apertureSize = 3)
                    kernel = np.ones((3,3),np.uint8)
                    edges = cv2.dilate(edges,kernel,iterations = 1)
                    kernel = np.ones((5,5),np.uint8)
                    edges = cv2.erode(edges,kernel,iterations = 1)
                    # cv2.imwrite('canny.jpg',edges)

                    lines = cv2.HoughLines(edges,1,np.pi/180,150)
                    if lines is None:
                        print('nolines!')
                    else:
                        filtered_lines = []
                        quad = 1.5708 # 90 degrees
                        margin = 0.0872665 # 5 degrees
                        horizontal = 0
                        vertical = 0

                        for line in lines:
                            rho,theta = line[0]
                            if abs(theta) < margin:
                                horizontal += 1
                                filtered_lines.append(line)
                            elif abs(theta - quad) < margin:
                                vertical += 1
                                filtered_lines.append(line)

                        print('Number of filtered lines:', len(filtered_lines))

                        if horizontal > 1 and vertical > 1 and len(filtered_lines) < 200:
                            print('theres a grid fam')
                            print(filename)
                            os.remove(filename)
                            print('file removed')
                            break

                    file_name = os.path.join(
                        os.path.dirname(__file__),
                        filename)

                    with io.open(file_name, 'rb') as image_file:
                        content = image_file.read()

                    image = types.Image(content=content)
                    response = client.label_detection(image=image)
                    labels = response.label_annotations
                    print('sent to google vision')
                    score = 0
                    for label in labels:
                        if (label.description in goodLabels):
                            score += 1

                    percentage = score/len(labels)
                    print(percentage)

                    # if (percentage > 0.6):
                    #     blob = bucket.blob('pic'+str(counter)+'.jpg')
                    #     blob.upload_from_filename(filename)
                    #     counter += 1

                    print(filename)
                    # os.remove(filename)
                    print('file removed')

            except Exception as e:
                print(e)
                print('### some weird shit going on w this file')

print(goodLabels)
