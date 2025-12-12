from config import init_supabase
import pandas as pd

# Initialize Supabase
supabase = init_supabase()

if not supabase:
    print("Failed to connect to Supabase.")
else:
    try:
        # Fetch the most recent entry with temperature
        response = supabase.table("weather_data").select("*").order("timestamp", desc=True).limit(1).execute()
        
        if response.data:
            latest = response.data[0]
            print(f"Latest Data Found:")
            print(f"Timestamp: {latest.get('timestamp')}")
            print(f"T_current: {latest.get('t_current')} °C")
            print(f"Zone: {latest.get('zone')}")
        else:
            print("No data found in 'weather_data' table.")
            
    except Exception as e:
        print(f"Error querying Supabase: {e}")
