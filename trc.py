# Copyright 2012 Nexiwave Canada. All rights reserved.
# Nexiwave Canada PROPRIETARY/CONFIDENTIAL. Use is subject to license terms.

import sys, os, json, urllib2, urllib, time

# You will need python-requests package. It makes things much easier.
import requests

# Change these:
# Login details:
USERNAME = "hashjith@gmail.com"
PASSWORD = "BXUSTSAPXF595KW"

def transcribe_audio_file(filename):
    """Transcribe an audio file using Nexiwave"""
    url = 'https://api.nexiwave.com/SpeechIndexing/file/storage/' + USERNAME +'/recording/?authData.passwd=' + PASSWORD + '&auto-redirect=true&response=application/json'

    # To receive transcript in plain text, instead of html format, comment this line out (for SMS, for example)
    #url = url + '&transcriptFormat=html'


    # Ready to send:
    sys.stderr.write("Send audio for transcript with " + url + "\n")
    r = requests.post(url, files={'mediaFileData': open(filename,'rb')})
    data = r.json()
    transcript = data['text']
    foo = data['text']
    f = open('newf.txt', 'w')
    f.write(foo)
    f.close()    
    # Perform your magic here:
    print "Transcript for "+filename+"=" + transcript


if __name__ == '__main__':
    # Change this to your own
    filename = "/home/hashin/mini/message.wav"
    
    transcribe_audio_file(filename)

#foo = + transcript 
#f = open('newf.txt', 'w')
#f.write(foo)
#f.close()
#text_file = open("newf.txt", "w")
#text_file.write("%s" % transcript)
#text_file.close()
#file = open("newf.txt", "w")
#file.write( + transcript ) 
#file.close()
