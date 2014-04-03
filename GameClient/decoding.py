import pocketsphinx

def decode(wavInputFile, hmmdir = None, lmdir = None, dictdir = None):
	speechRec = pocketsphinx.Decoder()
	speechRec.decode_raw(wavInputFile)
	result = speechRec.get_hyp()
	print(result)
	
