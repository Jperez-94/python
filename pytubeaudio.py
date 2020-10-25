##########################
# Author: José Luis Pérez
# Date: 25/10/2020
##########################



import pytube
import sys
import os

#########################################
# Download audio channel of any youtube
# video.
#########################################


print("URL of the original youtube video:")
url = input()

print("\nSearching...\n")

# Modify the path where the files are downloaded
path = r"C:\Users\user\Downloads"

try:
    audio = pytube.YouTube(url).streams.filter(only_audio=True).first()
except:
    print("Se ha producido un error durante la busqueda:\n", sys.exc_info())
else:
    print("Downloading...\n")
    try:
        audio.download(path)
    except:
        print("No pudo completarse la descarga:\n", sys.exc_info(), "\n")
    else:
        print("Done\n")

print("Press ENTER to exit...")
input()