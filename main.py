import tkinter as tk
import customtkinter
import keyboard
import time
import winshell
import subprocess
import ctypes
import sys
import os
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
    time.sleep(1)
    os.startfile("explorer.exe")
    print("Restarted.")

# when run as admin explorer.exe does not launch, must be launched as standard user
#def updateWinget():
#    command="winget update --all"
#    subprocess.run(f'start cmd /k "{command}"', shell=True)
#    print("EVENT: Attempt winget update execution successful.")

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
customtkinter.set_appearance_mode("dark")

label=customtkinter.CTkLabel(root, text="Halt! Input", font=("Impact", 50, "bold"))
label.pack(pady=30)

appearanceLabel=customtkinter.CTkLabel(root, text="Halt! Input Appearence", font=("Impact", 25, "normal"))
appearanceLabel.pack()

appearanceButton=customtkinter.CTkButton(root, text="Switch to light mode", width=25, command=darkToLight)
appearanceButton.pack(pady=15)


inputLabel=customtkinter.CTkLabel(root, text="Input Blocking", font=("Impact", 25, "normal"))
inputLabel.pack()

keyboardButton=customtkinter.CTkButton(root, text="Halt! Keyboard Blocking", width=25, command=lockKeyboard)
keyboardButton.pack(pady=15)

mouseButton=customtkinter.CTkButton(root, text="Halt! Mouse Blocking", width=25, command=lockMouse)
mouseButton.pack(pady=15)


cmdLabel=customtkinter.CTkLabel(root, text="Command Prompt Speed-dial", font=("Impact", 25, "normal"))
cmdLabel.pack()

updateWingetButton=customtkinter.CTkButton(root, text="Update Winget packages", width=25, command=updateWinget)
updateWingetButton.pack(pady=15)

flushDNSButton=customtkinter.CTkButton(root, text="Flush DNS", width=25, command=flushDNS)
flushDNSButton.pack(pady=15)

clearClipboardButton=customtkinter.CTkButton(root, text="Clear clipboard", width=25, command=clearClipboard)
clearClipboardButton.pack(pady=15)

batteryReportButton=customtkinter.CTkButton(root, text="Generate battery report (if applicable)", width=25, command=batteryReport)
batteryReportButton.pack(pady=15)

dismButton=customtkinter.CTkButton(root, text="Check for and repair damaged system files (DISM)", width=25, command=dism)
dismButton.pack(pady=15)

sfcButton=customtkinter.CTkButton(root, text="Check for and repair critical system files (sfc)", width=25, command=sfcScan)
sfcButton.pack(pady=15)

chkdskButton=customtkinter.CTkButton(root, text="Check drive for and repair bad sectors/errors (chkdsk)", width=25, command=chkdsk)
chkdskButton.pack(pady=15)


funLabel=customtkinter.CTkLabel(root, text="Fun", font=("Impact", 25, "normal"))
funLabel.pack()

parrotButton=customtkinter.CTkButton(root, text="Parrot", width=25, command=parrot)
parrotButton.pack(pady=15)

rickrollButton=customtkinter.CTkButton(root, text="Mystery Button", width=25, command=rickroll)
rickrollButton.pack(pady=15)



dangerLabel=customtkinter.CTkLabel(root, text="(Kind of) Dangerous actions", font=("Impact", 25, "normal"))
dangerLabel.pack()

recycleButton=customtkinter.CTkButton(root, text="Empty Recycle Bin", width=25, command=emptyBin, fg_color=("#FF0000", "#8B0000"))
recycleButton.pack(pady=15)

#restartExplorerButton=customtkinter.CTkButton(root, text="Restart Windows Explorer", width=25, command=restartExplorer, fg_color=("#FF0000", "#8B0000"))
#restartExplorerButton.pack(pady=15)

root.mainloop()