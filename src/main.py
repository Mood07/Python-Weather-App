import requests

# ❗ ENTER YOUR API KEY HERE ❗
API_KEY = "YOUR_API_KEY_HERE"

API_URL = "https://api.openweathermap.org/data/2.5/weather"


def fetch_weather(city_name):
    """
    Fetch weather data for a given city using OpenWeather API.
    Returns JSON response if successful, otherwise None.
    """
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric",
    }

    try:
        response = requests.get(API_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 401:
            print("❌ Invalid API key. Please update the API_KEY variable.")
        elif response.status_code == 404:
            print("❌ City not found. Check the name and try again.")
        else:
            print(f"HTTP Error: {http_err}")

    except requests.exceptions.Timeout:
        print("⏳ Request timed out. Try again later.")

    except requests.exceptions.RequestException as err:
        print(f"❌ Error fetching weather data: {err}")

    return None


def print_weather(data):
    """
    Pretty-print weather information.
    """
    try:
        city = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"].title()

        print("\n==============================")
        print(f"Weather in {city}, {country}")
        print("==============================")
        print(f"Description : {description}")
        print(f"Temperature : {temp:.1f}°C")
        print(f"Feels like  : {feels_like:.1f}°C")
        print(f"Humidity    : {humidity}%")
        print("==============================\n")

    except (KeyError, IndexError, TypeError):
        print("Unexpected API response format.")


def main():
    print("====================================")
    print("           WEATHER APP              ")
    print("====================================")

    if API_KEY == "YOUR_API_KEY_HERE":
        print("⚠️ ERROR: Please edit main.py and add your API key to the API_KEY variable.")
        return

    while True:
        city = input("Enter city name (or 'q' to quit): ").strip()

        if city.lower() == "q":
            print("Goodbye! 👋")
            break

        if not city:
            print("City name cannot be empty.")
            continue

        data = fetch_weather(city)
        if data:
            print_weather(data)


if __name__ == "__main__":
    main()
