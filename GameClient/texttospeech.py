import urllib
import urllib.parse
import urllib.request
import time
import os


def speak(text='hello', lang='en', fname='ttsout', player='play -q'):
    """ Send text to Google's text to speech service
    and returns created speech (wav file). """

    if(len(text)<1):
        return
    i = 0
    j = 0
    words = text.split(" ")
    while i < len(words):
        sentence = ""
        while i < len(words) and len(sentence) + len(words[i]) < 100:
                sentence += words[i] + " "
                i+= 1
        
        print(sentence)
        values = urllib.parse.urlencode({"q": sentence, "textlen": len(sentence), "tl": lang})
        url = "http://translate.google.com/translate_tts?" + values
        #print(url)
        hrs = {"User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.63 Safari/535.7"}
        #TODO catch exceptions
        req = urllib.request.Request(url, headers=hrs)
        p = urllib.request.urlopen(req)
        f = open(fname + str(j) + ".mp3", 'wb')
        f.write(p.read())
        f.close()
        j += 1
    #print("Speech saved to:", fname)
    k = 0;
    catstr = "cat "
    while k < j:
        catstr += fname + str(k) + ".mp3 "
        k += 1
    catstr += "> " + fname + ".mp3"
    os.system(catstr)
    os.system("lame --quiet --decode " + fname +".mp3 " + fname + ".wav")
    play_wav(fname, player)
        


def play_wav(filep, player='play -q'):
    #print("Playing %s file using %s" % (filep, player))
    return os.system(player + " " + filep + ".wav")


if(__name__ == '__main__'):
    speak("Hello world. The time is %s" % (time.time()))
