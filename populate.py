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
        print(f"Failed to post {endpoint} {response} - {data}")


def main():
    # Colección de pacientes
    with open("./data/patients_medicalhistory.csv") as fd:
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
                "ultima_consulta": row["ultima_consulta"],
                "padecimientos": row["padecimientos"].split(),
                "consultas": row["consultas"].split("/")
            }

            post(patient_endpoint, patient)

    # Colección de consultas
    with open("./data/patient_checkupshistory.csv") as fd:
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
    with open("./data/Meds.csv") as fd:
        prescriptions_csv = csv.DictReader(fd)

        for row in prescriptions_csv:
            prescription = {
                "nss": row["NSS"],
                "consulta": "any",
                "medicamentos": {
                    "nombre": row["nombre"],
                    "dosis": row["dosis"],
                    "gramaje": row["gramaje"],
                    "frecuencia": row["frecuencia"],
                    "duracion": row["duracion"]
                }
            }

            post(prescription_endpoint, prescription)

    # Colección de pruebas clínicas
    with open("./data/patient_labshistory.csv") as fd:
        lab_tests_csv = csv.DictReader(fd)

        for row in lab_tests_csv:
            lab_test = {
                "nss": row["nss"],
                "consulta": "any",
                "pruebas": [{
                    "nombre": row["nombre"],
                    "fecha": row["fecha"],
                    "url": "cdn.lab-test-results.com/test_url"
                }]
            }

            post(lab_test_endpoint, lab_test)


if __name__ == "__main__":
    main()
