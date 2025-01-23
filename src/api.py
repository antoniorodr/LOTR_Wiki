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
    print(api_call("character/5cd99d4bde30eff6ebccfc5f/quote"))
    # print(api_call("character"))