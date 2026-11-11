import json
import os
import urllib.parse
import urllib.request

from dotenv import load_dotenv


# 1. A small class to store the results
class Weather:
    def __init__(self, data):
        self.city = data["name"]
        self.description = data["weather"][0]["description"]
        self.temp = data["main"]["temp"]
        self.humidity = data["main"]["humidity"]
        self.wind = data["wind"]["speed"]

    def summary(self):
        print("-------------------------")
        print("City       :", self.city)
        print("Condition  :", self.description)
        print("Temperature:", self.temp, "°C")
        print("Humidity   :", self.humidity, "%")
        print("Wind       :", self.wind, "m/s")
        print("-------------------------")


# 2. Read the API key from the .env file
load_dotenv()
api_key = os.getenv("OPENWEATHER_API_KEY")

# 3. Build the URL
city = input("Enter city: ")
parms = {"q": city, "appid": api_key, "units": "metric"}
url = "https://api.openweathermap.org/data/2.5/weather?" + urllib.parse.urlencode(parms)

# 4. Call the API and read the response
try:
    response = urllib.request.urlopen(url)
    text = response.read().decode()
except Exception as e:
    print("Request failed:", e)
    quit()

# 5. Parse the JSON into a dictionary
data = json.loads(text)

# 6. Store it in the class and print the summary
weather = Weather(data)
weather.summary()
