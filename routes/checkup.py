#!/usr/bin/env python3
from fastapi import APIRouter, Body, Request, status
from lib.mongo import insert_one

from models.checkup import Checkup, CheckupUpdate

router = APIRouter()
coll = "checkup"


@router.post("/", response_description="Create a new checkup", status_code=status.HTTP_201_CREATED,
             response_model=Checkup)
def create_patient(request: Request, checkup: Checkup = Body(...)):
    return insert_one(request, checkup, coll)
