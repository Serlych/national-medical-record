#!/usr/bin/env python3
import csv

from routes.patient import coll as patient_endpoint
from routes.checkup import coll as checkup_endpoint
from lib.http import get, post

import json


def main():
    with open(f"data/names.csv") as fd:
        names_csv = csv.DictReader(fd)

        for row in names_csv:
            patient_nss = row['nss']

            res = get(checkup_endpoint, patient_nss)
            [checkups, object_ids] = json.loads(res)

            for object_id in object_ids:
                a = post(patient_endpoint, {'nss': patient_nss, 'object_id': object_id}, 'associate_checkup')
                print(a)

            break

    # post('/checkup/associate_prescription')


if __name__ == "__main__":
    main()
