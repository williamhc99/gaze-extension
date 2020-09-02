# gaze-extension

A personal python project focused around Computer Vision. The aim was to create a library that would be able to scrape Nasa's website for space pictures. These pictures would then go into a pipeline where they will be filtered and resized based on their pixel density and blur detection using OpenCV. These filtered and resized pictures would be fed to a SVM that I trained with a dataset of 600 pictures. The pictures that are deemed worthy 'space themed wallpaper' get stored inside a GCP bucket. 

The chrome extension https://chrome.google.com/webstore/detail/gaze/hdjjocbdhnjchhepfdioddlooblklboa then pulls a random space wallpaper everytime you open a new tab. 

## imagedownloader.py

This python file will scrape this page: https://apod.nasa.gov/apod/archivepix.html and then filter for cool space pictures and store them

The pictures are stored on a Google Cloud Storage. 

## imageresizer.py

This file will filter and resize all the pictures using simple methods like simple count and more complex methods like applying the Laplacian Matrix to determine the 'blurriness' of the picture

## imageclassifier.py

This file contains the code I used to train my space themed wallpaper SVM as a lot of pictures that my pipeline produces are not space themed.

## Todo

- [ ] Utilized trained model to automatically store inside GCP bucket
- [ ] Setup cron job for this code to run at set time interval for fresh pictures
