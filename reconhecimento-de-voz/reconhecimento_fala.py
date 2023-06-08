import speech_recognition as sr
import pyaudio

recog = sr.Recognizer()

with sr.Microphone(1) as mic:
    recog.adjust_for_ambient_noise(mic)
    print("Pode me dizer que eu irei transcrever!")
    audio = recog.listen(mic)
    texto = recog.recognize_google(audio, language="pt-BR")
    print(texto)