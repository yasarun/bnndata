import requests
import datetime
import os

def download_binance_data(start_date, end_date, symbol="BTCUSDT", interval="5m", output_dir="binance_data"):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Convert start and end dates to UNIX timestamp
    start_timestamp = int(datetime.datetime.strptime(start_date, "%Y-%m-%d").timestamp()) * 1000
    end_timestamp = int(datetime.datetime.strptime(end_date, "%Y-%m-%d").timestamp()) * 1000

    # Generate list of dates within the specified range
    date_range = [datetime.datetime.utcfromtimestamp(ts / 1000).strftime('%Y-%m-%d') for ts in range(start_timestamp, end_timestamp, 86400000)]

    # Download data for each date in the range
    for date in date_range:
        url = f"https://data.binance.vision/data/spot/daily/klines/{symbol}/{interval}/{symbol}-{interval}-{date}.zip"
        filename = f"{symbol}-{interval}-{date}.zip"
        filepath = os.path.join(output_dir, filename)

        # Check if file already exists
        if os.path.exists(filepath):
            print(f"File {filename} already exists. Skipping...")
            continue

        # Download the file
        print(f"Downloading {filename}...")
        response = requests.get(url)
        with open(filepath, 'wb') as f:
            f.write(response.content)

    print("Download completed.")

# Example usage:
start_date = "2024-01-01"
end_date = "2024-01-10"
download_binance_data(start_date, end_date)
