from gtts import gTTS
import subprocess

mytext = 'Opened in a new tab.'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)  
myobj.save("welcome.mp3") 
subprocess.call(['afplay','welcome.mp3'])