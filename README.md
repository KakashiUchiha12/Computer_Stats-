# System Stats Dashboard with Weather and GIF Animation

This is a Python application that displays real-time system stats, weather updates, and inspirational quotes, with a dynamic animated GIF background. The dashboard is created using the **Tkinter** library and integrates with the **OpenWeatherMap API** for live weather updates.

---

## Features

- **System Monitoring**:
  - Real-time CPU usage and frequency.
  - Real-time RAM usage.
  - Network statistics (Upload and Download speeds).
  - Battery percentage and charging status.

- **Weather Updates**:
  - Fetches live weather data using OpenWeatherMap API.
  - Displays temperature, "feels like" temperature, and weather description with relevant emojis.

- **Dynamic Background**:
  - Displays a looping animated GIF as the background.

- **Inspirational Quotes**:
  - Rotates through a list of motivational quotes every 5 minutes.

- **Customizable Transparency**:
  - Allows adjusting the window transparency using a slider.

---

## Prerequisites

- Python 3.8+
- Internet connection (for weather updates).

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/KakashiUchiha12/system-stats-dashboard.git
   cd system-stats-dashboard


   Install Required Libraries: Use pip to install the necessary libraries:

bash
Copy code
pip install tkinter pillow psutil requests
Download and Configure OpenWeatherMap API:

Sign up at OpenWeatherMap and get your free API key.
Replace YOUR_OPENWEATHERMAP_API_KEY in the code with your API key.
Place Your GIF File:

Replace the path "C:/Users/Kakashi Uchiha/Downloads/200w.gif" in the code with the path to your desired GIF file.
Usage
Run the script using Python:

bash
Copy code
python system_stats_dashboard.py
Configuration
City Name:

To update the weather for a specific location, replace "Lahore" in this line:
python
Copy code
weather_info = get_weather_by_city("Lahore")
Example:
python
Copy code
weather_info = get_weather_by_city("New York")
Inspirational Quotes:

You can customize the list of quotes in the quotes array:
python
Copy code
quotes = [
    "Believe in yourself and all that you are.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
]
Screenshots
1. Dashboard Overview

2. Weather and System Stats

Troubleshooting
Missing Libraries:

Ensure all required libraries are installed:
bash
Copy code
pip install tkinter pillow psutil requests
Weather Not Updating:

Verify your API key and ensure it is correctly entered in the script:
python
Copy code
api_key = "YOUR_OPENWEATHERMAP_API_KEY"
GIF Not Displaying:

Ensure the path to the GIF file is correct and the file is accessible.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Author
Haris Khan
Email: kakahikage2@gmail.com
GitHub: KakashiUchiha12
