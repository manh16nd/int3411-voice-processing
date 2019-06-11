import speech_recognition as sr
from underthesea import classify
import glob

print(sr.__version__)
r = sr.Recognizer()

def recognition(filename):
	for file in glob.glob("upload/sound.wav"):
		wav_file = sr.AudioFile(file)
		
		try: 
			with wav_file as source:
				audio = r.record(source)
				text = r.recognize_google(audio, language="vi-VN")
				print(text)
				return(text)
		except:
			return "Unrecognize"
			
