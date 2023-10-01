import sounddevice as sd
from tkinter import *
import queue
import soundfile as sf
import threading
from tkinter import messagebox
from tkinter import PhotoImage

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
# Recording function
def record_audio():
    global recording
    recording = True
    global file_exists
    messagebox.showinfo(message="Recording Audio. Speak into the microphone.")
    with sf.SoundFile("trial.wav", mode='w', samplerate=44100, channels=2) as file:
        with sd.InputStream(samplerate=44100, channels=2, callback=callback):
            while recording:
                file_exists = True
                file.write(q.get())

# Label to display the app title
title_lbl = Label(voice_rec, text="Voice Recorder", font=("Arial", 26, "bold"),bg="#FFFFFF", fg="Black")
title_lbl.grid(row=0, column=0, columnspan=5, pady=10)

# Buttons with improved style
record_btn = Button(voice_rec, text="Record", command=lambda m=1: threading_rec(m), bg="#FFFFFF", fg="Black", font=("Times", 20))
stop_btn = Button(voice_rec, text="Stop", command=lambda m=2: threading_rec(m), bg="#FFFFFF", fg="Black", font=("Times", 20))
play_btn = Button(voice_rec, text="Play", command=lambda m=3: threading_rec(m), bg="#FFFFFF", fg="Black", font=("Times", 20))
pause_btn = Button(voice_rec, text="Pause", command=lambda m=4: threading_rec(m), bg="#FFFFFF", fg="Black", font=("Times", 20))
resume_btn = Button(voice_rec, text="Resume", command=lambda m=5: threading_rec(m), bg="#FFFFFF", fg="Black", font=("Times", 20))

record_btn.grid(row=1, column=0, padx=85, pady=85)
stop_btn.grid(row=1, column=1, padx=85, pady=85)
play_btn.grid(row=1, column=2, padx=125, pady=90)
pause_btn.grid(row=1, column=3, padx=85, pady=85)
resume_btn.grid(row=1, column=4, padx=85, pady=85)

# Start the Tkinter main loop
voice_rec.mainloop()
