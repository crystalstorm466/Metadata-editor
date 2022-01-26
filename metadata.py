import unicodedata
import mutagen
from mutagen import *
from os import system, name

print("Welcome to Audio Metadata editor\n")
filepath = input("Please provide the file path to your audio file\n")

audio = mutagen.File(filepath)

WhichOne = input("What tag do you want to edit in the file?\nTitle\nArtist\nTrackNumber\nAlbum\nGenre\n")
print("The answer is " + WhichOne)
if WhichOne == "Title":
    if name == 'nt':
        system('cls')
    else:
        system('clear')
    NewTitle = input("What is the new title?\n")
    audio["title"] = (NewTitle) #mutagen.TextFrame(encoding=3, text=[NewTitle]) 
    print(audio)
    mutagen.save(audio)


