#!/usr/bin/env python2
"""
Author        :Julio Sanz
Website       :www.elarraydejota.com
Email         :juliojosesb@gmail.com
Description   :Extract mp3 audio from mp4 file
Dependencies  :This script has been written using Python 2.7.9
Usage         :python extract_mp3.py /path/to/file.mp4
Example       :python extract_mp3.py /home/bob/Music/mysong.mp4
License       :GPLv3
"""

import os,sys
from pydub import AudioSegment

orig_file = sys.argv[1]
dest_file = os.path.splitext(sys.argv[1])[0]+'.mp3'

def mp4_extract_mp3():
    AudioSegment.from_file(orig_file).export(dest_file, format="mp3")
    
if __name__ == '__main__':
    mp4_extract_mp3()