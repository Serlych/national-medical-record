#!/usr/bin/env python3
from fastapi import APIRouter, Body, Request, status
from lib.mongo import insert_one, find_one

from models.checkup import Checkup, CheckupUpdate

router = APIRouter()
coll = "checkup"

@router.get("/{NSS}", response_description="Get checkup info", status_code=status.HTTP_200_OK,
            response_model=Checkup)
def find_checkup(request: Request, NSS: str):
    return find_one(request, {"NSS": NSS}, coll)

@router.post("/", response_description="Create a new checkup", status_code=status.HTTP_201_CREATED,
             response_model=bool)
def create_checkup(request: Request, checkup: Checkup = Body(...)):
    return insert_one(request, checkup, coll)
