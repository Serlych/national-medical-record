import json

from lib.http import get, post, patch
from lib.input import input_handler


def api(action: str, collection_url: str, available_endpoints: dict, model):
    data = input_handler(model)
    print(data)
    endpoint = available_endpoints[action]
    url = f"{collection_url}/{endpoint}"

    handler = {
        'get': get,
        'post': post,
        'patch': patch
    }

    response = handler[action](endpoint=url, data=data)
    deserialized_response = json.loads(response)

    print(json.dumps(deserialized_response, indent=4))

    return response


def api_factory(action: str, collection_url: str, available_endpoints: dict, model):
    return api(action, collection_url, available_endpoints, model)
