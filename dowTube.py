from pytube import YouTube
import os

SAVE_PATH = os.path.expanduser('~/Downloads')

# Function to download one video
def give_link():
    link = input("Paste the link here: ")

    try:
        yt = YouTube(link)
    except:
        print("Error: The link given doesn't exist")

    video = yt.streams.get_highest_resolution()

    try:
        video.download(SAVE_PATH)
        print(video.title + ": Video downloaded successfuly")
    except:
        print("Error downloading the video")
    

# Function to download multiple videos
def give_mul_links():
    print("* Paste the links separate with a coma: link1,link2,link3 *")
    links = input("Paste the links here: ")
    links = "[" + links + "]"
    values = [ x.strip() for x in links.strip('[]').split(',') ]
    
    for i in values:
        try:
            yt = YouTube(i)
        except:
            print("Error: The link given doesn't exist")

        video = yt.streams.get_highest_resolution()

        try:
            video.download(SAVE_PATH)
            print(video.title + ": Video downloaded successfuly")
        except:
            print("Error downloading the video")

# Function to download multiple videos from a .txt
def give_txt():
    f = open("links.txt", "r")
    links = f.readlines()

    for i in links:
        try:
            yt = YouTube(i)
        except:
            print("Error: The link given doesn't exist")
        
        video = yt.streams.get_highest_resolution()

        try:
            video.download(SAVE_PATH)
            print(video.title + ": Video downloaded succesfuly")
        except:
            print("Error downloading the video")

# Main
option = 0

while option < 4:
    print("+ - - - - - - - - - - - - - - - - - - +")
    print("|      For give a link write 1        |")
    print("|   For give multiple links write 2   |")
    print("|  For give a txt with links write 3  |")
    print("|           To exit write 4           |")
    print("+ - - - - - - - - - - - - - - - - - - +")
    option = int(input("Select an option: "))

    if(option==1):
        give_link()
        break
    elif(option==2):
        give_mul_links()
        break
    elif(option==3):
        give_txt()
        break