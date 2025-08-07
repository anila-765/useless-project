import tkinter as tk
import random

# List of silly vibe messages
vibes = [
    "You radiate squirrel energy today 🐿️",
    "Your aura smells like burnt toast and ambition 🔥🍞",
    "You are 73% chaos, 27% glitter ✨",
    "Your vibe: mysterious potato 🥔",
    "Like a confused penguin, you waddle through greatness 🐧",
    "You have the energy of a Wi-Fi signal with one bar 📶",
    "Today, you are the human version of a loading screen 🔄",
    "Your vibe? Just vibes. Nothing else. 🎵",
    "Cloudy with a chance of brain fog ☁️🧠",
    "You're a whole vibe... but it's on airplane mode ✈️"
]

# Function to update the vibe label
def check_vibe():
    name = name_entry.get()
    if name.strip() == "":
        result_label.config(text="Please enter your name 👀")
    else:
        vibe = random.choice(vibes)
        result_label.config(text=f"Hey {name}, {vibe}")

# Setup the main app window
app = tk.Tk()
app.title("Vibe Checker 3000")
app.geometry("400x300")
app.configure(bg="#f0f8ff")

# Title label
title_label = tk.Label(app, text="✨ Vibe Checker 3000 ✨", font=("Comic Sans MS", 16), bg="#f0f8ff")
title_label.pack(pady=10)

# Name entry
name_entry = tk.Entry(app, font=("Arial", 12), width=30)
name_entry.pack(pady=10)

# Check vibe button
vibe_button = tk.Button(app, text="Check My Vibe", command=check_vibe, font=("Arial", 12), bg="#b3e5fc")
vibe_button.pack(pady=10)

# Result label
result_label = tk.Label(app, text="", font=("Arial", 12), wraplength=300, bg="#f0f8ff")
result_label.pack(pady=20)

# Run the app
app.mainloop()
