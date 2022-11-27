import requests

from main import NMR_API_URL


def get(endpoint, data=None, verbose=False):
    response = requests.get(f"{NMR_API_URL}/{endpoint}")

    if verbose:
        if not response.ok:
            print(f"Failed to get on {endpoint}: {response.text}.")
        else:
            print(f"Get on {endpoint} succesfully.")

    return response.text


def post(endpoint, data, verbose=False):
    response = requests.post(f"{NMR_API_URL}/{endpoint}", json=data)

    if verbose:
        if not response.ok:
            print(f"Failed to post on {endpoint}: {response.text}.")
        else:
            print(f"Post on {endpoint} succesfully.")

    return response.text


def patch(endpoint, data, verbose=False):
    response = requests.patch(f"{NMR_API_URL}/{endpoint}", json=data)

    if verbose:
        if not response.ok:
            print(f"Failed to patch on {endpoint}: {response.text}.")
        else:
            print(f"Patch on {endpoint} succesfully.")

    return response.text
