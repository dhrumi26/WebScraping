import os
from PIL import Image
import cv2

img_dir = r"/home/ubuntu/web_scraping/google-images-download/downloads/FriendsCharacters/"
# filtering frineds folder
for filename in os.listdir(img_dir):
    try :
        with Image.open(img_dir + "/" + filename) as im:
             print('ok')
    except :
        print(img_dir + "/" + filename)
        os.remove(img_dir + "/" + filename)

# removing files that are not in jpg format
for filename in os.listdir(img_dir):
    if filename[-3:] == 'jpg':
        continue
    else:
        os.remove(img_dir + "/" + filename)


# for filename in os.listdir(img_dir):
#     print(filename[-3:])

# renaming files
i =0
for filename in os.listdir(img_dir):
    dst ="Friends%i"%i + ".jpg"
    src =img_dir + filename 
    dst =img_dir + dst 
        
    # rename() function will 
    # rename all the files 
    os.rename(src, dst)
    i += 1

# resizing and grascaling images
count = 0
for filename in os.listdir(img_dir):
    imgPath = img_dir + filename
    img = cv2.imread(imgPath)
    img = cv2.resize(img, (240,240))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('/home/ubuntu/web_scraping/google-images-download/downloads/FriendsCharacters/Friends%i.jpg'%count, img)
    count += 1
