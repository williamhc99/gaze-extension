import httplib2
import requests
import cv2
import wget
import os
from bs4 import BeautifulSoup, SoupStrainer
from io import BytesIO
from PIL import Image
from google.cloud import storage
from tempfile import TemporaryFile

client = storage.Client()
bucket = client.get_bucket('gaze_pictures')

http = httplib2.Http()
status, response = http.request('https://apod.nasa.gov/apod/archivepix.html')
counter = 0
for imageLink in BeautifulSoup(response, "lxml", parse_only=SoupStrainer('a')):
# for i in range(9):
    if counter > 100:
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
                    print(filename)

                    blob = bucket.blob('pic'+str(counter)+'.jpg')
                    blob.upload_from_filename(filename)
                    os.remove(filename)


                    counter += 1
            except Exception as e:
                print(e)
                print('some weird shit going on w this file')
