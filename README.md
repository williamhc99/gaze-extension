# gaze-extension

## Todo

- [ ] add OpenCV blur detection
- [ ] add OpenCV line detection
- [ ] store 'bad' pictures on gcp storage bucket
- [ ] space picture AI

## How the pictures are obtained

The python file scrapper.py will scrape this page: https://apod.nasa.gov/apod/archivepix.html and then filter for cool space pictures and store them

The pictures are stored on a Google Cloud Storage. 
