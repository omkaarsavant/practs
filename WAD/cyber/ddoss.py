import requests
import time

TARGET_URL = "https://www.ganeshcables.com/"


# Now we define two variables...
REQUEST_INTERVAL = 1  # The number of seconds between each request sent to the target
DURATION = 60  # The total number of seconds this script will run unless manually stopped earlier, the server crashes, or you're cut off

def send_request():
    try:
        requests.get(TARGET_URL)  # Here is where a GET request is sent to the target server
        print(f"Request sent to {TARGET_URL}")
    except requests.RequestException:  # This will stop sending the requests as soon as it no longer can
        print("Error sending request")

def main():
    end_time = time.time() + DURATION  # Here, we establish the maximum length of time the script will run
    while time.time() < end_time:  # Now we have the control mechanism to automate sending the GET requests at our chosen interval
        send_request()
        time.sleep(REQUEST_INTERVAL)

if __name__ == "__main__":
    main()
