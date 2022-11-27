from fastapi import Request
from fastapi.encoders import jsonable_encoder
from pymongo.results import InsertOneResult, UpdateResult
from pymongo.typings import _DocumentType
from typing import List, Optional


def insert_one(request: Request, data, collection: str) -> InsertOneResult:
    to_insert = jsonable_encoder(data)
    return request.app.database[collection].insert_one(to_insert)


def find_one(request: Request, criteria: dict, collection: str) -> Optional[_DocumentType]:
    return request.app.database[collection].find_one(criteria)


def find_many(request: Request, criteria: dict, collection: str) -> [List[_DocumentType], List]:
    cursor = list(request.app.database[collection].find(criteria))
    object_ids = [str(item['_id']) for item in cursor]

    return [cursor, object_ids]


def update_one(request: Request, find_criteria: dict, update_criteria: dict, collection: str) -> UpdateResult:
    return request.app.database[collection].update_one(find_criteria, update_criteria)


def aggregate(request: Request, aggregate_criteria: List[dict], collection: str):
    return request.app.database[collection].aggregate(aggregate_criteria)
