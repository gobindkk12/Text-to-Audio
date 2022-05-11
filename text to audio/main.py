from gtts import gTTS #we have imported module text to speech
import os

myText = "Hello Gobinda How are you I am from Banglore iit HR"

language = 'en'

output = gTTS(text=myText, lang=language,slow=False)

output.save("output.mp3")

os.system("start output.mp3")
