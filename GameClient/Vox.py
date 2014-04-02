import pyaudio
import wave
import sys
import pocketsphinx

import recording


CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
WAVE_OUTPUT_FILENAME = "output.wav"

def decode():
	recording.record()
	speechRec = pocketsphinx.Decoder()
	wavFile = file(WAVE_OUTPUT_FILENAME,'rb')
	speechRec.decode_raw(wavFile)
	result = speechRec.get_hyp()
	print (result)
