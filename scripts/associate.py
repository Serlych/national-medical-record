#!/usr/bin/env python3
import csv
import json

from routes.checkup import coll as checkup_endpoint
from routes.patient import coll as patient_endpoint
from routes.prescription import coll as prescription_endpoint
from routes.lab_test import coll as lab_test_endpoint

from lib.http import get, post


def main():
    # Associate checkups with patient
    with open(f"data/{patient_endpoint}.csv") as fd:
        names_csv = csv.DictReader(fd)

        for row in names_csv:
            patient_nss = row['nss']

            checkup_res = get(checkup_endpoint, patient_nss)
            checkups = json.loads(checkup_res)

            for checkup_id in checkups:
                post(patient_endpoint, {'nss': patient_nss, 'checkup_id': checkup_id}, 'associate_checkup')

    # Associate prescription with checkup
    with open(f"data/{patient_endpoint}.csv") as fd:
        names_csv = csv.DictReader(fd)

        for row in names_csv:
            patient_nss = row['nss']

            checkup_res = get(checkup_endpoint, patient_nss)
            checkups = json.loads(checkup_res)

            prescription_res = get(prescription_endpoint, patient_nss)
            prescriptions = json.loads(prescription_res)

            checkup_id = checkups[0]
            prescription_id = prescriptions[0]

            post(checkup_endpoint, {
                'checkup_id': checkup_id,
                'prescription_id': prescription_id
            }, 'associate_prescription')

    # Associate lab test with checkup
    with open(f"data/{patient_endpoint}.csv") as fd:
        names_csv = csv.DictReader(fd)

        for row in names_csv:
            patient_nss = row['nss']

            checkup_res = get(checkup_endpoint, patient_nss)
            checkups = json.loads(checkup_res)

            lab_test_res = get(lab_test_endpoint, patient_nss)
            lab_tests = json.loads(lab_test_res)

            if len(lab_tests) == 0:
                continue

            checkup_id = checkups[0]
            lab_test_id = lab_tests[0]

            post(checkup_endpoint, {
                'checkup_id': checkup_id,
                'lab_test_id': lab_test_id
            }, 'associate_lab_test')

    # Associate checkup with prescription
    with open(f"data/{patient_endpoint}.csv") as fd:
        names_csv = csv.DictReader(fd)

        for row in names_csv:
            patient_nss = row['nss']

            checkup_res = get(checkup_endpoint, patient_nss)
            checkups = json.loads(checkup_res)

            prescription_res = get(prescription_endpoint, patient_nss)
            [_, prescription_object_ids] = json.loads(prescription_res)

            if len(prescription_object_ids) == 0:
                continue

            checkup_id = checkups[0]
            prescription_id = prescription_object_ids[0]

            post(prescription_endpoint, {
                'checkup_id': checkup_id,
                'prescription_id': prescription_id
            }, 'associate_checkup')

    # Associate checkup with lab test
    with open(f"data/{patient_endpoint}.csv") as fd:
        names_csv = csv.DictReader(fd)

        for row in names_csv:
            patient_nss = row['nss']

            checkup_res = get(checkup_endpoint, patient_nss)
            checkups = json.loads(checkup_res)

            lab_test_res = get(lab_test_endpoint, patient_nss)
            lab_tests = json.loads(lab_test_res)

            if len(lab_tests) == 0:
                continue

            checkup_id = checkups[0]
            lab_test_id = lab_tests[0]

            post(lab_test_endpoint, {
                'checkup_id': checkup_id,
                'lab_test_id': lab_test_id
            }, 'associate_checkup')


if __name__ == "__main__":
    main()
