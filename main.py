#!/usr/bin/env python3
import os

from fastapi import FastAPI
from pymongo import MongoClient

from routes.patient import router as patient_router
from routes.checkup import router as checkup_router
from routes.prescription import router as prescription_router
from routes.lab_test import router as lab_test_router

from routes.patient import coll as patient_endpoint
from routes.checkup import coll as checkup_endpoint
from routes.prescription import coll as prescription_endpoint
from routes.lab_test import coll as lab_test_endpoint

MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb+srv://test:test@national-medical-record.34mgqxn.mongodb.net/test')
DB_NAME = os.getenv('MONGODB_DB_NAME', 'HMN')  # Historial médico nacional

app = FastAPI()


@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(MONGODB_URI)
    app.database = app.mongodb_client[DB_NAME]
    print(f"Connected to MongoDB at: {MONGODB_URI} \n\t Database: {DB_NAME}")


@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()
    print(f"Connection to MongoDB at: {MONGODB_URI} is now closed")


app.include_router(patient_router, tags=[patient_endpoint], prefix=f"/{patient_endpoint}")
app.include_router(checkup_router, tags=[checkup_endpoint], prefix=f"/{checkup_endpoint}")
app.include_router(prescription_router, tags=[prescription_endpoint], prefix=f"/{prescription_endpoint}")
app.include_router(lab_test_router, tags=[lab_test_endpoint], prefix=f"/{lab_test_endpoint}")
