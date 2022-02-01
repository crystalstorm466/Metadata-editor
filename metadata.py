import sys
from time import sleep
import time
import unicodedata
import mutagen
from mutagen import *
from mutagen.id3 import ID3NoHeaderError
from mutagen.id3 import ID3, TIT2, TALB, TPE1, TPE2, COMM, TCOM, TCON, TDRC, TRCK
from mutagen.flac import FLAC
from mutagen.mp3 import MP3
from mutagen.aac import AAC
from mutagen.m4a import M4A
from mutagen.ogg import OggFileType
from mutagen.wave import WAVE
from mutagen.smf import SMF
from mutagen.easyid3 import EasyID3
from os import system, name

def Choice2Exit():
    Exit = input("Do you want to continue editing? \n")
    if Exit == "Yes" or "Y":
     TagEdit(filepath, audio)
    elif Exit == "No" or "N":
        sys.exit(0)


print("Welcome to Audio Metadata editor\n")
print("Supported File Types are:\nFlAC, MP3, AAC, M4A, OGG,and WAV\n")

filepath = input("Please provide the file path to your audio file\n")
 




#this identifes the filetype and opens it, yes I could just use mutagen.File however it does not allow for tag editing
try: 
    audio = EasyID3(filepath)
except ID3NoHeaderError:
    audio = mutagen.File(filepath, easy=True)
    audio.add_tags()







def TagEdit(filepath, audio):
    WhichOne = input("What tag do you want to edit in the file?\nTitle\nArtist\nTrack Number\nAlbum\nGenre\n")

    print("The answer is " + WhichOne)
    if name == 'nt':
        system('cls') # windows clear command
    else:
        system('clear') # linux and unix clear command

    if WhichOne == "title" or "Title":

        NewTitle = input("What is the new title?\n")
        audio["title"] = NewTitle
        audio.save(v1=0, v2_version=3)
        print(audio)

    elif WhichOne == "Artist" or "artist":

        NewArtist = input("What is the new Artist?")
        audio["artist"] = NewArtist
        print(audio)
        audio.save(v1=0, v2_version=3)

    elif WhichOne == "trackNumber" or "Track Number":

        NewTrackNumber = input("What is the Track Number")
        audio["tracknumber"] = NewTrackNumber
        audio.save(v1=0, v2_version=3)
        print(audio)

    elif WhichOne == "album" or "Album":

        NewAlbum = input("What is the Album name?")
        audio["album"] = NewAlbum
        audio.save(v1=0, v2_version=3)
        print(audio)
    elif WhichOne == "genre" or "Genre":

        NewGenre = input("What is the Genre?")
        audio["genre"] = NewGenre
        audio.save(v1=0, v2_version=3)
        print(audio)

    time.sleep(3)
    if name == 'nt':
        system('cls') # windows clear command
    else:
        system('clear') # linux and unix clear command
    Choice2Exit()
    


TagEdit(filepath, audio)


        