import os
import cv2


DIR_PATH = '/home/ubuntu/web_scraping/google-images-download/downloads/Paris/'
# for count,filename in enumerate(os.listdir(DIR_PATH)):
#     dst ="Paris" + str(count) + ".jpg"
#     src =DIR_PATH + filename 
#     dst =DIR_PATH + dst 
        
#     # rename() function will 
#     # rename all the files 
#     os.rename(src, dst)
count = 0
for filename in os.listdir(DIR_PATH):
    imgPath = DIR_PATH + filename
    img = cv2.imread(imgPath)
    img = cv2.resize(img, (240,240))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('/home/ubuntu/web_scraping/google-images-download/downloads/Paris/Paris%i.jpg'%count, img)
    count += 1


