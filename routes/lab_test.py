#!/usr/bin/env python3
from fastapi import APIRouter, Body, Request, status
from lib.mongo import insert_one, find_one, update_one

from models.lab_test import LabTest, LabTestUpdate

router = APIRouter()
coll = "lab_test"


@router.get("/{nss}", response_description="Get lab results", status_code=status.HTTP_200_OK,
            response_model=LabTest)
def find_lab_test(request: Request, nss: str):
    find_criteria = {"nss": nss}
    return find_one(request, find_criteria, coll)


@router.post("/", response_description="Create a new lab test", status_code=status.HTTP_201_CREATED,
             response_model=LabTest)
def create_lab_test(request: Request, lab_test: LabTest = Body(...)):
    return insert_one(request, lab_test, coll)


@router.post("/")
def associate_checkup_with_lab_test(request, lab_test: LabTest):
    find_criteria = {"nss": lab_test.nss}
    checkup = find_one(request, find_criteria, 'checkup')
    return update_one(request, find_criteria, {"$set": {"consulta": checkup._id}}, coll)
