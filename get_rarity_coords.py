import pyautogui
import time

print("Move your mouse to top-left and bottom-right of the rarity box.")
time.sleep(3)

print("Top-left:")
time.sleep(2)
print(pyautogui.position())

time.sleep(3)
print("Bottom-right:")
time.sleep(2)
print(pyautogui.position())
