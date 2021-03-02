import ctypes
import sys
import tkinter as tk


def keep_display_on():
    print("Staying ON")
    ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)


def kill_prog():
    ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)
    sys.exit(0)


settings = tk.Tk()
settings.geometry("200x60")
settings.title("Manage Display")
frame = tk.Frame(settings)
frame.pack()

button1 = tk.Button(frame, text="Quit", fg="red", command=kill_prog)
button1.pack(side=tk.LEFT)

button2 = tk.Button(frame, text="STAY ON", command=keep_display_on)
button2.pack(side=tk.LEFT)


settings.mainloop()
