import tkinter as tk 
import requests
import json
from datetime import datetime

# Initialize window
root = tk.Tk()
root.geometry("400x400")
root.resizable(0,0)

# Title of window & icon
root.title('Weather App')
root.iconbitmap('icon.ico')

# ----------------------Functions to fetch and display weather info
city_value = tk.StringVar()

def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()

def showWeather():
    # Entry Api key, copies from the OpenWeatherApp dashboard
    api_key = 'YOUR_API_KEY'

    # Get city name from user from the input field 
    city_name = city_value.get()

    # API Url
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid='+api_key

    #get the response from fetched url
    response  = requests.get(weather_url)

    #changing response from json to python module
    weather_info = response.json()

    tfield.delete('1.0',tk.END)   #to clear the text field for every new output
    

    #as per API documentation, if the cod is 200, it means that weather data was successfully fetched

    if weather_info['cod'] == 200:
        kelvin = 273 
        #-----------Storing the fetched values of weather of a city
        temp = int(weather_info['main']['temp'] - kelvin)
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed'] * 3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']
        
        sunrise_time = time_format_for_location(sunrise +timezone)
        sunset_time = time_format_for_location(sunset + timezone)
        
        # assigning value to our weather variable, to display as output
        weather = f"\nWeather of: {city_name}\nTemparture (Celsis) : {temp} \nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"

    tfield.insert(tk.INSERT, weather)   #to insert or send value in our Text Field to display output






city_head = tk.Label(root, text='Enter City Name', font='Arial 12 bold')
city_head.pack(pady=10)

input_entry = tk.Entry(root, width=24, font=('Arial 14 bold'),textvariable=city_value)
input_entry.pack()

button = tk.Button(root, text='Check Weather',font="Arial 10", bg='lightblue', fg='black',padx=5, pady=5,command=showWeather,)
button.pack(pady= 20)

weather_now = tk.Label(root, text = "The Weather is:", font = 'arial 12 bold')
weather_now.pack(pady=10)
 
tfield = tk.Text(root, width=46, height=10)
tfield.pack()
 

root.mainloop()
