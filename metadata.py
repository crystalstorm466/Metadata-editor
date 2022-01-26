from re import U
import unicodedata
import mutagen
from mutagen import *
from mutagen.flac import FLAC
from mutagen.mp3 import MP3
from mutagen.aac import AAC
from mutagen.m4a import M4A
from mutagen.ogg import OggFileType
from mutagen.wave import WAVE
from mutagen.smf import SMF
from os import system, name





print("Welcome to Audio Metadata editor\n")
print("Supported File Types are:\nFlAC, MP3, AAC, M4A, OGG,and WAV\n")
filepath = input("Please provide the file path to your audio file\n")

#this identifes the filetype and opens it, yes I could just use mutagen.File however it does not allow for tag editing
def IdentifyFileType(filepath):

    if filepath.endswith == ".FLAC":
        audio = FLAC(filepath)
        return audio
    elif filepath.endswith == ".Mp3":
        audio = MP3(filepath)
        return audio
    elif filepath.endswith == ".AAC":
        audio = AAC(filepath)
        return audio
    elif filepath.endswith == ".M4A":
        audio = M4A(filepath)
        return audio
    elif filepath.endswith == ".OGG":
        audio = OggFileType(filepath)
        return audio
    elif filepath.endswith == ".WAV":
        audio = WAVE(filepath)
        return audio

audio = IdentifyFileType(filepath)

WhichOne = input("What tag do you want to edit in the file?\nTitle\nArtist\nTrack Number\nAlbum\nGenre\n")
print("The answer is " + WhichOne)
if name == 'nt':
    system('cls') # windows clear command
else:
    system('clear') # linux and unix clear command
if WhichOne == "Title":
    NewTitle = input("What is the new title?\n")
    audio["title"] = [NewTitle] #mutagen.TextFrame(encoding=3, text=[NewTitle]) 
    print(audio)
    print("The new title is: " + audio["title"])
    mutagen.save(audio)
elif WhichOne == "Artist":
    NewArtist = input("What is the new Artist?")
    audio["artist"] = NewArtist
    print("The new Artist is: " + audio["artist"])
    mutagen.save(audio)
elif WhichOne == "TrackNumber" or "Track Number":
    NewTrackNumber = input("What is the Track Number")
    audio["tracknumber"] = NewTrackNumber
    print("The new Track Number is: " + audio["tracknumber"])
    mutagen.save(audio)




