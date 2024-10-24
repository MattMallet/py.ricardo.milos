# import time
#
# import pyautogui
#
# time.sleep(5)
# print(pyautogui.position())

import pyautogui
import time

pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")
pyautogui.press("F11")

pyautogui.click(x=376, y=284)

pyautogui.write("https://i.kym-cdn.com/photos/images/original/001/479/169/c57.gif")
pyautogui.press("enter")
