import pocketsphinx

import recording
import decoding

recording.record('output.wav')
decoding.decode(file('output.wav', 'rb'))
