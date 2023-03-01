import pyscreenshot as ImageGrab
import numpy as np

import pyautogui
import time

time.sleep(1)
px = 0
pyautogui.hotkey("alt","tab")
time.sleep(1)
image = ImageGrab.grab().load()
imageArray = np.asanyarray(image)
px = image[620,265]
print(px)
pyautogui.hotkey("alt","tab")