#!/usr/bin/env python3
from fastapi import APIRouter, Body, Request, status

from lib.mongo import find_one, insert_one, update_one

from models.patient import Patient, PatientUpdate

router = APIRouter()
coll = "patient"


@router.get("/{nss}", response_description="Get a single patient", status_code=status.HTTP_200_OK,
            response_model=Patient)
def get_patient(request: Request, nss: str):
    find_criteria = {"nss": nss}
    return find_one(request, find_criteria, coll)


@router.post("/", response_description="Create a new patient", status_code=status.HTTP_201_CREATED,
             response_model=Patient)
def create_patient(request: Request, patient: PatientUpdate = Body(...)):
    inserted = insert_one(request, patient, coll)
    return find_one(request, {'_id': inserted.inserted_id}, coll)


@router.post("/associate_checkup", response_description="Adds a single checkup to the list of a patient's checkups",
             status_code=status.HTTP_201_CREATED, response_model=Patient)
def associate_checkup_with_patient(request: Request, data=Body(...)):
    patient_find_criteria = {"nss": data['nss']}
    update_one(request, patient_find_criteria, {
        "$push": {
            "consultas": data['checkup_id']
        }
    }, coll)

    return find_one(request, patient_find_criteria, coll)
