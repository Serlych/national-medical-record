#!/usr/bin/env python3
from fastapi import APIRouter, Body, Request, status

from lib.mongo import find_one, insert_one, update_one
from models.patient import Patient

router = APIRouter()
coll = "patient"


@router.get("/{nss}", response_description="Get a single patient", status_code=status.HTTP_200_OK,
            response_model=Patient)
def find_patient(request: Request, nss: str):
    find_criteria = {"nss": nss}
    return find_one(request, find_criteria, coll)


@router.post("/", response_description="Create a new patient", status_code=status.HTTP_201_CREATED,
             response_model=Patient)
def create_patient(request: Request, patient: Patient = Body(...)):
    return insert_one(request, patient, coll)


@router.post("/associate_checkup",
             response_description="Adds a single checkup to the list of a patient's checkups",
             status_code=status.HTTP_201_CREATED,
             response_model=Patient)
def associate_checkup_with_patient(request: Request, data=Body(...)):
    find_criteria = {"nss": data['nss']}
    update_one(request, find_criteria, {
        "$push": {
            "consultas": data['object_id']
        }
    }, coll)

    return find_one(request, find_criteria, coll)
