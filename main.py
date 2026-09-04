import tkinter as tk
import keyboard
import time
from pynput.mouse import Listener

def lockKeyboard():
    for keys in range(200):
        keyboard.block_key(keys)
    keyboardButton.configure(text="Unblock input", command=unlockKeyboard)
    print("EVENT: Locked keyboard.")

def unlockKeyboard():
    for keys in range(200):
        try:
            keyboard.unblock_key(keys)
        except KeyError:
            pass
    keyboardButton.configure(text="Halt input", command=lockKeyboard)
    print("EVENT: Unlocked Keyboard.")

def onClick(x, y, button, pressed):
    return False

def lockMouse():
    global mouseListener
    mouseListener=Listener(on_click=onClick, suppress=True)
    mouseListener.start()
    mouseButton.configure(text="To unlock mouse, press <Enter> or <Return>", command=unlockMouse)
    print("EVENT: Locked mouse.")

def unlockMouse(event=None):
    global mouseListener
    if mouseListener and mouseListener.is_alive():
        mouseListener.stop()
        mouseListener=None
    mouseButton.configure(text="Lock Mouse", width=25, command=lockMouse)
    print("EVENT: Unlocked mouse.")

root=tk.Tk()
root.bind('<Return>', unlockMouse)

label =tk.Label(root, text="Halt! Input")
label.pack()

keyboardButton = tk.Button(root, text="Halt Input", width=25, command=lockKeyboard)
keyboardButton.pack()

mouseButton = tk.Button(root, text="Lock Mouse", width=25, command=lockMouse)
mouseButton.pack()

root.mainloop()