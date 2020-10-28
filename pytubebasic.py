##########################
# Author: José Luis Pérez
# Date: 25/10/2020
##########################



import pytube
import sys
import os


########################################
# Initial script to use pytube library
# It shows all the available formats of
# the desire video and you choose which
# is downloaded.
########################################


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
    youtube = pytube.YouTube(url)
except:
    print("ERROR: There is a problem with the video URL\n", sys.exc_info())
    sys.exit()
else:
    # List of the available formats
    streams = youtube.streams.all()
    print("======================================")
    print("Formats available:")
    print("======================================")
    for i in streams:
        print(i)
    print("======================================\n")

    # Look at the itag of each item in the list and the associated format
    itag = input('Choose the \"itag\" of the format you want to download:\n')
    print("\nDownloading...\n")
    video = youtube.streams.get_by_itag(int(itag))
    video.download(path)

    print("\nDone")

    input('\nPress ENTER to exit...')