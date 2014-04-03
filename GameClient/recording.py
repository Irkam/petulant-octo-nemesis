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

def record(outputfilename):
	p = pyaudio.PyAudio()
	stream = openRecordStream(pyaudiohandler = p)
	
	frames = []
	
	for i in range(0, (RATE/CHUNK * RECORD_SEC)):
		data = stream.read(CHUNK)
		frames.append(data)
	
	closeRecordStream(stream)
	p.terminate()
	
	writeWAV(outputfilename, p, frames)
