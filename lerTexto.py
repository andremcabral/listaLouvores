from gtts import gTTS
import os
texto='teste de texto'
lingua="pt"
tts=gTTS(texto, lang=lingua)
tts.save('leitura2.mp3')
os.system('ffplay -autoexit -nodisp leitura.mp3')