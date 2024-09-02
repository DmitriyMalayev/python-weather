from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def get_weather_data(city="New York"):
    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=imperial"
    weather_data = requests.get(request_url).json()
    return weather_data


if __name__ == "__main__":
    print("Getting weather data for New York...\n")
    city = input("Enter city name: ")
    weather_data = get_weather_data(city)
    pprint(weather_data)
