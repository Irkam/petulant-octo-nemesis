import pocketsphinx

DEFAULT_WAV_FILE = "output.wav"

def decode(wavInputFile = file(DEFAULT_WAV_FILE, 'rb')):
	speechRec = pocketsphinx.Decoder()
	speechRec.decode_raw(wavInputFile)
	result = speechRec.get_hyp()
	print(result)
	
