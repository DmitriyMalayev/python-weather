from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def get_weather_data(city="New York"):
    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=imperial"
    weather_data = requests.get(request_url).json()
    return weather_data


weather = True
if __name__ == "__main__":
    while True:
        city = input("Enter city name: ")
        print("Getting weather data for {city}...\n")
        weather_data = get_weather_data(city if city else "New York")
        pprint(weather_data)
        info = input("\nPress x to exit or press any other key to view more details: ")
        if info.lower() == "x":
            weather = False
