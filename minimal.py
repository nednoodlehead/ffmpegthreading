import threading

import pydub
import time
import pydub.playback

def dosomething():
    print("Hello!")
    time.sleep(15)
    print('hi!')

def thr():
    thread = threading.Thread(target=play)
    thread.start()

def main_occupy_thr():
    thread = threading.Thread(target=dosomething)
    thread.start()


def play():
    x = pydub.AudioSegment.from_file("./audio/Ghais Guevara - This Ski Mask Ain't For COVIDcASilnJR_aI.mp3")
    pydub.playback.play(x)
    time.sleep(50)
main_occupy_thr()
time.sleep(2)
thr()
