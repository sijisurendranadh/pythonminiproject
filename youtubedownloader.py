#!/usr/bin/env python3
#REQUIREMENT:
#5.  Download the video from url if it is available.
from pytube import YouTube
def banner():
    
    print("\nYoutube downloader with Pytube..\n")
def download():
    try:
        tubeURL=input("Enter the Youtube URL to download: ")
        yt_obj = YouTube(tubeURL)
        filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
        # download the highest quality video
        filters.get_highest_resolution().download()
        print('\nVideo Downloaded Successfully\n')
    except Exception as e:
        print(e)
def main():
    banner()
    download()
if __name__ == "__main__":
    main()