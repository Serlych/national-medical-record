#!/usr/bin/env python3
from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from lib.mongo import insert_one

from models.prescription import Prescription, PrescriptionUpdate

router = APIRouter()
coll = "prescription"


@router.post("/", response_description="Create a new prescription", status_code=status.HTTP_201_CREATED,
             response_model=Prescription)
def create_prescription(request: Request, prescription: Prescription = Body(...)):
    return insert_one(request, prescription, coll)
