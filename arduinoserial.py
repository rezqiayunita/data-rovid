from email.headerregistry import HeaderRegistry
from struct import pack
from cv2 import split
import keyboard
from matplotlib import test
from numpy import integer
import serial.tools.list_ports
import pyttsx3

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

# voice
engine = pyttsx3.init()
#rate 
rate = engine.getProperty("rate")
engine.setProperty("rate",150)
#print(rate)

#volume 
volume = engine.getProperty("volume")
engine.setProperty("volume",1)
#print("volume is {0}".format(volume))

#male female voices
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id) # for windows

def talk(text):
    engine.say(text)
    engine.runAndWait()

portList = []

serialInst.baudrate = 9600
serialInst.port = "COM6"
serialInst.open()

def Convert(string):
    li = list(string.split(","))
    return li

while True :
    while serialInst.in_waiting:
        pass
        packet = serialInst.readline().decode('utf-8')
        a = packet.strip('\r\n')
        splitpacket = a.split(",")
        # print(splitpacket)
        x = (splitpacket[0])
        print(packet)
        # y = (splitpacket[1])
        # z = (splitpacket[2])
        # print("X= ", x, "Y= ", y, "Z= ", z)
        # print("Y= ", y)
        # print("Z= ", z)

        # test = Convert(packet)
        # ambient,object = test
        # # print(test)
        # print(object)
        # # print(cek)

        # talk(f"good morning adam")
        # talk(f"this is the data of your medical check up")
        # talk(f"your body temperature {object} celcius")  
        # if packet.strip() == "A":
        #         print("itworks")
        # if keyboard.is_pressed('esc'):
        #         break

# import serial
# from struct import *
# import sys
# import time
# import random
# import ast


# try:
#     ser=serial.Serial(baudrate='9600', timeout=.5, port='COM6')
# except:
#     print('Port open error')

# time.sleep(5)#no delete!
# while True:
#     try:
#         ser.write(pack ('15h',0,1,2,3,4,666,6,7,444,9,10,2222,12,13,random.randint(0,100)))#the 15h is 15 element, and h is an int type data
#                                                                     #random test, that whether data is updated
#         time.sleep(.01)#delay
#         dat=ser.readline()#read a line data
        
#         if dat!=b''and dat!=b'\r\n':
#             try:                #convert in list type the readed data
#                 dats=str(dat)
#                 dat1=dats.replace("b","")
#                 dat2=dat1.replace("'",'')
#                 dat3=dat2[:-4]
#                 list_=ast.literal_eval(dat3) #list_ value can you use in program
#                 print(dat3)
#             except:
#                 print('Error in corvert, readed: ', dats)
#         time.sleep(.05)
#     except KeyboardInterrupt:
#         break
#     except:
#         print(str(sys.exc_info())) #print error
#         break