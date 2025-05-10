def get_rarity_from_screen():
    return "common"

import re
import pyautogui
import time
import pyperclip
import keyboard
import json
import os
from PIL import ImageGrab
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


COORDS_FILE = "ball_coords.json"

def get_or_load_ball_coords():
    coord_file = "ball_coords.json"
    if os.path.exists(coord_file):
        with open(coord_file, "r") as f:
            return json.load(f)

    coords = {}
    print("We'll now collect coordinates for each Pokéball type.")
    time.sleep(1)

    for rarity in ["common", "rare", "ultra-rare", "other"]:
        print(f"Hover over the button you want to use for: {rarity.upper()} and press Enter...")
        input()
        coords[rarity] = pyautogui.position()
        print(f"{rarity} position saved:", coords[rarity])

    coords["uncommon"] = coords["common"]

    with open(coord_file, "w") as f:
        json.dump(coords, f)

    return coords

BALL_CHECK_BOX = (540, 700, 1020, 860)  # Try widening and adjusting height

def extract_ball_count(text, ball_type):
    # Clean the text to fix common OCR issues
    text = text.lower()
    text = text.replace("\n", " ").replace(":", "").replace("|", "l").replace("ba11s", "balls").replace("ba1ls", "balls")

    # Define flexible regex patterns for each type
    patterns = {
        "pokeballs": [r"poke[\s\-]*balls?\s*(\d+)"],
        "greatballs": [r"great[\s\-]*balls?\s*(\d+)"],
        "ultraballs": [r"ultra[\s\-]*balls?\s*(\d+)", r"ultraball\s*(\d+)"]
    }

    for pattern in patterns.get(ball_type, []):
        match = re.search(pattern, text)
        if match:
            return int(match.group(1))

    return 0  # Return 0 if not found



def check_and_buy_balls():
    screenshot = ImageGrab.grab(bbox=BALL_CHECK_BOX)
    text = pytesseract.image_to_string(screenshot).lower()

    # Clean OCR text
    text = text.replace("\n", " ").replace(":", "").replace("|", "l").replace("ba11s", "balls").replace("ba1ls", "balls")

    print(f"[DEBUG] Ball Count OCR Text:\n{text}\n")

    # Only proceed if ALL relevant keywords are found
    keywords = ["pokeball", "greatball", "ultraball", "poke ball", "great ball", "ultra ball"]
    if not any(k in text for k in keywords):
        print("No ball-related keywords found. Skipping buy check.")
        return

    # Proceed with extraction
    poke_count = extract_ball_count(text, "pokeballs")
    great_count = extract_ball_count(text, "greatballs")
    ultra_count = extract_ball_count(text, "ultraballs")

    print(f"Counts - Pokeballs: {poke_count}, Greatballs: {great_count}, Ultraballs: {ultra_count}")

    if "pokeball" in text and poke_count <= 5:
        print("No Pokeballs found. Buying 30...")
        pyautogui.typewrite(";s b 1 30")
        pyautogui.press("enter")
        time.sleep(5)

    if "greatball" in text and great_count <= 5:
        print("No GreatBalls found. Buying 20...")
        pyautogui.typewrite(";s b 2 20")
        pyautogui.press("enter")
        time.sleep(5)

    if "ultraball" in text and ultra_count <= 5:
        print("No UltraBalls found. Buying 10...")
        pyautogui.typewrite(";s b 3 10")
        pyautogui.press("enter")
        time.sleep(5)

  
RARITY_BOX = (566, 415, 999, 852)

def get_rarity_from_screen():
    screenshot = ImageGrab.grab(bbox=RARITY_BOX)
    text = pytesseract.image_to_string(screenshot).lower()
    print(f"OCR Text: {text}")

    if "shiny" in text or "legendary" in text:
        return "masterball"
    elif "super rare" in text:
        return "ultraball"
    elif "rare" in text:
        return "greatball"
    elif "uncommon" in text:
        return "pokeball"
    elif "common" in text:
        return "pokeball"
    else:
        return "default"

def main():
    coords = get_or_load_ball_coords()
    print("Running auto catcher... Press ESC to stop.")

    try:
        while True:
            check_and_buy_balls()
            
            pyautogui.typewrite(";p")
            pyautogui.press("enter")

            time.sleep(6)

            pyautogui.hotkey("ctrl", "c")
            time.sleep(0.5)

            rarity = get_rarity_from_screen()
            print(f"Ball to use:-{rarity}")
            if rarity not in coords:
                print(f"Unknown rarity '{rarity}', using 'common' as fallback.")
                rarity = "common"

            x, y = coords[rarity]
            pyautogui.moveTo(x, y, duration=0.3)
            pyautogui.click()

            wait_time = 5 + int(10 * time.time()) % 11
            time.sleep(wait_time)

            if keyboard.is_pressed('esc'):
                print("Stopped by user.")
                break
    except KeyboardInterrupt:
        print("Stopped manually.")

if __name__ == "__main__":
    main()
