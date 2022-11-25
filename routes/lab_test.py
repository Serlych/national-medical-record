#!/usr/bin/env python3
from fastapi import APIRouter, Body, Request, status
from lib.mongo import insert_one, find_one

from models.lab_test import LabTest, LabTestUpdate

router = APIRouter()
coll = "lab_test"

@router.get("/{NSS}", response_description="Get lab results", status_code=status.HTTP_200_OK,
            response_model=LabTest)
def find_lab_test(request: Request, NSS: str):
    return find_one(request, {"NSS": NSS}, coll)

@router.post("/", response_description="Create a new lab test", status_code=status.HTTP_201_CREATED,
             response_model=bool)
def create_lab_test(request: Request, lab_test: LabTest = Body(...)):
    return insert_one(request, lab_test, coll)
