import tkinter as tk
import threading
import time
import pydub
import pydub.playback

def cmd():
    print("begin!")
    time.sleep(1)
    print("end!")

def play():
    x = pydub.AudioSegment.from_file("./audio/Ghais Guevara - This Ski Mask Ain't For COVIDcASilnJR_aI.mp3")
    pydub.playback.play(x)
    time.sleep(50)

def invoke_thr_regular():
    thr = threading.Thread(target=cmd)
    thr.start()

def invoke_thr_ffmpeg():
    thr = threading.Thread(target=play)
    thr.start()


root = tk.Tk()
root.geometry("500x500")
root.configure(background="#2b2b1c")
tk.Label(root, text="Main Page!").pack()
tk.Button(root, command=invoke_thr_regular, text='non-ffmpeg test').pack()
tk.Button(root, command=invoke_thr_ffmpeg, text='(it is very loud btw, use volume mixer. turn down)').pack()


root.mainloop()