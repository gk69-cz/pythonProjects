import os
import playsound
from googletrans import Translator
from gtts import gTTS
import speech_recognition as sr
from google_trans_new import google_translator
from translate import Translator

r= sr.Recognizer()
translator = google_translator()


with sr.Microphone() as source:
    print("please speak")
    audio = r.listen(source)
    try:
        speech_Text = r.recognize_google(audio);
        print(speech_Text)
    except sr.UnknownValueError:
        print('couldnt understand')
    except sr.RequestError:
        print('couldnt get results')
    except:
        print("error")
    
    from_language = 'english'
    to_language='french'
        
    translator= Translator(from_lang=from_language,to_lang=to_language)
    translation = translator.translate(speech_Text)

    print (translation)
    
    voice= gTTS(translation,lang='hi')
    voice.save('voice.mp3')
        