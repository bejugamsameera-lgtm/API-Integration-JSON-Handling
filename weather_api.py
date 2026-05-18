import requests

API_KEY = "bd550a767db97aa4d57b11161dfd214d"   # Replace with your OpenWeather API key
CITY = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url, timeout=10)

    # Check if request was successful
    if response.status_code == 200:
        data = response.json()

        # Parse JSON data
        city = data["name"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]

        # Display output
        print("\nWeather Information")
        print("-------------------")
        print(f"City: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather}")

    elif response.status_code == 404:
        print("City not found. Please enter a valid city name.")

    else:
        print(f"Error: {response.status_code}")

except requests.exceptions.RequestException as e:
    print("Network error:", e)