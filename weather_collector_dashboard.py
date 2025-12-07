import requests
import pandas as pd
import matplotlib.pyplot as plt
import schedule
import time
import csv
import os
from datetime import datetime

# Constants
CSV_FILE = 'weather_data.csv'
ZONES = [
    {'name': 'Umuahia', 'lat': 5.526, 'lon': 7.489},
    {'name': 'Aba', 'lat': 5.106, 'lon': 7.366},
    {'name': 'Ohafia', 'lat': 5.622, 'lon': 7.857}
]

def fetch_weather_data(zone):
    """Fetches weather data for a specific zone from Open-Meteo API."""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": zone['lat'],
        "longitude": zone['lon'],
        "current": ["temperature_2m", "relative_humidity_2m", "rain"],
        "timezone": "auto"
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        current = data.get('current', {})
        return {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'zone': zone['name'],
            'temperature': current.get('temperature_2m'),
            'humidity': current.get('relative_humidity_2m'),
            'rain': current.get('rain')
        }
    except Exception as e:
        print(f"Error fetching data for {zone['name']}: {e}")
        return None

def init_csv():
    """Initializes the CSV file with headers if it doesn't exist."""
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['timestamp', 'zone', 'temperature', 'humidity', 'rain'])

def save_to_csv(data):
    """Appends a single data record to the CSV file."""
    if not data:
        return
    
    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            data['timestamp'],
            data['zone'],
            data['temperature'],
            data['humidity'],
            data['rain']
        ])
    print(f"Saved data for {data['zone']}")

def job():
    """Main job to fetch and save data for all zones."""
    print(f"Starting data collection job at {datetime.now()}")
    for zone in ZONES:
        weather_data = fetch_weather_data(zone)
        save_to_csv(weather_data)

def visualize_trends():
    """Reads data from CSV and plots trends."""
    if not os.path.exists(CSV_FILE):
        print("No data file found.")
        return

    try:
        df = pd.read_csv(CSV_FILE)
        if df.empty:
            print("No data to visualize.")
            return

        # Convert timestamp to datetime
        df['timestamp'] = pd.to_datetime(df['timestamp'])

        # Plot Temperature
        plt.figure(figsize=(10, 6))
        for zone_name in df['zone'].unique():
            zone_data = df[df['zone'] == zone_name]
            plt.plot(zone_data['timestamp'], zone_data['temperature'], marker='o', label=zone_name)
        
        plt.title('Temperature Trends in Abia State Agricultural Zones')
        plt.xlabel('Time')
        plt.ylabel('Temperature (°C)')
        plt.legend()
        plt.grid(True)
        plt.savefig('temperature_trends.png')
        print("Saved temperature_trends.png")
        
        # Plot Rain (Optional, can be a separate plot)
        plt.figure(figsize=(10, 6))
        for zone_name in df['zone'].unique():
            zone_data = df[df['zone'] == zone_name]
            plt.plot(zone_data['timestamp'], zone_data['rain'], marker='x', linestyle='--', label=zone_name)

        plt.title('Rainfall Trends in Abia State Agricultural Zones')
        plt.xlabel('Time')
        plt.ylabel('Rain (mm)')
        plt.legend()
        plt.grid(True)
        plt.savefig('rainfall_trends.png')
        print("Saved rainfall_trends.png")

    except Exception as e:
        print(f"Error visualizing data: {e}")

if __name__ == "__main__":
    init_csv()
    
    # For demonstration, run immediately then schedule
    job()
    visualize_trends()
    
    # Schedule every 1 minute for demo purposes (real usage might be hourly)
    schedule.every(1).minutes.do(job)
    
    print("Scheduler started. Press Ctrl+C to exit.")
    while True:
        schedule.run_pending()
        time.sleep(1)
