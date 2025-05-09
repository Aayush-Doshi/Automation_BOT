# Discord Pokémeow Auto Catcher Bot

An automated Pokémeow catching assistant using Python, PyAutoGUI, OCR (Tesseract), and screen detection.

---
## ⚠️ Disclaimer
This tool is intended for educational purposes only. Use responsibly and ensure it complies with the terms of service of any platform you're using it on.
---
## 🔍 Features

- Auto-detects Pokémon rarity using Tesseract OCR from the Discord screen.
- Selects the appropriate Pokéball based on rarity.
- Automatically buys more Pokéballs when stock is low.
- Configurable coordinates for each Pokéball.
- Runs in a loop with stop control (`ESC` key).

---

## 🧰 Requirements

- Python 3.7+
- Tesseract-OCR (Install & configure path)
- Python packages:
  ```bash
  pip install pyautogui pillow pytesseract pyperclip keyboard
