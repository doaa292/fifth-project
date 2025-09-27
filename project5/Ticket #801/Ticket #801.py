import tkinter as tk
import requests
import threading

def get_weather():
    def worker():
        city = entry.get()
        try:
            data = requests.get(f"https://example.com/weather/{city}").text
            label.config(text=data)
        except Exception as e:
            label.config(text=f"Error: {e}")
    threading.Thread(target=worker).start()  # start new thread

root = tk.Tk()
root.title("Weather App")

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Get Weather", command=get_weather)
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()