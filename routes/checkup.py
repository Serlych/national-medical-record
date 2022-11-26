#!/usr/bin/env python3
from fastapi import APIRouter, Body, Request, status
from lib.mongo import insert_one, find_one, update_one, find_many
from typing import List

from models.checkup import Checkup

router = APIRouter()
coll = "checkup"


@router.get("/{nss}", response_description="Get all checkups for a patient", status_code=status.HTTP_200_OK,
            response_model=List[Checkup])
def find_checkup(request: Request, nss: str):
    find_criteria = {"nss": nss}
    return find_many(request, find_criteria, coll)


@router.post("/", response_description="Create a new checkup", status_code=status.HTTP_201_CREATED,
             response_model=Checkup)
def create_checkup(request: Request, checkup: Checkup = Body(...)):
    return insert_one(request, checkup, coll)


@router.post("/associate_prescription", response_description="Linking prescription with checkup",
             status_code=status.HTTP_200_OK,
             response_model=Checkup)
def associate_prescription_with_checkup(request, checkup: Checkup):
    find_criteria = {"nss": checkup.nss}
    prescription = find_one(request, find_criteria, 'prescription')
    update_one(request, find_criteria, {"$push": {"recetas": prescription._id}}, coll)

    return find_one(request, find_criteria, coll)


@router.post("/associate_lab_test", response_description="Linking lab tests with checkup",
             status_code=status.HTTP_200_OK,
             response_model=Checkup)
def associate_lab_test_with_checkup(request, checkup: Checkup):
    find_criteria = {"nss": checkup.nss}
    lab_test = find_one(request, find_criteria, 'lab_test')
    update_one(request, find_criteria, {"$push": {"pruebas_de_laboratorio": lab_test._id}}, coll)

    return find_one(request, find_criteria, coll)
