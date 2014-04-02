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
	hmdir = "/usr/share/pocketsphinx/model/hmm/wsj1"
	lmdir = "/usr/share/pocketsphinx/model/lm/wsj/wlist5o.3e-7.vp.tg.lm.DMP"
	dictd = "/usr/share/pocketsphinx/model/lm/wsj/wlist5o.dic"
	speechRec = pocketsphinx.Decoder(hmm = hmdir, lm = lmdir, dict = dictd)
	wavFile = file(WAVE_OUTPUT_FILENAME,'rb')
	speechRec.decode_raw(wavFile)
	result = speechRec.get_hyp()
	print (result)

decode()