import httplib2
import requests
import wget
import os
import io
import urllib.request
import numpy as np
from bs4 import BeautifulSoup, SoupStrainer
from io import BytesIO
from google.cloud import storage

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'C:/Users/w1l-y/Documents/Starchart/google_creds.json'
client = storage.Client()
bucket = client.get_bucket('gaze_pictures_test')
basewidth = 1920
http = httplib2.Http()
status, response = http.request('https://apod.nasa.gov/apod/archivepix.html')
counter = 0
startIndex = 0
goodLabels = open('imagelabels.txt').read().splitlines()

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
                    wget.download(url, out = 'data')
            except Exception as e:
                print(e)
                print('### some weird shit going on w this file')
       # 15 images with errors