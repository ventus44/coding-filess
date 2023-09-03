import requests
from bs4 import BeautifulSoup
import time

def get_opap_data():
    url = "https://www.opap.gr/en/powerspin-draw-results" 

    while True:
        response = requests.get(url)
        soup = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')  # Here is the modification
        outcomes = soup.find_all(class_="draw-overunder") 

        count = 0
        last_outcome = ""

        for outcome in outcomes:
            style = outcome.get('style')
            current_outcome = "U"  # Default to "U" for "under"

            if style is not None and 'rgb(250, 173, 41)' in style:
                current_outcome = "O"

            print("Processing outcome: ", current_outcome)

            if current_outcome == last_outcome:
                count += 1
            else:
                count = 1
                last_outcome = current_outcome

            if count == 6:
                print(f"6 {last_outcome}s in a row!")

        print("Waiting for next update...")
        time.sleep(60)

print("Starting script...")
get_opap_data()

    

   