from fastapi import Request
from fastapi.encoders import jsonable_encoder
from pymongo.results import InsertOneResult, UpdateResult
from pymongo.typings import _DocumentType
from typing import List, Any


def insert_one(request: Request, data, collection: str) -> InsertOneResult:
    to_insert = jsonable_encoder(data)
    return request.app.database[collection].insert_one(to_insert)


def find_one(request: Request, criteria: dict, collection: str) -> _DocumentType:
    find_result = request.app.database[collection].find_one(criteria)
    copy = find_result.copy()
    copy['id'] = str(find_result['_id'])

    return copy


def find_many(request: Request, criteria: dict, collection: str) -> list[_DocumentType]:
    cursor = list(request.app.database[collection].find(criteria))
    copy = cursor.copy()

    for item in copy:
        item['id'] = str(item['_id'])

    return copy


def update_one(request: Request, find_criteria: dict, update_criteria: dict, collection: str) -> UpdateResult:
    return request.app.database[collection].update_one(find_criteria, update_criteria)


def aggregate(request: Request, aggregate_criteria: List[dict], collection: str):
    return request.app.database[collection].aggregate(aggregate_criteria)
