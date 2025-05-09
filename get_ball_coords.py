import pyautogui
import time

balls = ["Pokéball", "Greatball", "Ultraball", "Masterball"]
for ball in balls:
    print(f"Hover your mouse on the {ball} button...")
    time.sleep(5)
    print(f"{ball} position:", pyautogui.position())
