import cv2
from urllib.request import urlopen

imageLinks = open("imageurl.txt")
counter = 0
for url in imageLinks:
  if counter > 10:
    break

  with urlopen(url) as img:
    with open(str(counter)+'pic.jpg', "w+") as file:
      cv2.imwrite(file,img)

  print(url) 
  # wget.download(url)

  # filename = str(link['href'])[11:]
  # print(filename)
  counter += 1

