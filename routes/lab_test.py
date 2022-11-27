#!/usr/bin/env python3
from fastapi import APIRouter, Body, Request, status
from bson.objectid import ObjectId
from typing import List, Tuple, Union

from lib.mongo import insert_one, find_one, find_many, update_one

from models.lab_test import LabTest, LabTestUpdate

router = APIRouter()
coll = "lab_test"


@router.get("/{nss}", response_description="Get all lab tests for a patient", status_code=status.HTTP_200_OK,
            response_model=Tuple[List[LabTest], List[str]])
def find_lab_tests(request: Request, nss: str):
    find_criteria = {"nss": nss}
    return find_many(request, find_criteria, coll)


@router.post("/", response_description="Create a new lab test", status_code=status.HTTP_201_CREATED,
             response_model=LabTest)
def create_lab_test(request: Request, lab_test: LabTest = Body(...)):
    return insert_one(request, lab_test, coll)


@router.post("/associate_checkup",
             response_description="Links a checkup to the 'checkup' field for a lab test",
             status_code=status.HTTP_200_OK,
             response_model=LabTest)
def associate_checkup_with_lab_test(request: Request, data=Body(...)):
    lab_test_find_criteria = {"_id": ObjectId(data['lab_test_id'])}
    update_one(request, lab_test_find_criteria, {
        "$set": {
            "consulta": data['checkup_id']
        }
    }, coll)

    return find_one(request, lab_test_find_criteria, coll)
