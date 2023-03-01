from math import floor
import os
import pyscreenshot as takeScreenshot

import time, pyautogui

from random import randint
from datetime import datetime

workCount = 0
positionToClick = (0, 0)
numberOfAccounts = 3

def getTimeNow():
    timeNow = datetime.now()
    return timeNow.strftime("%H:%M:%S")

def getMinutesNow():
    timeNow = getTimeNow()
    minutesNow = int(timeNow[3:5])
    return minutesNow

def comparingPixelColor(colorRGB, positionToCompare):
    image = takeScreenshot.grab().load()
    px = image[positionToCompare]
    del image
    return (px == colorRGB)

def altTab(numberOfAccounts):
    pyautogui.keyDown('alt')
    time.sleep(0.4)
    pyautogui.press('tab', presses = numberOfAccounts - 1, interval=0.2)
    time.sleep(0.4)
    pyautogui.keyUp('alt')
    time.sleep(0.4)
    return 0

# def altTabCtrlShiftReload(numberOfAccounts):
#     for account in range(numberOfAccounts):
#         altTab(numberOfAccounts)
#         pyautogui.hotkey('ctrl','r')
#         time.sleep(0.5)
#     return 0

def altTabClick(numberOfAccounts, clicks=1):
    for account in range(numberOfAccounts - 1):
        pyautogui.click(clicks = clicks, interval = 0.5)
        altTab(numberOfAccounts)
        time.sleep(0.5)
    altTab(numberOfAccounts)
    time.sleep(1)
    return 0

def getWhiteError():
    if (comparingPixelColor((255, 255, 255), (45, 400))):
        print("White error at", getTimeNow())
    return (comparingPixelColor((255, 255, 255), (45, 400)))

def makeClick(colorRGB, positionToCompare, positionToClick, message, minutesWhenCalled, numberOfAccounts):
    print(message)

    while(not (comparingPixelColor(colorRGB, positionToCompare))):
        print("Waiting for the condition to match:", message)        
        if(abs(getMinutesNow() - minutesWhenCalled) >= 2):
            for item in range(numberOfAccounts):
                pyautogui.hotkey('ctrl','w')
                time.sleep(1)
            gameRoutine(numberOfAccounts)
        time.sleep(1)

    if(comparingPixelColor(colorRGB, positionToCompare)):
        if(abs(getMinutesNow() - minutesWhenCalled) >= 2):
            for item in range(numberOfAccounts):
                pyautogui.hotkey('ctrl','w')
                time.sleep(1)
            gameRoutine(numberOfAccounts)
        pyautogui.click(positionToClick)
        time.sleep(1)

    # Redundance to make sure
    
    while(comparingPixelColor(colorRGB, positionToCompare)):
        if(abs(getMinutesNow() - minutesWhenCalled) >= 2):
            for item in range(numberOfAccounts):
                pyautogui.hotkey('ctrl','w')
                time.sleep(1)
            gameRoutine(numberOfAccounts)
        pyautogui.click(positionToClick)
        time.sleep(1)
        
    print("Done")
    return 0

def connect(message, numberOfAccounts):
    # Reloading and Clicking Connect
    time.sleep(2)
    for item in range(numberOfAccounts):
        pyautogui.write('https://app.bombcrypto.io')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(1)
        altTab()
        time.sleep(1)
    altTab()
    colorRGB = (255, 103, 0)
    positionToCompare = (620 + adjustValueX, 570 + adjustValueY)
    x = randint(560 + adjustValueX, 780 + adjustValueX)
    y = randint(575 + adjustValueY, 630 + adjustValueY)
    positionToClick = (x + adjustValueX, y + adjustValueY)
    makeClick(colorRGB, positionToCompare, positionToClick, message, getMinutesNow())
    del colorRGB
    del positionToCompare
    del x
    del y
    del positionToClick
    return 0

def login(message, numberOfAccounts):
    # Clicking Login Button
    colorRGB = (240, 212, 156)
    positionToCompare = (630 + adjustValueX, 445 + adjustValueY)
    x = randint(615 + adjustValueX, 720 + adjustValueX)
    y = randint(445 + adjustValueY, 475 + adjustValueY)
    positionToClick = (x + adjustValueX, y + adjustValueY)
    makeClick(colorRGB, positionToCompare, positionToClick, message, getMinutesNow(), numberOfAccounts)
    del colorRGB
    del positionToCompare
    del x
    del y
    return positionToClick

def enterGame(message, positionToClick, numberOfAccounts):
    # Entering The Game
    colorRGB = (122, 191, 255)
    positionToCompare = (600 + adjustValueX, 630 + adjustValueY)
    makeClick(colorRGB, positionToCompare, positionToClick, message, getMinutesNow(), numberOfAccounts)
    print('Game Entered')
    return colorRGB, positionToCompare
	
def compareCorrectlyEntered(message, positionToClick, colorRGB, positionToCompare):
    # Comparing if the game correctly entered
    while(comparingPixelColor(colorRGB, positionToCompare)):
        pyautogui.click()
        time.sleep(1)
    print('Game entered correctly')
    return 0
    
def upHeroesMenu(message, numberOfAccounts):
    # Up Heroes Menu
    positionToClick = (670,690)
    pyautogui.click(positionToClick)
    time.sleep(2)
    colorRGB = (248, 228, 192)
    positionToCompare = (780 + adjustValueX, 670 + adjustValueY)
    makeClick(colorRGB, positionToCompare, positionToClick, message, getMinutesNow(), numberOfAccounts)
    del positionToClick
    del colorRGB
    del positionToCompare
    return 0
    
def makeAllWork(message, numberOfAccounts):
    # Making all workcolorRGB, positionToCompare
    colorRGB = (235,182,164)
    positionToCompare = (615 + adjustValueX, 310 + adjustValueY)
    positionToClick = positionToCompare
    while(not comparingPixelColor(colorRGB, positionToCompare)):
        pyautogui.click(positionToClick)
        time.sleep(1)
    del colorRGB
    del positionToCompare
    del positionToClick
    return 0

def clickXButton(message):
    # Clicking the x Button multiple times to get back to the game
    pyautogui.click(720,265, clicks=6, interval = 0.5)
    print(message)
    return 0

def gameRoutine(numberOfAccounts):
    time.sleep(1)
    pyautogui.keyDown('ctrl')
    pyautogui.press('w',presses = 3, interval = 0.5)
    pyautogui.keyUp('ctrl')
    for item in range(numberOfAccounts):
        time.sleep(2)
        chromeClicks = [(595,340),(770,340),(940,340)]
        pyautogui.press('win')
        time.sleep(1)
        pyautogui.write('chrome')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(chromeClicks[item])
        time.sleep(2)
    altTab()
    connect("Reloading and Clicking Connect", numberOfAccounts)
    positionToClick = login("Clicking Login Button", numberOfAccounts)
    colorRGB, positionToCompare = enterGame("Trying to enter the Game", positionToClick)
    compareCorrectlyEntered("Comparing if the game correctly entered", positionToClick, colorRGB, positionToCompare)
    del positionToClick
    del colorRGB
    del positionToCompare
    upHeroesMenu("Up Heroes Menu")
    makeAllWork("Making all work")
    clickXButton("Clicking X Button")
    print("Put to Work done on all accounts")
    return getTimeNow()

adjustValueX = 0
adjustValueY = 0

time.sleep(1)

lastTimeWorked = 0
errorCount = 0
# actualAccount = 0
numberOfAccounts = 3
# moduleNumber = 60 / numberOfAccounts
# actualAccount = int(floor(getMinutesNow() / moduleNumber))
# if (moduleNumber < 10):
#     moduleNumber = 10

while(True):
    # Waiting For An Hour to Pass Before Continue
    while(getMinutesNow() != 0):
        print("Waiting five seconds to see if an hour passed at",  getTimeNow(),"and worked", workCount, "times")
        print("Last time worked at", lastTimeWorked, "with", errorCount, "errors")
        time.sleep(5)
        
        if(getWhiteError()):
            # Double check for error
            if(getWhiteError()):
                lastTimeWorked = gameRoutine(numberOfAccounts)
                errorCount += 1
    
    lastTimeWorked = gameRoutine((numberOfAccounts))
    workCount += 1
    time.sleep(60)

# Modelo para uma conta por vez
# while(True):
#     # Waiting For An Hour to Pass Before Continue
#     while(getMinutesNow() != 6):
#         print("Waiting five seconds to see if an hour passed at",  getTimeNow(),"and worked", int ((workCount + numberOfAccounts - 1)/ 3), "times")
#         print("Last time worked at", lastTimeWorked, "with", errorCount, "errors")
#         time.sleep(5)
        
#         if(getWhiteError()):
#             # Double check for error
#             if(getWhiteError()):
#                 lastTimeWorked = gameRoutine((actualAccount))
#                 errorCount += 1
    
#     actualAccount = int(floor(getMinutesNow() / moduleNumber))
#     if(actualAccount >= numberOfAccounts):
#         actualAccount = 0
#     lastTimeWorked = gameRoutine((actualAccount))
#     if(actualAccount >= numberOfAccounts):
#         actualAccount = 0
#     workCount += 1
#     time.sleep(60)
