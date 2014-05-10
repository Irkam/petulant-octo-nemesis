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
	return out.stdout.read().decode(encoding)