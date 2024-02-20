# -*- coding: utf-8 -*-
import pyautogui
import os
import time

class EnviarWhatsapp:

    def mensagem():
        print("Aqui está o seu comprovante, obrigado!")
        

    def abrirWhatsapp(nomeComprovante, numero):        
        pyautogui.PAUSE = 2
        time.sleep(7)
        pyautogui.hotkey("ctrl", "t")
        time.sleep(1)        
        link = "wa.me/" + numero
        pyautogui.write(link)
        pyautogui.press("enter")
        time.sleep(5)        
        #time.sleep(15)

        pyautogui.press("tab")
        time.sleep(0.75)
        pyautogui.press("enter")
        time.sleep(0.75)
        pyautogui.press("tab")
        time.sleep(0.75)
        pyautogui.press("enter")
        time.sleep(0.75)
        pyautogui.press("tab")
        time.sleep(0.75)
        pyautogui.press("tab")
        time.sleep(0.75)
        pyautogui.press("enter")
        time.sleep(12)
        print("Abertura do whatsapp")


        pyautogui.press("tab")
        time.sleep(0.5)

        pyautogui.press("tab")
        time.sleep(0.5)

        pyautogui.press("tab")
        time.sleep(0.5)

        pyautogui.press("tab")
        time.sleep(0.5)

        pyautogui.press("tab")
        time.sleep(0.5)

        pyautogui.press("tab")
        time.sleep(0.5)

        pyautogui.press("tab")
        time.sleep(0.5)

        pyautogui.press("tab")
        time.sleep(0.5)

        pyautogui.press("tab")
        time.sleep(0.5)

        pyautogui.press("tab")
        time.sleep(0.5)

        pyautogui.press("tab")
        time.sleep(0.5)

        pyautogui.press("tab")
        time.sleep(0.5)

        pyautogui.press("tab")
        time.sleep(0.5)

        pyautogui.press("tab")
        time.sleep(0.5)

        pyautogui.press("tab")
        time.sleep(0.5)


        pyautogui.press("enter")
        time.sleep(0.5)

        pyautogui.press("down")
        time.sleep(0.1)

        pyautogui.press("enter")
        time.sleep(2)

        pyautogui.write(nomeComprovante, interval=0.1)
        pyautogui.press("enter")


        pyautogui.write("Seu comprovante, obrigado!", interval=0.1)
        pyautogui.press("enter")

        time.sleep()

        pyautogui.hotkey("ctrl", "w")


