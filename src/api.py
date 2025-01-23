import requests
import os
from dotenv import load_dotenv

load_dotenv()

def api_call(endpoint):
    URL = f"https://the-one-api.dev/v2/{endpoint}"
    headers = {
        "Authorization": os.environ["token"]
        }
    response = requests.get(url = URL, headers = headers)
    if response:
        return response.json()
    else:
        raise Exception(f"Non-success. Status code: {response.status_code}")




if __name__ == "__main__":
    # print(api_call("movie/5cd95395de30eff6ebccde5c/quote"))
    print(api_call("character"))