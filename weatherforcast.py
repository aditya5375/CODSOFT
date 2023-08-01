#import requests
import tkinter as tk
from tkinter import font

API_KEY = "51cd8d28ede14132a38112633230807"



def get_weather():
    city = entry.get()
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"
    response = requests.get(url)
    data = response.json()

    if 'error' in data:
        result_label.config(text="City not found.", font=font_style)
        return

    temperature = data['current']['temp_c']
    humidity = data['current']['humidity']
    wind_speed = data['current']['wind_kph']
    description = data['current']['condition']['text']

    result_label.config(text=f"Temperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} km/h\nDescription: {description}", font =font_style)

# Create the GUI
window = tk.Tk()
window.title("Weather Forecast")
window.geometry("300x400")

# Configure Poppins font
font_style = font.Font(family="Poppins", size=10)


# Set Poppins font for labels and entry
label = tk.Label(window, text="Enter city:", font=font_style)
label.pack(pady=10)

entry = tk.Entry(window, font=font_style)
entry.pack()

button = tk.Button(window, text="Get Weather", command=get_weather, font=font_style , bg="#4CAF50", fg="white")
button.pack()

result_label = tk.Label(window, text="", font=font_style )
result_label.pack()

Credit_label = tk.Label(window, text="Code By Aditya Mandhare", font=font_style, wraplength=250 , pady= 50)
Credit_label.pack()

window.mainloop()

# Code by Aditya Mandhare