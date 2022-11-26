#!/usr/bin/env python3
import csv

from routes.patient import coll as patient_endpoint
from routes.checkup import coll as checkup_endpoint
from lib.http import get, post

import json


def main():
    # Associate checkups with patient
    with open(f"data/{patient_endpoint}.csv") as fd:
        names_csv = csv.DictReader(fd)

        for row in names_csv:
            patient_nss = row['nss']

            checkup_res = get(checkup_endpoint, patient_nss)
            [checkups, checkup_object_ids] = json.loads(checkup_res)

            for object_id in checkup_object_ids:
                post(patient_endpoint, {'nss': patient_nss, 'object_id': object_id}, 'associate_checkup')


if __name__ == "__main__":
    main()
