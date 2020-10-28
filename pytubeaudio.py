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


# Modify the path of the folder where the files are downloaded
try:
    path = r"C:\Users\user\Downloads"
    if (os.path.isdir(path) == False):
        raise Exception()
except:
    print('ERROR: You have to introduce a valid folder path', sys.exc_info())
    sys.exit()


url = input('URL of the original youtube video:\n')

print("\nSearching...\n")


try:
    audio = pytube.YouTube(url).streams.filter(only_audio=True).first()
except:
    print("ERROR: The download was cancelled:\n", sys.exc_info())
    sys.exit()
else:
    print("Downloading...\n")
    try:
        audio.download(path)
    except:
        print("ERROR: The download was cancelled:\n", sys.exc_info(), "\n")
        sys.exit()
    else:
        print("Done\n")

input('Press ENTER to exit...')