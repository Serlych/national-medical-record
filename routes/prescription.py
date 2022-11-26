#!/usr/bin/env python3
from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from lib.mongo import insert_one, find_one, update_one
from typing import Union

from models.prescription import Prescription, PrescriptionUpdate

router = APIRouter()
coll = "prescription"


@router.get("/{nss}", response_description="Get prescription info", status_code=status.HTTP_200_OK,
            response_model=Union[Prescription, None])
def find_precription(request: Request, nss: str):
    find_criteria = {"nss": nss}
    return find_one(request, find_criteria, coll)


@router.post("/", response_description="Create a new prescription", status_code=status.HTTP_201_CREATED,
             response_model=Union[Prescription, None])
def create_prescription(request: Request, prescription: Prescription = Body(...)):
    find_criteria = {"nss": prescription.nss}
    update_criteria = {"$push": {"medicamentos": prescription.medicamentos[0]}}

    if (existing_prescription := find_one(request, find_criteria, coll)) is not None:
        update_one(request, find_criteria, update_criteria, coll)
        return existing_prescription

    insert_one(request, prescription, coll)
    return find_one(request, find_criteria, coll)


@router.post("/")
def associate_checkup_with_prescription(request, prescription: Prescription):
    find_criteria = {"nss": prescription.nss}
    checkup = find_one(request, find_criteria, 'checkup')
    update_one(request, find_criteria, {"$set": {"consulta": checkup._id}}, coll)

    return find_one(request, find_criteria, coll)
