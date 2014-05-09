import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SEC = 5
WAVE_OUTPUT_FILENAME = "output.wav"

def openRecordStream(pyaudiohandler):
	stream = pyaudiohandler.open(format = FORMAT,
			channels = CHANNELS,
			rate = RATE,
			input = True,
			frames_per_buffer = CHUNK)
	return stream

def closeRecordStream(stream):
	stream.stop_stream()
	stream.close()

def writeWAV(wavefilename, pyaudiohandler, frames):
	wf = wave.open(wavefilename, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(pyaudiohandler.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))
	wf.close()


import os
def record(outputfilename):
	#out = Popen(["rm", outputfilename, "_"+outputfilename])
	#out.
	#out = Popen(["rec", "_"+outputfilename, " rate 16k silence 1 0.1 3% 1 3.0 3%"])
	#out.wait()
	os.system("rm " + outputfilename)
	cmd = "rec --rate 16k " + outputfilename + " silence 1 0.2 1% 1 1.0 2%"
	print(cmd)
	os.system(cmd)