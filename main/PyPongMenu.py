import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

def file_exists_or_error(filepath):
    if not os.path.isfile(filepath):
        messagebox.showerror("File Not Found", f"Cannot find file:\n{filepath}")
        return False
    return True

def launch_single_player():
    filepath = os.path.join(os.path.dirname(__file__), "PyPong1Player.py")
    if file_exists_or_error(filepath):
        root.destroy()
        subprocess.run([sys.executable, filepath])

def launch_two_player():
    filepath = os.path.join(os.path.dirname(__file__), "PyPong2Player.py")
    if file_exists_or_error(filepath):
        root.destroy()
        subprocess.run([sys.executable, filepath])

root = tk.Tk()
root.title("PyPong Menu")
root.geometry("300x200")

label = tk.Label(root, text="Welcome to PyPong!", font=("Arial", 18))
label.pack(pady=20)

single_btn = tk.Button(root, text="Single Player (AI)", font=("Arial", 14), command=launch_single_player)
single_btn.pack(pady=10)

two_btn = tk.Button(root, text="2 Player", font=("Arial", 14), command=launch_two_player)
two_btn.pack(pady=10)

root.mainloop()