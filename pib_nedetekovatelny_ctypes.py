import ctypes
import time
import random
import keyboard
import tkinter as tk
from PIL import ImageGrab
root = tk.Tk() # Konfiguračné parameter
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x, y = int(screen_width / 2), int(screen_height / 2)
activation_key = 'x'
min_delay = 0.05
max_delay = 0.1
MOUSEEVENTF_LEFTDOWN = 0x0002    # Konštanty pre kliknutie myši
MOUSEEVENTF_LEFTUP = 0x0004
def click():  # Funkcia pre simuláciu kliknutia myši pomocou WinAPI
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(0.01)  # Krátke oneskorenie na simuláciu realistického kliknutia
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
def get_center_pixel_color():  # Funkcia na získanie farby stredového pixelu
    screenshot = ImageGrab.grab()
    return screenshot.getpixel((x, y))
initial_color = get_center_pixel_color()# Počiatočné získanie referenčnej farby
print("Triggerbot je pripravený. Držte 'x' na aktiváciu.")
while True: # Nekonečný cyklus na sledovanie farby a simuláciu kliknutia pri držaní klávesu
    if keyboard.is_pressed(activation_key):
        current_color = get_center_pixel_color()
        if current_color != initial_color:          # Kontrola zmeny farby oproti počiatočnej
            delay = random.uniform(min_delay, max_delay)
            time.sleep(delay)
            click()
            print(f"Výstrel s oneskorením {delay:.2f} sekúnd")
            initial_color = current_color              # Aktualizácia počiatočnej farby po výstrele
            time.sleep(5)
    time.sleep(0.01)
