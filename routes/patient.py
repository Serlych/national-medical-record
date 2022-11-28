#!/usr/bin/env python3
from fastapi import APIRouter, Body, Request, status

from lib.mongo import find_one, insert_one, update_one
from lib.input import filter_empty

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


@router.patch("/{nss}", response_description="Update an existing patient", status_code=status.HTTP_200_OK,
              response_model=Patient)
def update_patient(request: Request, nss: str, patient: PatientUpdate = Body(...)):
    patient_find_criteria = {"nss": nss}
    patient_dict = filter_empty(patient.dict())
    keys = patient_dict.keys()

    for key in keys:
        update_one(request, patient_find_criteria, {
            "$set": {
                f"{key}": patient_dict[key]
            }
        }, coll)

    return find_one(request, patient_find_criteria, coll)
