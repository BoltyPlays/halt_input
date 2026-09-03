import tkinter as tk
import keyboard

def lockKeyboard():
    for keys in range(200):
        keyboard.block_key(keys)
        button.configure(text = "Unblock input", command=unlockKeyboard)

def unlockKeyboard():
    for keys in range(200):
        keyboard.unblock_key(keys)
        button.configure(text = "Halt input", command=lockKeyboard)

root=tk.Tk()
label =tk.Label(root, text="Halt! Input")
label.pack()

button = tk.Button(root, text="Halt Input", width=25, command=lockKeyboard)
button.pack()

root.mainloop()