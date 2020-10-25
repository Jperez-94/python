##########################
# Author: José Luis Pérez
# Date: 25/10/2020
##########################




import pytube
import sys
import os
import re
import progressbar

########################################
# Download a complete list of videos,
# choosing between video or only audio
# format
########################################

print("URL of the original youtube video:")
url = input()

# Choose the format it is going to be downloaded
print("\nDownload audio or video:")
elem_type = input()
print("\nSearching...\n")

# Modify the path where the files are downloaded
path = r"C:\Users\user\Downloads"

try:
    playlist = pytube.Playlist(url)
    # Solve problems to download lists
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
except:
    print("ERROR: An error has ocurred:\n", sys.exc_info())
else:
    print("Downloading...\n")
    try:
        # Show a progressbar of the process
        for i in progressbar.progressbar(range(len(playlist.video_urls)),prefix = 'Progress:', suffix = 'Complete', length = 20):
            try:
                video_url = playlist.video_urls[i]
                if elem_type == "audio":
                    elem = pytube.YouTube(video_url).streams.filter(only_audio=True).first()
                elif elem_type == "video":
                    elem = pytube.YouTube(video_url).streams.filter(only_video=True).first()
                else:
                   raise Exception("\n\n===============================\nERROR: The format required doesn't exist -> " + "\'" + elem_type + "\'\n===============================")
                elem.download(path)
            
            except Exception as wrong_type:
                print(wrong_type.args[0])
                break
            except:
                print("\nIt hasn`t been able to download the video " + elem.title + "\n")
    except:
        print("\nThe download couldn't end:\n", sys.exc_info(), "\n")

print("\nPress ENTER to exit...")
input()