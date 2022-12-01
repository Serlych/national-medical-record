import json

from lib.http import get, post, patch
from lib.input import input_handler


def api(action: str, collection_url: str, available_endpoints: dict, model, data_override=None):
    endpoint = available_endpoints[action]
    url = f"{collection_url}/{endpoint}"

    handler = {
        "buscar": get,
        "crear": post,
        "actualizar": patch,
        "asociar": post,
        "asociar_receta": post,
        "asociar_prueba": post
    }

    data = data_override
    if (action == "crear") or (action == "actualizar"):
        data = input_handler(model, action)

    response = handler[action](endpoint=url, data=data)
    deserialized_response = json.loads(response)

    print(json.dumps(deserialized_response, indent=4))

    return response


def api_factory(action: str, collection_url: str, available_endpoints: dict, model, data_override=None):
    return api(action, collection_url, available_endpoints, model, data_override)
