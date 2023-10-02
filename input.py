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
