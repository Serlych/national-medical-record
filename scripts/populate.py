#!/usr/bin/env python3
import csv

from routes.patient import coll as patient_endpoint
from routes.checkup import coll as checkup_endpoint
from routes.prescription import coll as prescription_endpoint
from routes.lab_test import coll as lab_test_endpoint

from lib.http import post


def main():
    # Colección de pacientes
    with open(f"data/{patient_endpoint}.csv") as fd:
        patients_csv = csv.DictReader(fd)

        for row in patients_csv:
            patient = {
                "nss": row["nss"],
                "nombre": row["nombre"],
                "apellidos": row["apellidos"],
                "edad": row["edad"],
                "fecha_de_nacimiento": row["fecha_de_nacimiento"],
                "ciudad_de_nacimiento": row["ciudad_de_nacimiento"],
                "tipo_de_sangre": row["tipo_de_sangre"],
                "imc": row["imc"],
                "alergias": row["alergias"].split(),
                "padecimientos": row["padecimientos"].split(),
            }

            post(patient_endpoint, patient)

    # Colección de consultas
    with open(f"data/{checkup_endpoint}.csv") as fd:
        checkups_csv = csv.DictReader(fd)

        for row in checkups_csv:
            checkup = {
                "nss": row["nss"],
                "fecha": row["fecha"],
                "medico_tratante": row["medico_tratante"],
                "cedula_profesional": row["cedula_profesional"],
                "diagnostico": row["diagnostico"],
                "recetas": [],
                "pruebas_de_laboratorio": []
            }

            post(checkup_endpoint, checkup)

    # Colección de medicamentos
    with open(f"data/{prescription_endpoint}.csv") as fd:
        prescriptions_csv = csv.DictReader(fd)

        # find_criteria = {"nss": prescription.nss}
        # update_criteria = {"$push": {"medicamentos": prescription.medicamentos[0]}}
        #
        # if (existing_prescription := find_one(request, find_criteria, coll)) is not None:
        #     update_one(request, find_criteria, update_criteria, coll)
        #     return existing_prescription
        #
        # insert_one(request, prescription, coll)
        # return find_one(request, find_criteria, coll)
        for row in prescriptions_csv:
            prescription = {
                "nss": row["nss"],
                "consulta": "",
                "medicamentos": [{
                    "nombre": row["nombre"],
                    "dosis": float(row["dosis"]),
                    "gramaje": int(row["gramaje"]),
                    "frecuencia": int(row["frecuencia"]),
                    "duracion": int(row["duracion"])
                }]
            }

            post(prescription_endpoint, prescription)

    # Colección de pruebas clínicas
    with open(f"data/{lab_test_endpoint}.csv") as fd:
        lab_tests_csv = csv.DictReader(fd)

        for row in lab_tests_csv:
            lab_test = {
                "nss": row["nss"],
                "consulta": "",
                "pruebas": [{
                    "nombre": row["nombre"],
                    "fecha": row["fecha"],
                    "url": "cdn.lab-test-results.com/test_url"
                }]
            }

            post(lab_test_endpoint, lab_test)


if __name__ == "__main__":
    main()
