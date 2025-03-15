import os
import socket
import requests
import time
from dotenv import load_dotenv

load_dotenv()


def main():
    """
    Fetch data from the ADSB API and send it over a TCP connection.

    Uses the following environment variables:
      ADSB_KEY: API key for authentication.
      TARGET_IP: IP address of the target server.
      TARGET_PORT: Port number of the target server.
      TARGET_LAT: Latitude for the API request.
      TARGET_LON: Longitude for the API request.
      TARGET_MILES: Distance (in nautical miles) for the API request.
    """

    adsb_key = os.environ.get("ADSB_KEY")
    target_ip_address = os.environ.get("TARGET_IP")
    target_port = int(os.environ.get("TARGET_PORT"))
    target_lat = os.environ.get("TARGET_LAT")
    target_lon = os.environ.get("TARGET_LON")
    target_miles = os.environ.get("TARGET_MILES")
    url = (
        "https://adsbexchange-com1.p.rapidapi.com/v2/lat/"
        + target_lat
        + "/lon/"
        + target_lon
        + "/dist/"
        + target_miles
        + "/"
    )
    headers = {
        "x-rapidapi-host": "adsbexchange-com1.p.rapidapi.com",
        "x-rapidapi-key": adsb_key,
    }

    while True:
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.text
        except Exception as e:
            print("Error fetching data:" + e)

        if data:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((target_ip_address, target_port))
                    s.sendall((data + "\n").encode("utf-8"))
            except Exception as e:
                print(f"Error sending data: {e}")

        time.sleep(5)


if __name__ == "__main__":
    main()
