#!/usr/bin/env python3
from fastapi import APIRouter, Body, Request, status
from lib.mongo import find_one, insert_one, update_one

from models.patient import Patient, PatientUpdate

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

@router.post("/associate_checkups", response_description="Linking patient with checkups", status_code=status.HTTP_200_OK, 
             response_model=Patient)
def associate_checkup_with_patient(request, patient: Patient):
    find_criteria = {"nss": patient.nss}
    checkup = find_one(request, find_criteria, 'checkup')
    update_one(request, find_criteria, {"$push": {"consultas": checkup._id}}, coll)
    
    return find_one(request, find_criteria, coll)


