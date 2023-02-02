import requests
import json

# API Key for OpenWeatherMap
api_key = '<your_api_key_here>'

# Location for which to retrieve weather data
city = '<city_name>'

# API URL
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

# Make API request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse JSON data
    data = json.loads(response.text)

    # Get current weather and temperature
    weather = data['weather'][0]['main']
    temperature = data['main']['temp']
    
    # Match the weather to an icon
    if weather == 'Clear':
        icon = '☀️'
    elif weather == 'Clouds':
        icon = '☁️'
    elif weather == 'Rain':
        icon = '🌧'
    elif weather == 'Snow':
        icon = '❄️'
    else:
        icon = '🌤'

    # Display the current weather and temperature
    print(f'{icon} The current weather in {city} is {weather} with a temperature of {temperature}°F.')
else:
    # If the request was not successful, display an error message
    print('An error occurred while retrieving the weather data.')
