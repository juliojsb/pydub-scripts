#!/usr/bin/env python2
"""
Author        :Julio Sanz
Website       :www.elarraydejota.com
Email         :juliojosesb@gmail.com
Description   :Convert ogg audio file to mp3
Dependencies  :This script has been written using Python 2.7.9
Usage         :python ogg_to_mp3.py /path/to/file.ogg
Example       :python ogg_to_mp3.py /home/bob/Music/mysong.ogg
License       :GPLv3
"""

import os,sys
from pydub import AudioSegment

orig_song = sys.argv[1]
dest_song = os.path.splitext(sys.argv[1])[0]+'.mp3'

def convert_ogg_to_mp3():
    song = AudioSegment.from_ogg(orig_song)
    song.export(dest_song, format="mp3")
    
if __name__ == '__main__':
    convert_ogg_to_mp3()