import requests
from main import BASE_URL


def get(endpoint, args=''):
    response = requests.get(BASE_URL + f"/{endpoint}/{args}")

    if response.ok:
        return response.text


def post(endpoint, data, args=''):
    response = requests.post(BASE_URL + f"/{endpoint}/{args}", json=data)

    if not response.ok:
        print(f"Failed to post on {endpoint}: {response.text}.")
    else:
        print(f"Posted on {endpoint} succesfully.")
