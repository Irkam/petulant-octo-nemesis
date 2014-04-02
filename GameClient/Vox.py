import pyaudio
import wave
import sys
import pocketsphinx

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
WAVE_OUTPUT_FILENAME = "output.wav"

def record(seconds):
	p = pyaudio.PyAudio()
	stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True,frames_per_buffer=CHUNK)
	frames = []
	for i in range(0, int(RATE / CHUNK * seconds)):
		data = stream.read(CHUNK)
		frames.append(data)
	stream.stop_stream()
	stream.close()
	p.terminate()
	
def decode():
	record(5)
	speechRec = pocketsphinx.Decoder(hmm = hmdir, lm = lmdir, dict = dictd)
	wavFile = file(WAVE_OUTPUT_FILENAME,'rb')
	speechRec.decode_raw(wavFile)
	result = speechRec.get_hyp()
	print result