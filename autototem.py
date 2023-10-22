from pynput.keyboard import Key, Listener
import pyautogui
import keyboard
import os

script_directory = os.path.dirname(os.path.abspath(__file__))
settings_file = os.path.join(script_directory, 'settings.txt')
settings = {}

with open(settings_file, 'r') as file:
    for line in file:
        line = line.strip()
        if line:
            key, value = line.split('=')
            settings[key] = value

totem_keybind = settings.get('totem_keybind')
open_inventory_keybind = settings.get('open_inventory_keybind')

print("Auto totem is ready! Don't close this window until you are done playing :)")

def autoTotem():
    empty_offhand = os.path.join(script_directory, 'empty_offhand.png')
    totem = os.path.join(script_directory, 'totem.png')

    pyautogui.moveTo(200, 200)
    offhandlocation = pyautogui.locateOnScreen(empty_offhand)
    if offhandlocation is not None:
        location = pyautogui.locateOnScreen(totem)
        if location is not None:
            x, y = pyautogui.center(location)
            pyautogui.moveTo(x, y)
            keyboard.press(totem_keybind)

def keyPress(key):
    if key == open_inventory_keybind:
        autoTotem()

with Listener(on_press=keyPress) as listener:
    listener.join()