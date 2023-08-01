import random
import string
import tkinter as tk
from tkinter import font
from tkinter import messagebox


def generate_password():
    """ Generate Chipher TEXT based On word length using random module"""
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length must be a positive integer.")
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text="Generated Password: \n " + password)
    except ValueError as e:
        messagebox.showerror("Error", str(e))


# creating Main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("300x500")

# font style setting
font_style = font.Font(family="Poppins", size=10)

# Title label Creating
title_label = tk.Label(window, text="Password Generator", font=("Poppins", 16, "bold"), fg="#0066CC", pady=10)
title_label.pack()

# Creating length label and entry field for geting user input
length_label = tk.Label(window, text="Password Length:", font=font_style)
length_label.pack()
length_entry = tk.Entry(window, font=font_style, width=20)
length_entry.pack()

# Creating a frame for buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

# Creating the generate button
generate_button = tk.Button(button_frame, text="Generate", command=generate_password, font=font_style, padx=5, pady=3,
                            bg="#4CAF50", fg="white", width=10)
generate_button.pack(side=tk.LEFT)

# Creating the result label
result_label = tk.Label(window, text="   Generated Password : ", font=font_style, wraplength=250, padx=10)
result_label.pack()

Credit_label = tk.Label(window, text="Code By Aditya Mandhare", font=font_style, wraplength=250, pady=50)
Credit_label.pack()

# Center the window on the screen
window.update_idletasks()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
window.geometry(f"+{x_coordinate}+{y_coordinate}")

# Starting the GUI
window.mainloop()

# Code by Aditya Mandhare