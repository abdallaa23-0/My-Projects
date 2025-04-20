import requests 
from colorama import Fore 
API_KEY = "c89c10d182d0b561800f52ca2c2b3755"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather" 

def get_weather(city):
    params = {
        'q':city,
        'appid':API_KEY,
        'units':'metric'
    }

    try: 
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        if response.status_code == 404:
            print(Fore.RED + 'City not found.')
            return
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        weather_desc = data["weather"][0]["description"].title()
        wind = data["wind"]["speed"]
        humidity = data["main"]["humidity"]

        print(Fore.CYAN + f"\n📍 {city.title()}")
        print(Fore.YELLOW + f"🌡️ Temperature: {temp}°C (feels like {feels_like}°C)")
        print(Fore.BLUE + f"☁️ Weather: {weather_desc}")
        print(Fore.MAGENTA + f"💨 Wind Speed: {wind} m/s")
        print(Fore.LIGHTGREEN_EX + f"💧 Humidity: {humidity}%")
         
    except Exception as e:
        print(Fore.RED + "⚠️ Something went wrong:", str(e))


# ---- Main ----
if __name__ == "__main__":
    print(Fore.LIGHTYELLOW_EX + "=== Terminal Weather App ===")
    city = input("Enter your city: ")
    get_weather(city)