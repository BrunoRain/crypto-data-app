
import requests

API_URL = "https://api.coincap.io/v2/assets"

def fetch_data():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    data = fetch_data()
    print(data)
