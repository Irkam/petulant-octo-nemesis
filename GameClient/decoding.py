#import pocketsphinx
#def decode(wavInputFile, hmmdir = None, lmdir = None, dictdir = None):
#	speechRec = pocketsphinx.Decoder()
#	speechRec.decode_raw(wavInputFile)
#	result = speechRec.get_hyp()
#	return result

from subprocess import *
import locale

encoding = locale.getdefaultlocale()[1]
hmdir = "/usr/local/bin/pocketsphinx-0.8/model/hmm/fr_FR/"
lmd = "/usr/local/bin/pocketsphinx-0.8/model/lm/fr_FR/french3g62K.lm.dmp"
dictd = "/usr/local/bin/pocketsphinx-0.8/model/lm/fr_FR/frenchWords62K.dic"

def decode (flacInutFile):
	out = Popen(["./transcribe", flacInutFile], stdout=PIPE)
	#out = Popen(["curl", "-X","POST","--data-binary @'output.flac'", "--header 'Content-Type: audio/x-flac; rate=16000;'","'https://www.google.com/speech-api/v2/recognize?output=json&lang=fr-fr&key=AIzaSyCnl6MRydhw_5fLXIdASxkLJzcJh5iX0M4' | tail --lines=+2 - ], stdout = PIPE)
	return out.stdout.read().decode(encoding)