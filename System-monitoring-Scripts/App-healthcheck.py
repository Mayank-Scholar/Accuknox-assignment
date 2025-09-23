import requests
import logging
import os
from datetime import datetime

os.makedirs("log", exist_ok=True)

# CONFIGURATION
LOG_FILE = "log/app_uptime.log"
TIMEOUT = 5  # seconds

# SETUP LOGGING 
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def check_application_status(url):
    try:
        response = requests.get(url, timeout=TIMEOUT)
        status_code = response.status_code

        if 200 <= status_code < 300:
            logging.info(f"Application is UP. Status code: {status_code}")
            print(f"[{datetime.now()}] Application is UP. Status code: {status_code}")
        else:
            logging.warning(f"Application is DOWN. Status code: {status_code}")
            print(f"[{datetime.now()}] Application is DOWN. Status code: {status_code}")

    except requests.exceptions.RequestException as e:
        logging.error(f"Application is DOWN. Error: {str(e)}")
        print(f"[{datetime.now()}] Application is DOWN. Error: {str(e)}")

if __name__ == "__main__":
    APP_URL = input("Enter application URL:")
    check_application_status(APP_URL)