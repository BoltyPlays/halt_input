import tkinter as tk
import customtkinter
import keyboard
import time
import winshell
import subprocess
import ctypes
import sys
from ctypes import windll
from pynput.mouse import Listener

mouseListener=None

# note: use PyInstaller with --uac-admin

def lockKeyboard():
    for keys in range(200):
        keyboard.block_key(keys)
    keyboardButton.configure(text="Unblock input", command=unlockKeyboard)
    mouseButton.configure(text="Not usable when keyboard is locked.", command=print("hello"))
    print("EVENT: Locked keyboard.")

def unlockKeyboard():
    for keys in range(200):
        try:
            keyboard.unblock_key(keys)
        except KeyError:
            pass
    keyboardButton.configure(text="Halt input", command=lockKeyboard)
    mouseButton.configure(text="Lock Mouse", width=25, command=lockMouse)

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
    winshell.recycle_bin().empty(confirm=True, show_progress=False, sound=False)
        # thx g4g
        # https://www.geeksforgeeks.org/python/how-to-empty-recycle-bin-using-python/
    recycleButton.configure(text="Empty Recycle Bin", width=25, command=emptyBin, fg_color=("#FF0000", "#8B0000"))
    print("EVENT: Emptied Recycle Bin.")

def lightToDark():
    customtkinter.set_appearance_mode("dark")
    appearanceButton.configure(text="Switch to light mode", width=25, command=darkToLight)
    print("EVENT: Day to night.")

def darkToLight():
    customtkinter.set_appearance_mode("light")
    appearanceButton.configure(text="Switch to dark mode", width=25, command=lightToDark)
    print("EVENT: Night to day.")

def restartExplorer():
    restart=subprocess.run(["taskkill", "/f", "/im", "explorer.exe"])
    time.sleep(0.1)
    subprocess.Popen(["explorer.exe"], shell=True)
    print("Restarted.")

def updateWinget():
    command="winget update --all"
    subprocess.run(f'start cmd /k "{command}"', shell=True)
    print("EVENT: Attempt winget update execution successful.")

def flushDNS():
    command="ipconfig /flushdns"
    subprocess.run(f'start cmd /k "{command}"', shell=True)
    print("EVENT: Attempt flushdns execution successful.")

def clearClipboard():
    if windll.user32.OpenClipboard(None):
        windll.user32.EmptyClipboard()
        windll.user32.CloseClipboard()
    # https://stackoverflow.com/questions/9123090/clear-clipboard
    print("EVENT: Clipboard cleared.")

def parrot():
    command="curl parrot.live"
    subprocess.run(f'start cmd /k "{command}"', shell=True)
    print("EVENT: parrot")

def batteryReport():
    command="powercfg /batteryreport"
    subprocess.run(f'start cmd /k "{command}"', shell=True)
    print("EVENT: Attempt report generation successful.")

def rickroll():
    command="curl ascii.live/rick"
    subprocess.run(f'start cmd /k "{command}"', shell=True)
    print("EVENT: hahaha")

def dism():
    command="DISM /Online /CLeanup-Image /RestoreHealth"
    subprocess.run(f'start cmd /k "{command}"', shell=True)
    print("EVENT: Attempt dism execution successful.")

def sfcScan():
    command="sfc /scannow"
    subprocess.run(f'start cmd /k "{command}"', shell=True)
    print("EVENT: Attempt sfc execution successful.")

def chkdsk():
    command="chkdsk /f /r"
    subprocess.run(f'start cmd /k "{command}"', shell=True)
    print("EVENT: Attempt chkdsk execution successful.")

root=customtkinter.CTk()
root.geometry("400x1000")
root.bind('<Return>', unlockMouse)

customtkinter.set_default_color_theme("green")
customtkinter.set_appearance_mode("light")

label=customtkinter.CTkLabel(root, text="Halt! Input")
label.pack()

keyboardButton=customtkinter.CTkButton(root, text="Halt Input", width=25, command=lockKeyboard)
keyboardButton.pack(padx=20, pady=20)

mouseButton=customtkinter.CTkButton(root, text="Lock Mouse", width=25, command=lockMouse)
mouseButton.pack(padx=20, pady=20)

recycleButton=customtkinter.CTkButton(root, text="Empty Recycle Bin", width=25, command=emptyBin, fg_color=("#FF0000", "#8B0000"))
recycleButton.pack(padx=20, pady=20)

appearanceButton=customtkinter.CTkButton(root, text="Switch to dark mode", width=25, command=lightToDark)
appearanceButton.pack(padx=20, pady=20)

restartExplorerButton=customtkinter.CTkButton(root, text="Restart Windows Explorer", width=25, command=restartExplorer)
restartExplorerButton.pack(padx=20, pady=20)

updateWingetButton=customtkinter.CTkButton(root, text="Update Winget packages", width=25, command=updateWinget)
updateWingetButton.pack(padx=20, pady=20)

flushDNSButton=customtkinter.CTkButton(root, text="Flush DNS", width=25, command=flushDNS)
flushDNSButton.pack(padx=20, pady=20)

clearClipboardButton=customtkinter.CTkButton(root, text="Clear clipboard", width=25, command=clearClipboard)
clearClipboardButton.pack(padx=20, pady=20)

batteryReportButton=customtkinter.CTkButton(root, text="Generate battery report (if applicable)", width=25, command=batteryReport)
batteryReportButton.pack(padx=20, pady=20)

parrotButton=customtkinter.CTkButton(root, text="Parrot", width=25, command=parrot)
parrotButton.pack(padx=20, pady=20)

rickrollButton=customtkinter.CTkButton(root, text="Mystery Button", width=25, command=rickroll)
rickrollButton.pack(padx=20, pady=20)

dismButton=customtkinter.CTkButton(root, text="Check for and repair damaged system files (DISM)", width=25, command=dism)
dismButton.pack(padx=20, pady=20)

sfcButton=customtkinter.CTkButton(root, text="Check for and repair critical system files (sfc)", width=25, command=sfcScan)
sfcButton.pack(padx=20, pady=20)

chkdskButton=customtkinter.CTkButton(root, text="Check drive for and repair bad sectors/errors (chkdsk)", width=25, command=chkdsk)
chkdskButton.pack(padx=20, pady=20)

root.mainloop()