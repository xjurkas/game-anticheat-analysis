from PIL import ImageGrab
import pyautogui
import time
import random
import keyboard
import tkinter as tk
# Konfiguračné parametre
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x, y = screen_width/2, screen_height/2  # Pozícia na stred obrazovky
activation_key = 'x'  # Kláves, ktorého držanie aktivuje triggerbot
min_delay = 0.05  # Minimálny časový interval v sekundách
max_delay = 0.1  # Maximálny časový interval v sekundách
# Funkcia na získanie farby stredového pixelu
def get_center_pixel_color():
    screenshot = ImageGrab.grab()
    return screenshot.getpixel((x, y))
# Počiatočné získanie referenčnej farby
initial_color = get_center_pixel_color()
print("Triggerbot je pripravený. Držte 'x' na aktiváciu.")
while True: # Nekonečný cyklus na sledovanie farby a simuláciu kliknutia pri držaní klávesu
    if keyboard.is_pressed(activation_key):
        current_color = get_center_pixel_color()
        # Kontrola zmeny farby oproti počiatočnej
        if current_color != initial_color:
            # Generovanie náhodného časového oneskorenia
            delay = random.uniform(min_delay, max_delay)
            time.sleep(delay)  # Čakanie pred simuláciou kliknutia
            pyautogui.leftClick()
            print(f"Výstrel s oneskorením {delay:.2f} sekúnd")
            # Aktualizácia počiatočnej farby po výstrele
            initial_color = current_color
    time.sleep(0.01)
