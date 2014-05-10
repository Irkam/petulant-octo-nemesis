import urllib
import urllib.parse
import urllib.request
import time
import os


def speak(text='hello', lang='en', fname='ttsout.wav', player='vlc'):
    """ Send text to Google's text to speech service
    and returns created speech (wav file). """

    if(len(text)<1):
	    return

    limit = min(100, len(text))#100 characters is the current limit.
    text = text[0:limit]
    print("Text to speech:", text)
    values = urllib.parse.urlencode({"q": text, "textlen": len(text), "tl": lang})
    url = "http://translate.google.com/translate_tts?" + values
    print(url)
    hrs = {"User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.63 Safari/535.7"}
    #TODO catch exceptions
    req = urllib.request.Request(url, headers=hrs)
    p = urllib.request.urlopen(req)
    f = open(fname, 'wb')
    f.write(p.read())
    f.close()
    print("Speech saved to:", fname)
    play_wav(fname, player)


def play_wav(filep, player='vlc'):
    print("Playing %s file using %s" % (filep, player))
    os.system(player + " " + filep)


if(__name__ == '__main__'):
    speak("Hello world. The time is %s" % (time.time()))
