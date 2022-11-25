#!/usr/bin/env python3
import csv

from fastapi import requests

BASE_URL = "http://localhost:8000"


def main():
    # Colección de pacientes
    with open("./data/patients_medicalhistory.csv") as fd:
        patients_csv = csv.DictReader(fd)

        for patient in patients_csv:
            print(patient)
            # response = requests.post(BASE_URL + "/patient", json=patient)
            # if not response.ok:
            #     print(f"Failed to post patient {response} - {patient}")

    # Colección de consultas
    with open("./data/patient_checkupshistory.csv") as fd:
        consultations_csv = csv.DictReader(fd)

        for consultation in consultations_csv:
            print(consultation)

    # Colección de medicamentos
    with open("./data/patients_medshistory.csv") as fd:
        prescriptions_csv = csv.DictReader(fd)

        for row in prescriptions_csv:
            prescription = {
                "NSS": row['NSS'],
                "Consulta": "",
                "Medicamentos": {
                    "Nombre_del_Medicamento": row['Nombre_del_Medicamento'],
                    "Dosis_capsulas": row['Dosis_capsulas'],
                    "Gramaje_mg": row['Gramaje_mg'],
                    "Frecuencia_hrs": row['Frecuencia_hrs'],
                    "Duracion_dias": row['Duracion_dias']
                }
            }

            response = requests.post(BASE_URL + "/prescription", json=prescription)
            if not response.ok:
                print(f"Failed to post medication {response} - {row}")

    # Colección de pruebas clínicas
    with open("./data/patient_labshistory.csv") as fd:
        labtest_csv = csv.DictReader(fd)

        for labtest in labtest_csv:
            print(labtest)


if __name__ == "__main__":
    main()
