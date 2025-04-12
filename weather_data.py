import requests
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import random

# API setup
API_KEY = '25c714e643be12f885db4e09c306e501'  
CITIES = ['Bhopal', 'Mumbai', 'Delhi', 'Pune']
API_URL = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

# Store fetched weather data
weather_data = {}

# Fetch data for each city
for city in CITIES:
    response = requests.get(API_URL.format(city, API_KEY))
    
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp'] - 273.15  # Convert from Kelvin to Celsius
        humidity = data['main']['humidity']
        weather = data['weather'][0]['description']
        
        weather_data[city] = {
            'temperature': round(temperature, 2),
            'humidity': humidity,
            'weather': weather
        }
    else:
        print(f"Failed to fetch data for {city}")

# Extract values for visualization
cities = list(weather_data.keys())
temperatures = [weather_data[city]['temperature'] for city in cities]
humidity_levels = [weather_data[city]['humidity'] for city in cities]

# Bar plot for temperature & humidity
plt.figure(figsize=(10, 6))
sns.barplot(x=cities, y=temperatures, color='skyblue', label='Temperature (°C)')
sns.barplot(x=cities, y=humidity_levels, color='orange', label='Humidity (%)', alpha=0.6)
plt.title('Current Temperature and Humidity in Cities', fontsize=14)
plt.ylabel('Values', fontsize=12)
plt.xlabel('Cities', fontsize=12)
plt.legend()
plt.show()

# --- Line Chart for Date-wise Prediction ---
dates = [(datetime.date.today() + datetime.timedelta(days=i)).strftime('%Y-%m-%d') for i in range(7)]

# Generate mock predictions (You can use an actual API for forecasts)
predicted_temperatures = {city: [weather_data[city]['temperature'] + random.uniform(-2, 2) for _ in dates] for city in cities}

# Plot temperature trends
plt.figure(figsize=(12, 6))
for city in cities:
    plt.plot(dates, predicted_temperatures[city], marker='o', linestyle='-', label=city)

plt.title('Predicted Temperature Trends for Next 7 Days', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.show()

