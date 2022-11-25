#!/usr/bin/env python3
from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models.prescription import Prescription, PrescriptionUpdate

router = APIRouter()


@router.post("/", response_description="Post the info of a new medication", status_code=status.HTTP_201_CREATED,
             response_model=Prescription)
def create_prescription(request: Request, prescription: Prescription = Body(...)):
    # prescription = jsonable_encoder(prescription)
    print(prescription)
    # new_prescription = request.app.database["prescriptions"].insert_one(prescription)
    # created_prescription = request.app.database["prescriptions"].find_one(
    #     {"_id": new_prescription.inserted_id}
    # )

    # return created_prescription
