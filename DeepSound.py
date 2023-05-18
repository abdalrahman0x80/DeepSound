from gtts import gTTS
text ="hello world"
lang = "en"
obj = gTTS(text=text,lang=lang,slow=False).save("code.mp3")