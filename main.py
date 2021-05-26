from time import sleep
import os,sys,platform

_file,cl  = sys.argv[1]," "
_speed = sys.argv[2]

if(platform.system() == "Linux"): cl = "clear"
elif(platform.system() == "Windows"): cl = "cls"

def readFromFile(file,speed=1):
    f = open(file,'r')
    for l in f:
            w = str.split(l," ")
            for i in w:
                os.system(cl)
                print(i)
                sleep(speed)
            
readFromFile(_file,float(_speed))