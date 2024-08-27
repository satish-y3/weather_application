import os
from flask import Flask, render_template, request
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv('API_KEY')  # Replace with your OpenWeather API key

# datetimeformat filter function
def datetimeformat(value, timezone_offset, format='%Y-%m-%d %H:%M:%S'):
    utc_time = datetime.utcfromtimestamp(value)
    local_time = utc_time + timedelta(seconds=timezone_offset)
    return local_time.strftime(format)

# Jinja2
app.jinja_env.filters['datetimeformat'] = datetimeformat

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    city = request.form['city']
    state_code = request.form['state_code']
    country_code = request.form['country_code']
    location = f"{city},{state_code},{country_code}"
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    weather_data = response.json()

    if response.status_code != 200 or 'main' not in weather_data:
        weather_data = None  
    else:
        lat = weather_data['coord']['lat']
        lon = weather_data['coord']['lon']

        # Fetch hourly and daily forecast data
        forecast_url = f'http://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=current,minutely,alerts&appid={API_KEY}&units=metric'
        forecast_response = requests.get(forecast_url)
        forecast_data = forecast_response.json()

        hourly_data = forecast_data.get('hourly', [])[:12]  
        daily_data = forecast_data.get('daily', [])[:7]  

    return render_template('weather_dashboard.html', weather=weather_data, hourly=hourly_data, daily=daily_data)

@app.route('/get_weather_by_location', methods=['POST'])
def get_weather_by_location():
    lat = request.form['latitude']
    lon = request.form['longitude']

    weather_url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric'
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()

    if weather_response.status_code != 200 or 'main' not in weather_data:
        weather_data = None
    else:
        # Fetch hourly and daily forecast data
        forecast_url = f'http://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=current,minutely,alerts&appid={API_KEY}&units=metric'
        forecast_response = requests.get(forecast_url)
        forecast_data = forecast_response.json()

        hourly_data = forecast_data.get('hourly', [])[:12]  
        daily_data = forecast_data.get('daily', [])[:7]  

    return render_template('weather_dashboard.html', weather=weather_data, hourly=hourly_data, daily=daily_data)

if __name__ == '__main__':
    app.run(debug=True)
