from time import sleep
import time
import mutagen
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
import sys 

def Choice2Exit():
    Exit = input("Do you want to continue editing? \n")
    if Exit == "Y":
        print("yes")
        TagEdit(filepath, audio)
    elif Exit == "N":
        print("Bye\n")
        sys.exit()

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
    if name == 'nt':
        system('cls') # windows clear command
    else:
        system('clear') # linux and unix clear command

    if WhichOne == "Title":

        NewTitle = input("What is the new title?\n")
        audio["title"] = NewTitle
        audio.save(v1=0, v2_version=3)
        print(audio)

    elif WhichOne == "Artist":

        NewArtist = input("What is the new Artist?\n")
        audio["artist"] = NewArtist
        print(audio)
        audio.save(v1=0, v2_version=3)

    elif WhichOne == "Track Number":

        NewTrackNumber = input("What is the Track Number\n")
        audio["tracknumber"] = NewTrackNumber
        audio.save(v1=0, v2_version=3)
        print(audio)

    elif WhichOne == "Album":

        NewAlbum = input("What is the Album name?\n")
        audio["album"] = NewAlbum
        audio.save(v1=0, v2_version=3)
        print(audio)

    elif WhichOne == "Genre":

        NewGenre = input("What is the Genre?\n")
        audio["genre"] = NewGenre
        audio.save(v1=0, v2_version=3)
        print(audio)
    else:
        print("Invalid Option\n")
        time.sleep(3)
        TagEdit(filepath,audio)

    time.sleep(3)
    if name == 'nt':
        system('cls') # windows clear command
    else:
        system('clear') # linux and unix clear command
    Choice2Exit()
    

TagEdit(filepath, audio)


        