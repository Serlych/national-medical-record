from fastapi import Request
from fastapi.encoders import jsonable_encoder


def insert_one(request: Request, data, collection: str):
    to_insert = jsonable_encoder(data)
    new_entry = request.app.database[collection].insert_one(to_insert)

    return new_entry.acknowledged


def find_one(request: Request, criteria: dict, collection: str):
    if entry := request.app.database[collection].find_one(criteria) is not None:
        return entry
