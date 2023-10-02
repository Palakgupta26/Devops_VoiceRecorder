import sounddevice as sd
from tkinter import *
import queue
import soundfile as sf
import threading
from tkinter import messagebox
from tkinter import PhotoImage
import time

# Create the main window
voice_rec = Tk()
voice_rec.geometry("2100x750")
voice_rec.title("Voice Recorder")

# Load the background image
bg_image = PhotoImage(file="background.gif")  # Replace with the path to your background image

# Create a Label widget to display the background image
bg_label = Label(voice_rec, image=bg_image)
bg_label.place(relwidth=1, relheight=1)
bg_label.lower()  # Place the label behind other widgets

# Create a queue to contain the audio data
q = queue.Queue()

# Declare variables and initialize them
recording = False
paused = False
file_exists = False

# Function to fit data into the queue
def callback(indata, frames, time, status):
    if not paused:
        q.put(indata.copy())

# Functions to play, stop, record, pause, and resume audio
def threading_rec(x):
    global recording, paused
    if x == 1:
        t1 = threading.Thread(target=record_audio)
        t1.start()
    elif x == 2:
        recording = False
        paused = False
        messagebox.showinfo(message="Recording finished")
    elif x == 3:
        if file_exists:
            data, fs = sf.read("trial.wav", dtype='float32')
            sd.play(data, fs)
            sd.wait()
        else:
            messagebox.showerror(message="Record something to play")
    elif x == 4:
        paused = not paused
        if paused:
            messagebox.showinfo(message="Recording paused")
    elif x == 5:
        paused = False
        messagebox.showinfo(message="Recording resumed")