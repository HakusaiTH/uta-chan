import speech_recognition as sr 
import pygame

all_music = ["ippo.mp3","overlap.mp3","my way.mp3","hekireki.mp3"]	

pygame.init()
pygame.mixer.init()

def open_music(x) :
	print(x)
	pygame.mixer.music.load(f'{all_music[x]}')
	pygame.mixer.music.play()	

def main() :
	print("main")
	r1 = sr.Recognizer()
	op = 0
	while True :
		with sr.Microphone() as source:
			audio = r1.record(source, duration=3)
			try:			
				text = r1.recognize_google(audio, language="th")
				if "เปิด" in text:
					open_music(0)
				if "ทดสอบ" in text:
					pygame.mixer.music.stop()
				if "ต่อไป" in text :
					op = op + 1
					if(op > len(all_music)) : op = len(all_music)
					open_music(op)				
				if "ก่อนหน้า" in text :
					op = op - 1
					if(op < len(all_music)) : op = 0
					open_music(op)
			except:
				text = "ระบบผิดพลาด"

if __name__ == '__main__':
	main()

#cd \miniproject_python\uta chan> uta.py