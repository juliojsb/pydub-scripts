#!/usr/bin/env python2
"""
Author        :Julio Sanz
Website       :www.elarraydejota.com
Email         :juliojosesb@gmail.com
Description   :Python script to play audio with pydub
Dependencies  :This scrip has been written using Python 2.7.9
Usage         :python playsong.py /path/to/song
Example       :python playsong.py /home/user/Music/example.mp3
License       :GPLv3
"""

from pydub import AudioSegment
from pydub.playback import play
import sys
import os

song = sys.argv[1]
extension = os.path.basename(song)

def playsong(song):
    if extension.endswith('.wav'):
        song = AudioSegment.from_wav(song)
        play(song)
    elif extension.endswith('.mp3'):
        song = AudioSegment.from_mp3(song)
        play(song)
    elif extension.endswith('.ogg'):
        song = AudioSegment.from_ogg(song)
        play(song)
    
if __name__ == '__main__':
    playsong(song)