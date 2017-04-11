#!/usr/bin/env python2
"""
Author        :Julio Sanz
Website       :www.elarraydejota.com
Email         :juliojosesb@gmail.com
Description   :Convert mp3 audio file to ogg
Dependencies  :This script has been written using Python 2.7.9
Usage         :python mp3_to_ogg.py /path/to/file.mp3
Example       :python mp3_to_ogg.py /home/bob/Music/mysong.mp3
License       :GPLv3
"""

import os,sys
from pydub import AudioSegment

orig_song = sys.argv[1]
dest_song = os.path.splitext(sys.argv[1])[0]+'.ogg'

def convert_mp3_to_ogg():
    song = AudioSegment.from_mp3(orig_song)
    song.export(dest_song, format="ogg")
    
if __name__ == '__main__':
    convert_mp3_to_ogg()