import keyboard
import time
import pyautogui
import string
import random
EsetDownloadLink = "https://proxy.eset.com/li-handler/?branch=sk&prod=essp&transaction_id=odcm_download|ggl|sk|oksewyl51fpqmz7h1y181ig7dk91k6i5kdw42utf3zgdoxkdlon14aodav12iadaz7pid"



#----------------------------------------------------------------------------------------------
# Odinstalovanie esetu
#----------------------------------------------------------------------------------------------
def EsetUninstall(lang): 

    keyboard.press_and_release('windows')

    time.sleep(delay)
    if lang.lower() == 'en':
        keyboard.write("Apps & features")

    
    if lang.lower() == 'sk':
       keyboard.write("Aplikácie a súčasti")

    time.sleep(delay)
    keyboard.press_and_release('enter')

    #---------------------------------------
    # Vyhladanie Esetu
    #---------------------------------------
    time.sleep(6)
    i=0
    while i < 3:
        time.sleep(1)
        keyboard.press_and_release('tab')
        i += 1

    time.sleep(delay)
    keyboard.write("Eset")
    #---------------------------------------


    #---------------------------------------
    # Otvorenie Esetu a spustenie procesu odinstalovania
    #---------------------------------------

    x=0
    while x < 3:
        time.sleep(delay)
        keyboard.press_and_release('tab')
        x += 1
    
    time.sleep(delay)
    keyboard.press_and_release('enter')

    time.sleep(delay)
    keyboard.press_and_release('tab')

    time.sleep(delay)
    keyboard.press_and_release('enter')

    print("Eset open")

    time.sleep(delay)
    keyboard.press_and_release('enter')

    time.sleep(delay)
    keyboard.press_and_release('tab')

    time.sleep(delay)
    keyboard.press_and_release('enter')

    #---------------------------------------
    # Odinstalovanie Esetu
    #---------------------------------------
    time.sleep(4)

    time.sleep(delay)
    keyboard.press_and_release('tab')

    time.sleep(delay)
    keyboard.press_and_release('enter')

    time.sleep(delay)
    while True:
        if pyautogui.locateOnScreen('Uninstalled.png', confidence = 0.7):
            break
    #---------------------------------------


    #---------------------------------------
    # Final touches
    #---------------------------------------
    time.sleep(delay)
    keyboard.press_and_release('enter')

    time.sleep(delay)
    keyboard.press_and_release('tab')

    time.sleep(delay)
    keyboard.press_and_release('enter')
    #---------------------------------------


#-----------------------------------------------
#               Odinstalovane
#-----------------------------------------------



#----------------------------------------------------------------------------------------------
# Instalacia Esetu
#----------------------------------------------------------------------------------------------
def EsetInstall(lang):
    
    #---------------------------------------
    # Otvorenie Chromu
    #---------------------------------------

    keyboard.press_and_release('windows')

    time.sleep(delay)
    keyboard.write("chrome")

    time.sleep(delay)
    keyboard.press_and_release('enter')
    #---------------------------------------


    #---------------------------------------
    # Input field v chrome
    #---------------------------------------
    time.sleep(delay)
    while True:
        if pyautogui.locateOnScreen('TuHladajPole.png'):
            time.sleep(delay)
            pyautogui.click('TuHladajPole.png')
            break
    #---------------------------------------


    #---------------------------------------
    # Download instaleru
    #---------------------------------------
    time.sleep(delay)
    keyboard.write(EsetDownloadLink)
    keyboard.press_and_release('enter')
    #---------------------------------------


    #---------------------------------------
    # Otvorenie instaleru
    #---------------------------------------
    time.sleep(delay)
    pyautogui.keyDown('ctrl')
    keyboard.press_and_release('j')
    pyautogui.keyUp('ctrl')
    
    time.sleep(delay)
    keyboard.press_and_release('tab')

    time.sleep(delay)
    keyboard.press_and_release('tab')

    time.sleep(delay)
    keyboard.press_and_release('enter')
    #---------------------------------------


    #---------------------------------------
    # Instaler
    #---------------------------------------
    time.sleep(delay)
    pyautogui.keyDown("shift")
    pyautogui.press("tab")

    time.sleep(delay)
    pyautogui.keyUp("shift")

    time.sleep(delay)
    keyboard.press_and_release('enter')
    #---------------------------------------


    #-------------------------------------
    #             UAC :(
    #-------------------------------------

    time.sleep(delay)
    while True:
        if pyautogui.locateOnScreen('InstallBegin.png'):
            time.sleep(delay)
            break

    keyboard.press_and_release("tab")

    time.sleep(delay)
    keyboard.press_and_release("tab")

    time.sleep(delay)
    keyboard.press_and_release("tab")

    time.sleep(delay)
    keyboard.press_and_release('enter')

    time.sleep(delay)
    keyboard.press_and_release("tab")

    time.sleep(delay)
    keyboard.press_and_release("tab")

    time.sleep(delay)
    keyboard.press_and_release('enter')

    time.sleep(delay)
    while True:
        if pyautogui.locateOnScreen('LogIn.png'):
            time.sleep(delay)
            break
    
    while True:
        if pyautogui.locateOnScreen('skipLogin.png'):
            time.sleep(delay)
            pyautogui.click('skipLogin.png')
            break

    i = 0
    while i < 3:
        time.sleep(delay)
        keyboard.press_and_release('tab')
        i += 1
    
    time.sleep(delay)
    keyboard.press_and_release('enter')
    

    while True:
        time.sleep(delay)
        letters = string.ascii_letters
        fakeMailPartOne = ( ''.join(random.choice(letters) for i in range(10)))
        fakeMailPartTwo = ( ''.join(random.choice(letters) for i in range(5)))

        with open('usedMails.txt') as f:
            if fakeMailPartOne not in f.read():
                if fakeMailPartTwo not in f.read():
                    f.close()
                    break
        
    f = open("usedMails.txt", "a")
    f.write('\n')
    f.write(f'{fakeMailPartOne}:{fakeMailPartTwo}')
    f.close()


    time.sleep(delay)
    keyboard.press_and_release('tab')

    time.sleep(delay)
    keyboard.write(fakeMailPartOne + '@' + fakeMailPartTwo + '.com')

    time.sleep(delay)
    keyboard.press_and_release('tab')

    time.sleep(delay)
    keyboard.write(fakeMailPartOne + '@' + fakeMailPartTwo + '.com')

    
    i = 0
    while i < 4:
        time.sleep(delay)
        keyboard.press_and_release('tab')
        i += 1
    
    time.sleep(delay)
    keyboard.press_and_release('enter')

    time.sleep(delay)
    keyboard.press_and_release('tab')
    
    time.sleep(delay)
    keyboard.press_and_release('enter')

    i = 0
    while i < 5:
        time.sleep(delay)
        keyboard.press_and_release('tab')
        i += 1

    time.sleep(delay)
    keyboard.press_and_release('enter')

    time.sleep(delay)
    while True:
        if pyautogui.locateOnScreen('Installed.png'):
            time.sleep(delay)
            break

    i = 0
    while i < 5:
        time.sleep(delay)
        keyboard.press_and_release('tab')
        i += 1

    time.sleep(delay)
    keyboard.press_and_release('enter')

#-----------------------------------------------
#               Nainstalovane
#-----------------------------------------------


delay = 2

#----------------------------------------------------------------------------------------------
# User inputy
#----------------------------------------------------------------------------------------------

#---------------------------------------
# Vyber jazyka
#---------------------------------------
print("System Language/Jazyk systemu")
while True:
    lang = input("EN/SK?: ")

    while lang.lower() not in ('en', 'sk'):
        lang = input('EN/SK?: ')
    
    if lang.lower() in ('en', 'sk'):
        break
#---------------------------------------

if lang.lower() == 'en':
    print('Please save all your work and close all running programs')
    print('')


elif lang.lower() == 'sk':
    print('Prosim ulozte si vsetku pracu a zatvorte beziace programy')
    print('')


#---------------------------------------
# Co sa ma robit
#---------------------------------------
print("Uninstall - 1")
print("Install - 2")
while True:
    WhatToDo = input("Input 1 or 2: ")

    while WhatToDo not in ('1', '2'):
        answer = input('1 or 2: ')
    
    if WhatToDo in ('1', '2'):
        break

if WhatToDo == '1':
    UninstallBool = True
    InstallBool = False

elif WhatToDo == '2':
    InstallBool = True
    UninstallBool = False
#---------------------------------------

if UninstallBool == True:
    EsetUninstall(lang)

elif InstallBool == True:
    EsetInstall(lang)