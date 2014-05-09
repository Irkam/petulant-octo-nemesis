#!/usr/bin/python
import sys
import urllib2
import json
import os
from subprocess import *
import locale
try:
    filename = sys.argv[1]
except IndexError:
    print 'Usage: transcribe.py <file>'
    sys.exit(1)


encoding = locale.getdefaultlocale()[1]
cmd = "curl -X POST --data-binary @'" + filename +"' --header 'Content-Type: audio/x-flac; rate=16000;' 'https://www.google.com/speech-api/v2/recognize?output=json&lang=fr-fr&key=AIzaSyCnl6MRydhw_5fLXIdASxkLJzcJh5iX0M4'| tail --lines=-1 - > out.json"
os.system(cmd)
req = Popen(["cat", "out.json"], stdout=PIPE);
#os.system("cat out.json")
resp = req.stdout.read().decode(encoding).split('"')

#print resp
#print json.loads(json.dumps(resp))
#text = json.loads(json.dumps(resp))['result']['alternative'][0]['transcript']
text=resp[7]
#os.system("rm out.json")
print text.encode(encoding) 