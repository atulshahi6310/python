#City Wise Weather Report Projects

#Weather Details Fetching Using Web API
#Step 01: Visit https://developer.accuweather.com/
#Step 02: Register Yourself using valid credentials.
#Step 03: Login into dashboard
#Step 04: Click on My Apps
#Step 05: Click on add a new app (Check All Features+ Select Country Specific Data Retrival)
#Step 06: Click on the app and copy the key

import requests

api_key = 	"0cLy4PHD8TNzokYhGnOdyoSyudJHvu4D"
city = input("Enter a City Name:")
url = f"http://dataservice.accuweather.com/locations/v1/cities/search?q={city}&apikey={api_key}"

# Step 1: Get the location key
def fetchLocationKey():
    location_url = url
    response = requests.get(location_url)
    data = response.json()
    if response.status_code == 200 and data:
        location_key = data[0]['Key']
        return location_key
    else:
        print("Error fetching location key")

location_Key = fetchLocationKey()

weather_url = f"http://dataservice.accuweather.com/currentconditions/v1/{location_Key}?apikey={api_key}"

# Make the request
response = requests.get(weather_url)

# Parse the response
if response.status_code == 200:
    weather_data = response.json()
    if weather_data:
        temperature = weather_data[0]['Temperature']['Metric']['Value']
        unit = weather_data[0]['Temperature']['Metric']['Unit']
        description = weather_data[0]['WeatherText']
        
        print(f"Current weather in {city}: {description}, {temperature}°{unit}")
    else:
        print("No weather data found")
else:
    print(f"Failed to fetch weather. Status: {response.status_code}")

