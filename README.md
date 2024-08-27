# Weather Application

This project is a Flask-based weather application that provides users with real-time weather information. The application allows users to search for weather conditions in any city worldwide and includes features like the current weather, hourly forecasts, and weekly forecasts. The application is designed with a responsive UI, including a video background and dynamic weather icons.

## Features

### Implemented Features
- **Current Weather Display**: Users can view the current temperature, high and low temperatures, weather conditions (e.g., clear sky, rain), wind status, humidity, visibility, and sunrise/sunset times for a selected city.
- **Search by Location**: Users can enter a city name, state code, and country code to retrieve weather information for that location.
- **Current Location Weather**: Users can click a button to retrieve the weather for their current location based on their device’s GPS coordinates.
- **Contact Form**: A contact form is included (not yet connected to a backend) where users can send messages.

### Future/Planned Features
- **Hourly Weather Forecast**: Space has been left in the UI for displaying an hourly weather forecast. This feature will show the weather conditions, temperature, and an icon for the next 12 hours.
- **Weekly Weather Forecast**: Space has been left in the UI for displaying a weekly weather forecast. This feature will provide the daily high and low temperatures and a weather icon for each day of the week.

## Setup Instructions

### Prerequisites
- **Python 3.6+**: Make sure you have Python installed on your system.
- **pip**: Ensure pip is installed for managing Python packages.

### Installation


# Clone the Repository
git clone git@github.com:satish-y3/weather_application.git
cd weather_application

# Create and Activate a Virtual Environment
python3 -m venv venv
source venv/bin/activate  
On Windows use `venv\Scripts\activate`

# Install Dependencies
pip install -r requirements.txt

# Set Up Environment Variables
# Create a .env file in the root of the project and add your API key
echo "API_KEY=your_openweather_api_key" > .env

# Run the Application
python app.py

# Access the Application
Open your web browser and go to http://localhost:5000 to view the weather dashboard.

# Usage
## Searching for Weather
- **Enter a city name, state code, and country code in the search form and click "Get Weather" to see the current weather information for that location.**
- **Click "Current Location Weather" to get the weather based on your device's current location.**

# Contact Form
- **Fill out the contact form to send a message. (Note: The backend functionality for the contact form is not yet implemented.)**

# Future Improvements
- **Hourly Forecast Implementation: Connect the hourly forecast data from the OpenWeather API to the front-end to display 12-hour forecasts.**
- **Weekly Forecast Implementation: Connect the daily forecast data from the OpenWeather API to the front-end to display 7-day forecasts.**
- **Contact Form Backend: Implement the backend to handle form submissions, store the data in a database, and potentially send emails.**
- **Error Handling: Improve error handling to manage cases where the API request fails or the user inputs invalid data.**

# Known Issues
- **Incomplete Features: Hourly and weekly forecast features are placeholders and are yet to be fully implemented.**
- **No Backend for Contact Form: The contact form is currently not functional, as it does not have a backend to process submissions.**


