# -*- mode: python -*-
import sys
sys.setrecursionlimit(5000)
block_cipher = None
import pyautogui 
import keyboard 
import asyncio
import tkinter as tk
from tkinter import ttk
from tkinter import * 
import threading
import multiprocessing
import time 
import os
import psutil
global iteration
iteration = 0

def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;
def main(iteration):
    while keyboard.is_pressed('end') == False:
        def okey():
            ok = pyautogui.locateOnScreen('assets/ok.jpg', grayscale=True, confidence=0.92)
            if  ok != None:
                pyautogui.leftClick(ok)
                time.sleep(0.25)
        def okey1():
            ok1 = pyautogui.locateOnScreen('assets/ok1.jpg', grayscale=True, confidence=0.92)
            if  ok1 != None:
                pyautogui.leftClick(ok1)
                time.sleep(0.25)
        def useit():
            use = pyautogui.locateOnScreen('assets/use.jpg', grayscale=True, confidence=0.85)
            if  use != None:
                pyautogui.leftClick(use)
                time.sleep(0.25)
        def takeit():
            take = pyautogui.locateOnScreen('assets/take.jpg', grayscale=True, confidence=0.92)
            if  take != None:
                pyautogui.leftClick(take)
                time.sleep(0.25)
                return True
        if checkIfProcessRunning('wolfteam.bin'):
            pass
        else:
            var2.set("Oyununuz Açık Değil!")
        useit()
        okey()
        var.set(f"Açılan Kutu Sayısı: {iteration}")
        if  takeit() == True:
            iteration += 1
            var.set(f"Açılan Kutu Sayısı: {iteration}")
            var1.set("Durum : Kutu Açılıyor!")
        else:
            var1.set(f"Durum: Kutu Bekleniyor...")
        okey1()
            
def starter(iteration):
    while True:
        if keyboard.is_pressed('f1'):
            if checkIfProcessRunning('wolfteam.bin'):
                var2.set("TAMAM!")
                main(iteration)
            else:
                var2.set("Uyarı: Oyununuz Açık Değil!")
            
root = Tk()
root.resizable(0, 0)
var = StringVar()
var1 = StringVar()
var2 = StringVar()
root.geometry('400x150')
root.iconbitmap('assets/favicon.ico')
root.configure(background='#F0F8FF')
root.title('WT BOX OPENER')
Label(root, text='Başlatmak İçin \'F1\' Tuşuna Basın.', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=12, y=14)
Label(root, text='Kapatmak İçin \'END\' Tuşuna Basın.', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=12, y=34)
Label(root, textvariable=var, bg='#F0F8FF', foreground="green",font=('arial', 12, 'normal')).place(x=12, y=54)
Label(root, textvariable=var1, bg='#F0F8FF', foreground="blue",font=('arial', 12, 'normal')).place(x=12, y=74)
Label(root, textvariable=var2, bg='#F0F8FF', foreground="red", font=('arial', 12, 'normal')).place(x=12, y=94)
x = threading.Thread(target=starter,args=[iteration])
x.start()
root.mainloop()
