
import requests
from datetime import datetime
#fetch the wordle today's answer from the website
def answer():
    today = datetime.today().strftime('%Y-%m-%d')
    url = f"https://www.nytimes.com/svc/wordle/v2/{today}.json"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data.get("solution", "apple")
    except:
        return "apple"


    


