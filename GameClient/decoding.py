#import pocketsphinx
#def decode(wavInputFile, hmmdir = None, lmdir = None, dictdir = None):
#	speechRec = pocketsphinx.Decoder()
#	speechRec.decode_raw(wavInputFile)
#	result = speechRec.get_hyp()
#	return result

from subprocess import *
import locale
import sys
import urllib
import json
import os
from subprocess import *

encoding = locale.getdefaultlocale()[1]

hmdir = "/usr/local/bin/pocketsphinx-0.8/model/hmm/fr_FR/"
lmd = "/usr/local/bin/pocketsphinx-0.8/model/lm/fr_FR/french3g62K.lm.dmp"
dictd = "/usr/local/bin/pocketsphinx-0.8/model/lm/fr_FR/frenchWords62K.dic"

def decode(filename):
    f = open(filename,'rb')
    flac_cont = f.read()
    f.close()

    #post it
    lang_code='fr-fr'
    googl_speech_url = 'https://www.google.com/speech-api/v2/recognize?output=json&lang=%s&key=AIzaSyCnl6MRydhw_5fLXIdASxkLJzcJh5iX0M4'%(lang_code)
    hrs = {"User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.63 Safari/535.7",'Content-type': 'audio/x-flac; rate=16000'}
    req = urllib.request.Request(googl_speech_url, data=flac_cont, headers=hrs)
    p = urllib.request.urlopen(req)
    r = json.loads(p.read().decode('utf-8').split('\n')[1])
    #r=eval(p.read())['hypotheses']
    #rep=r[0]
    #rep=rep.get('utterance')
    rep = r['result'][0]['alternative'][0]['transcript']
    
    if rep=="":
        rep="pas compris"
    map(os.remove, (filename+'.flac', filename+'.wav'))
    print("rep="+str(rep))
    return rep
