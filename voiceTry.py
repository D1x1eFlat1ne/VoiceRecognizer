import tkinter as tk
import speech_recognition as sr
import threading

r = sr.Recognizer()

def audioRecord():
    with sr.Microphone() as source:
        print("Listening")

        #adjust for ambient noise
        r.adjust_for_ambient_noise(source)

        try:
            #listen to audio
            audio = r.listen(source)
            print("processing")

            #Google service to convert to audio
            query = r.recognize_google(audio)
            print(f"You said: {query}")
        except sr.UnknownValueError:
            print("Sorry, I did not get that.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

def startListeningThreaded():
    #Start the thread
    threading.Thread(target=audioRecord).start()

root = tk.Tk()
root.title("Voice Assistant")

voiceButton = tk.Button(
    root,
    text = "Press button to speak",
    command=startListeningThreaded,
    padx = 40,
    pady = 30
)   

voiceButton.pack(pady=75, padx=75)
root.mainloop()