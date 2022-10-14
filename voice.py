# from openpyxl.workbook import Workbook
# from openpyxl import load_workbook
# from pygame import mixer
# import num2words
# import time
# import pygame
# import os

# input = int(input("Masukkan nama pasien :"))

# wb = load_workbook('data pasien.xlsx')
# ws = wb.active

# name = ws["F2"].value
# temperature = ws["B2"].value
# heartrate = ws["A2"].value
# systole = ws["C2"].value 
# diastole = ws["D2"].value

# SuhuBadan = temperature
# Nama = input
# text1 = num2words.num2words(SuhuBadan, lang='id')
# fullSentence = f"suhu badan anda adalah {text1} derajat celcius"

# sistol = systole
# diastol = diastole
# text2 = num2words.num2words(sistol, lang='id')
# text3 = num2words.num2words(diastol, lang='id')
# fullSentence = f"tekanan darah anda adalah {text2} per {text3}"

# DetakJantung = heartrate
# text4 = num2words.num2words(DetakJantung, lang='id')
# fullSentence = f"detak jantung anda adalah {text4} bpm"

# words = text1.split(" ")

# words1 = text2.split(" ")

# words2 = text3.split(" ")

# words3 = text4.split(" ")

# mixer.init()

# mixer.music.load('Selamat Datang.mp3')
# mixer.music.play()
# time.sleep(2.5)

# mixer.music.load('Suhu badan anda adalah.mp3')
# mixer.music.play()
# time.sleep(2.5)

 
# for word in words:
#     print(word.capitalize())
#     mixer.music.load(f'{word.capitalize()}.mp3')
#     mixer.music.play()
#     time.sleep(1)

# mixer.music.load('derajat celcius.mp3')
# mixer.music.play()
# time.sleep(3)

# mixer.music.load('Tekanan darah anda adalah.mp3')
# mixer.music.play()
# time.sleep(2.5)

# for word in words1:
#     print(word.capitalize())
#     mixer.music.load(f'{word.capitalize()}.mp3')
#     mixer.music.play()
#     time.sleep(1)

# for word in words2:
#     print(word.capitalize())
#     mixer.music.load(f'{word.capitalize()}.mp3')
#     mixer.music.play()
#     time.sleep(1)


# mixer.music.load('Detak jantung anda adalah.mp3')
# mixer.music.play()
# time.sleep(2.5)

# for word in words3:
#     print(word.capitalize())
#     mixer.music.load(f'{word.capitalize()}.mp3')
#     mixer.music.play()
#     time.sleep(1)
    
# mixer.music.load('bpm.mp3')
# mixer.music.play()
# time.sleep(3)

# for i in range(0,10):
#     print(i)

from gtts import gTTS
from io import BytesIO
import pygame

def tts(text):
    mp3_fp = BytesIO()
    tts = gTTS(text, lang ="id")
    tts.write_to_fp(mp3_fp)
    
    return mp3_fp

def speak(text):
    pygame.init()
    pygame.mixer.init()
    sound = tts(text)
    sound.seek(0)
    pygame.mixer.music.load(sound,"mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(1)

speak("selamat pagi")
speak("berikut adalah data medical checkup anda")
speak("tekanan darah anda adalah")