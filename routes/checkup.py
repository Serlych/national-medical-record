#!/usr/bin/env python3
from fastapi import APIRouter, Body, Request, status
from lib.mongo import insert_one, find_one, update_one

from models.checkup import Checkup

router = APIRouter()
coll = "checkup"


@router.get("/{nss}", response_description="Get checkup info", status_code=status.HTTP_200_OK,
            response_model=Checkup)
def find_checkup(request: Request, nss: str):
    find_criteria = {"nss": nss}
    return find_one(request, find_criteria, coll)


@router.post("/", response_description="Create a new checkup", status_code=status.HTTP_201_CREATED,
             response_model=Checkup)
def create_checkup(request: Request, checkup: Checkup = Body(...)):
    return insert_one(request, checkup, coll)


@router.post("/associate_prescription")
@router.post("/", response_description="Linking prescription with checkup", status_code=status.HTTP_200_OK, 
             response_model=bool)
def associate_prescription_with_checkup(request, checkup: Checkup):
    find_criteria = {"nss": checkup.nss}
    prescription = find_one(request, find_criteria, 'prescription')
    return update_one(request, find_criteria, {"$push": {"recetas": prescription._id}}, coll)

@router.post("/")
def associate_labTests_with_checkup(request, checkup: Checkup):
    find_criteria = {"nss": checkup.nss}
    lab_test = find_one(request, find_criteria, 'lab_test')
    update_one(request, find_criteria, {"$push": {"pruebas_de_laboratorio": lab_test._id}}, coll)

    return find_one(request, find_criteria, coll)
