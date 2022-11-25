#!/usr/bin/env python3
from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from lib.mongo import insert_one, find_one

from models.prescription import Prescription, PrescriptionUpdate

router = APIRouter()
coll = "prescription"

@router.get("/{NSS}", response_description="Get prescription info", status_code=status.HTTP_200_OK,
            response_model=Prescription)
def find_precription(request: Request, NSS: str):
    return find_one(request, {"NSS": NSS}, coll)

@router.post("/", response_description="Create a new prescription", status_code=status.HTTP_201_CREATED,
             response_model=bool)
def create_prescription(request: Request, prescription: Prescription = Body(...)):
    return insert_one(request, prescription, coll)
