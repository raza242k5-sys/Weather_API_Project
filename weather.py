import requests

from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

if API_KEY is None:
    print("API key not found. Please check your .env file.")
    exit()

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:

        city_name = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]
        wind = data["wind"]["speed"]

        print("\n------ Weather Report ------")
        print(f"City        : {city_name}")
        print(f"Country     : {country}")
        print(f"Temperature : {temperature} °C")
        print(f"Humidity    : {humidity}%")
        print(f"Weather     : {weather.title()}")
        print(f"Wind Speed  : {wind} m/s")

    else:
        print("City not found!")

except requests.exceptions.ConnectionError:
    print("No Internet Connection")

except Exception as e:
    print("Error:", e)