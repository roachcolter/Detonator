import urllib.request
import sys
import time
from os import system

def typewriter2(any):
    for char in (any):  
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)

def typewriter(any):
    for char in (any):  
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.001)

signal = str("SENDING SIGNAL! " * 112)

system('clear')

deto = ["detonator.txt"]
frames=[]
for name in deto:
    with open(name,"r",encoding="utf8") as f:
        frames.append(f.readlines())
for i in range(1):
    for frame in frames:
        typewriter("".join(frame))
        time.sleep(0.0000001)
print("\n")
typewriter("===================")
typewriter2("\nMade by roachcolter")
typewriter("\n===================\n")
time.sleep(1)

root_url = ("http://"+(input(str("\nMasukkan IP : "))))
print("===================")
print(root_url)
print("===================")
def sendRequest(url):
    n = urllib.request.urlopen(url)

def a():
    sendRequest(root_url+"/ledon")
def b():
    sendRequest(root_url+"/ledoff")
def c():
    sendRequest(root_url+"/buz1")
def d():
    sendRequest(root_url+"/buz2")
def e():
    sendRequest(root_url+"/buz3")
def f():
    sendRequest(root_url+"/buz4")

def detonator():
    x = input(str("Command : "))
    if x == ("send on signal request") :
        y = input("Key to send signal : ")
        if y == ("2461reload"):
            system('clear')
            print("10")
            d()
            time.sleep(0.5)
            d()
            time.sleep(0.5)
            print("9")
            d()
            time.sleep(0.5)
            d()
            time.sleep(0.5)
            print("8")
            d()
            time.sleep(0.5)
            d()
            time.sleep(0.25)
            e()
            time.sleep(0.25)
            print("7")
            e()
            time.sleep(0.25)
            e()
            time.sleep(0.25)
            e()
            time.sleep(0.25)
            e()
            time.sleep(0.25)
            e()
            print("6")
            time.sleep(0.25)
            e()
            time.sleep(0.25)
            e()
            time.sleep(0.25)
            e()
            time.sleep(0.25)
            print("5")
            e()
            time.sleep(0.25)
            e()
            time.sleep(0.25)
            e()
            time.sleep(0.25)
            e()
            time.sleep(0.25)
            print("4")
            e()
            time.sleep(0.25)
            e()
            time.sleep(0.25)
            e()
            time.sleep(0.25)
            system('clear')
            typewriter2("DETONATING")
            f()
            time.sleep(3)
            system('clear')
            b()
            typewriter(signal)
            time.sleep(10)
            system('clear')
            detonator()

        else :
            print("Key is wrong!")
            detonator()
    if x == ("turn off") :
        a()
        time.sleep(3)
        detonator()
    
    if x == ("test") :
        c()
        c()
        c()
        c()
        c()
        o = int(input("How long : "))
        b()
        time.sleep(o)
        a()
        detonator()

detonator()
