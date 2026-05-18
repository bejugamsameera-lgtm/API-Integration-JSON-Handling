# Python API Integration Project

## Project Goal

Learn how Python communicates with external APIs and handles JSON data.

---

## Project Title

Weather Information App Using Python and OpenWeather API

This project fetches real-time weather information for any city using the OpenWeather API. It demonstrates how to send HTTP requests, parse JSON responses, apply search logic, and handle errors.

---

## Learning Objectives

By completing this project, you will learn how to:

* Send HTTP requests using the `requests` library
* Receive and parse JSON responses
* Extract specific values from JSON data
* Accept user input for search
* Handle invalid input and network errors
* Work with external APIs

---

## Requirements

* Fetch data using the Requests library
* Parse JSON responses
* Apply filtering or search logic
* Handle API errors

---

## Deliverables

* Working Python script
* Output screenshots with explanation
* README documentation

---

## Tech Stack

* Python
* Requests library
* JSON
* OpenWeather API
* Visual Studio Code

---

## Project Structure

WEATHER-API-PROJECT/

├── test_api.py  
├── weather_api.py 

├── requirements.txt

---

# Step 1: Install Python

Download and install Python from:
[https://www.python.org/downloads/](https://www.python.org/downloads/)

During installation, enable the option:

* Add Python to PATH

Verify installation:

```bash
python --version
```

or

```bash
py --version
```

---

# Step 2: Create Project Folder

Create a folder named:

```text
weather-api-project
```

Open this folder in Visual Studio Code.

---

# Step 3: Install Required Library

Open the terminal in VS Code and run:

```bash
py -m pip install requests
```

Create `requirements.txt`:

```bash
py -m pip freeze > requirements.txt
```

---

# Step 4: Create an OpenWeather API Key

1. Go to [https://openweathermap.org/](https://openweathermap.org/)
2. Create a free account.
3. Verify your email.
4. Open the API Keys page.
5. Generate a new API key.
6. Copy the API key.
7. Wait 10 minutes to 2 hours for activation.

---

# Step 5: Create `weather_api.py`

paste code here

---

# Step 6: Add Your API Key

Replace:

```python
API_KEY = "YOUR_API_KEY"
```

with:

```python
API_KEY = "your_actual_api_key"
```

---

# Step 7: Run the Project

In the VS Code terminal:

```bash
py weather_api.py
```

---

# Step 8: Enter a City Name

Example:

```text
Enter city name: Hyderabad
```

---

# Sample Output

```text
Weather Information
-------------------
City: Hyderabad
Temperature: 31.2°C
Humidity: 62%
Condition: scattered clouds
```

---

# How the Project Works

## 1. User Input

The program asks the user to enter a city name.

## 2. Build API URL

The city name and API key are added to the API URL.

## 3. Send Request

The `requests.get()` function sends an HTTP GET request.

## 4. Receive JSON

The API returns weather data in JSON format.

## 5. Parse JSON

The script extracts:

* City name
* Temperature
* Humidity
* Weather description

## 6. Display Output

The extracted data is printed in a readable format.

## 7. Error Handling

The script handles invalid cities, invalid API keys, and network errors.

---

# JSON Parsing Example

If the API returns:

```json
{
  "name": "Hyderabad",
  "main": {
    "temp": 31.2,
    "humidity": 62
  },
  "weather": [
    {
      "description": "scattered clouds"
    }
  ]
}
```

The code accesses:

```python
data["name"]
data["main"]["temp"]
data["main"]["humidity"]
data["weather"][0]["description"]
```

---

# Search Logic Used

The user enters a city name, and the program fetches weather data only for that city.

---

# Error Handling Covered

* `401` → Invalid API key
* `404` → City not found
* Connection error
* Timeout error
* Other request exceptions

---

# Common Issues and Solutions

## API Error 401

Cause: Invalid or inactive API key.

Solution:

* Verify the API key.
* Wait for activation.

## API Error 404

Cause: Incorrect city name.

Solution:

* Check the spelling.

## `pip` Not Recognized

Use:

```bash
py -m pip install requests
```

## Connection Error

Cause: Internet, firewall, or VPN issue.

Solution:

* Check internet connection.
* Disable VPN.

---

# Testing the API in Browser

Replace `YOUR_API_KEY` and open:

```text
https://api.openweathermap.org/data/2.5/weather?q=Hyderabad&appid=YOUR_API_KEY&units=metric
```

If the key is valid, JSON weather data will appear.

---



# requirements.txt Example

```text
requests==2.32.4
```

---


# Useful Resources

* Python: [https://www.python.org/](https://www.python.org/)
* Requests Documentation: [https://requests.readthedocs.io/](https://requests.readthedocs.io/)
* OpenWeather API: [https://openweathermap.org/api](https://openweathermap.org/api)
* Visual Studio Code: [https://code.visualstudio.com/](https://code.visualstudio.com/)

---

# Author

Bejugam Sameera

