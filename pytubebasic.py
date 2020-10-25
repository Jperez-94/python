##########################
# Author: José Luis Pérez
# Date: 25/10/2020
##########################



import pytube
import sys


########################################
# Initial script to use pytube library
# It shows all the available formats of
# the desire video and you choose which
# is downloaded.
########################################


print("URL of the original youtube video:")
url = input()

print("\nSearching...\n")

# Modify the path where the files are downloaded
path = r"C:\Users\user\Downloads"

try:
    youtube = pytube.YouTube(url)
except:
    print("ERROR: There is a problem with the video URL\n", sys.exc_info())
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
    print("Choose the \"itag\" of the format you want to download:")
    itag = input()
    print("\nDownloading...\n")
    video = youtube.streams.get_by_itag(int(itag))
    video.download(path)

    print("\nDone")

    print("\nPress ENTER to exit...")
    input()