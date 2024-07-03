# librarys
import speech_recognition as sr
from datetime import datetime
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random
import os

r = sr.Recognizer()


def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language='tr-TR')
        except sr.UnknownValueError:
            speak("Sizi anlayamadım, lütfen tekrar söyleyebilir misiniz?")
        except sr.RequestError:
            speak("Sistem çalışmıyor. Lütfen daha sonra tekrar deneyiniz.")
        return voice


def response(voice):
    if "nasılsın" in voice:
        speak("İyiyim, teşekkürler. Sen nasılsın?")
    elif "haritaları aç" in voice:
        speak("Haritaları açıyorum.")
        time.sleep(1)
        webbrowser.get().open("https://www.google.com.tr/maps/@39.7681521,30.5163944,15z?hl=tr&authuser=0")
        speak("işte haritalar.")
    elif "hey" in voice:
        speak("hey.")
    elif "ne haber" in voice:
        speak("İyidir,senden?")
    elif "saat kaç" in voice:
        speak(datetime.now().strftime("%H:%M:%S"))
        speak("hey.")
    elif "hava durumu nasıl" in voice:
        hava_url = "https://www.mgm.gov.tr/"
        webbrowser.get().open(hava_url)
        speak("İşte hava durumu")
    elif "arama yap" in voice:
        search = record("ne aramak istiyorsun?")
        url = "https://www.google.com/search?q=" + search
        webbrowser.get().open(url)
        speak(search + " için bulduğum sonuçlar")
    elif "tamamdır" in voice:
        speak("Görüşürüz!")
        time.sleep(1)
        exit()
    elif "teşekkürler" in voice:
        speak("Görüşürüz!")
        time.sleep(1)
        exit()
    elif "bu kadar" in voice:
        speak("Görüşürüz!")
        time.sleep(1)
        exit()
    elif "bu kadardı" in voice:
        speak("Görüşürüz!")
        time.sleep(1)
        exit()
    elif "kapan" in voice:
        speak("Görüşürüz!")
        time.sleep(1)
        exit()


def speak(string):
    tts = gTTS(string, lang='tr')
    rand = random.randint(1, 10000)
    file = 'audio-' + str(rand) + '.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)


speak("Merhaba! Size nasıl yardımcı olabilirim acaba?")
time.sleep(1)
while 1:
    voice = record()
    print(voice)
    response(voice)
