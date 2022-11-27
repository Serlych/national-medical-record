#!/usr/bin/env python3
from fastapi import APIRouter, Body, Request, status
from bson.objectid import ObjectId
from typing import List, Tuple

from lib.mongo import insert_one, find_one, update_one, find_many

from models.checkup import Checkup

router = APIRouter()
coll = "checkup"


@router.get("/{nss}", response_description="Get all checkups for a patient", status_code=status.HTTP_200_OK,
            response_model=Tuple[List[Checkup], List[str]])
# response_model=List[Checkup])
def find_checkups(request: Request, nss: str):
    find_criteria = {"nss": nss}
    return find_many(request, find_criteria, coll)


@router.post("/", response_description="Create a new checkup", status_code=status.HTTP_201_CREATED,
             response_model=Checkup)
def create_checkup(request: Request, checkup: Checkup = Body(...)):
    return insert_one(request, checkup, coll)


@router.post("/associate_prescription",
             response_description="Adds a single prescription to the list of a checkup's prescriptions",
             status_code=status.HTTP_200_OK,
             response_model=Checkup)
def associate_prescription_with_checkup(request: Request, data=Body(...)):
    checkup_find_criteria = {"_id": ObjectId(data['checkup_id'])}
    update_one(request, checkup_find_criteria, {
        "$push": {
            "recetas": data['prescription_id']
        }
    }, coll)

    return find_one(request, checkup_find_criteria, coll)


@router.post("/associate_lab_test",
             response_description="Adds a single lab test to the list of a checkup's lab tests",
             status_code=status.HTTP_200_OK,
             response_model=Checkup)
def associate_lab_test_with_checkup(request: Request, data=Body(...)):
    checkup_find_criteria = {"_id": ObjectId(data['checkup_id'])}
    update_one(request, checkup_find_criteria, {
        "$push": {
            "pruebas_de_laboratorio": data['lab_test_id']
        }
    }, coll)

    return find_one(request, checkup_find_criteria, coll)
