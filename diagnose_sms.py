import os
from dotenv import load_dotenv
import requests

load_dotenv()

print("--- Environment Diagnostics ---")
api_key = os.getenv("TERMII_API_KEY")
sender_id = os.getenv("TERMII_SENDER_ID")

if api_key:
    print(f"TERMII_API_KEY found: {api_key[:4]}...{api_key[-4:]}")
else:
    print("ERROR: TERMII_API_KEY is missing or empty.")

print(f"TERMII_SENDER_ID: {sender_id}")

print("\n--- Termii Connectivity Test ---")
if api_key:
    url = "https://api.ng.termii.com/api/get-balance"
    params = {"api_key": api_key}
    try:
        response = requests.get(url, params=params)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Connectivity Error: {e}")
else:
    print("Skipping connectivity test due to missing key.")
