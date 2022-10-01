from google_images_download import google_images_download
import os

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"FriendsCharacters","limit":20, "f":"jpg", "print_urls":True}   #creating list of arguments

paths = response.download(arguments)   #passing the arguments to the function

print(paths)

