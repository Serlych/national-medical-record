#!/usr/bin/env python3
from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from bson.objectid import ObjectId
from typing import List, Tuple, Union

from lib.mongo import insert_one, find_one, find_many, update_one

from models.prescription import Prescription, PrescriptionUpdate

router = APIRouter()
coll = "prescription"


@router.get("/{nss}", response_description="Get all prescriptions for a patient", status_code=status.HTTP_200_OK,
            response_model=Tuple[List[Prescription], List[str]])
def find_precriptions(request: Request, nss: str):
    find_criteria = {"nss": nss}
    return find_many(request, find_criteria, coll)


@router.post("/", response_description="Create a new prescription", status_code=status.HTTP_201_CREATED,
             response_model=Union[Prescription, None])
def create_prescription(request: Request, prescription: Prescription = Body(...)):
    inserted = insert_one(request, prescription, coll)
    return find_one(request, {'_id': inserted.inserted_id}, coll)


@router.post("/associate_checkup",
             response_description="Links a checkup to the 'checkup' field for a prescription",
             status_code=status.HTTP_200_OK,
             response_model=Prescription)
def associate_checkup_with_prescription(request: Request, data=Body(...)):
    prescription_find_criteria = {"_id": ObjectId(data['prescription_id'])}
    update_one(request, prescription_find_criteria, {
        "$set": {
            "consulta": data['checkup_id']
        }
    }, coll)

    return find_one(request, prescription_find_criteria, coll)
