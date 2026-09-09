import tkinter as tk
import customtkinter
import keyboard
import time
import winshell
from pynput.mouse import Listener

mouseListener=None

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
    pass

def lockMouse():
    global mouseListener
    mouseListener=Listener(on_click=onClick, suppress=True)
    mouseListener.start()
    mouseButton.configure(text="To unlock mouse, press <Enter>", command=unlockMouse)
    print("EVENT: Locked mouse.")

def unlockMouse(event=None):
    global mouseListener
    if mouseListener and mouseListener.is_alive():
        mouseListener.stop()
        mouseListener=None
    mouseButton.configure(text="Lock Mouse", width=25, command=lockMouse)
    print("EVENT: Unlocked mouse.")

def emptyBin():
    try:
        winshell.recycle_bin().empty(confirm=True, show_progress=False, sound=False)
        # thx g4g
        # https://www.geeksforgeeks.org/python/how-to-empty-recycle-bin-using-python/
        recycleButton.configure(text="Emptied!", width=25, command=print("Emptying bin successful."))
        time.sleep(3)
        recycleButton.configure(text="Empty Recycle Bin", width=25, command=emptyBin, fg_color=("#FF0000", "#8B0000"))
    except:
        recycleButton.configure(text="Already empty!", width=25, command=print("Already empty!"))
        time.sleep(3)
        recycleButton.configure(text="Empty Recycle Bin", width=25, command=emptyBin, fg_color=("#FF0000", "#8B0000"))

def lightToDark():
    customtkinter.set_appearance_mode("dark")
    appearanceButton.configure(text="Switch to light mode", width=25, command=darkToLight)

def darkToLight():
    customtkinter.set_appearance_mode("light")
    appearanceButton.configure(text="Switch to dark mode", width=25, command=lightToDark)

root=customtkinter.CTk()
root.geometry("400x300")
root.bind('<Return>', unlockMouse)

customtkinter.set_default_color_theme("green")
customtkinter.set_appearance_mode("light")

label =tk.Label(root, text="Halt! Input")
label.pack()

keyboardButton=customtkinter.CTkButton(root, text="Halt Input", width=25, command=lockKeyboard)
keyboardButton.pack(padx=20, pady=20)

mouseButton=customtkinter.CTkButton(root, text="Lock Mouse", width=25, command=lockMouse)
mouseButton.pack(padx=20, pady=20)

recycleButton=customtkinter.CTkButton(root, text="Empty Recycle Bin", width=25, command=emptyBin, fg_color=("#FF0000", "#8B0000"))
recycleButton.pack(padx=20, pady=20)

appearanceButton=customtkinter.CTkButton(root, text="Switch to dark mode", width=25, command=lightToDark)
appearanceButton.pack(padx=20, pady=20)

root.mainloop()