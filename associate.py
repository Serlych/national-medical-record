#!/usr/bin/env python3
import csv
import requests

from routes.patient import coll as patient_endpoint
from routes.checkup import coll as checkup_endpoint
from routes.prescription import coll as prescription_endpoint
from routes.lab_test import coll as lab_test_endpoint

BASE_URL = "http://localhost:8000"


def post(endpoint, data):
    response = requests.post(BASE_URL + f"/{endpoint}", json=data)

    if not response.ok:
        print(f"Failed to post {endpoint} {response.text} - {data}")
    else:
        print(f"Posted {endpoint} succesfully for NSS: {data['nss']}")


def main():
    # get de la consulta
    # consutlta.nss
    post('/checkup/associate_prescription')


if __name__ == "__main__":
    main()
