#!/usr/bin/env python3
import csv

from fastapi import requests

BASE_URL = "http://localhost:8000"


def main():
    # Colección de pacientes
    with open("./data/patients_medicalhistory.csv") as fd:
        patients_csv = csv.DictReader(fd)

        for row in patients_csv:
            patient = {
                "NSS": row['NSS'],
                "Nombre": row['Nombre'],
                "Apellidos": row['Apellidos'],
                "Edad": row['Edad'],
                "Fecha_de_Nacimiento": row['Fecha_de_Nacimiento'],
                "Ciudad_de_Nacimiento": row['Ciudad_de_Nacimiento'],
                "Tipo_de_Sangre": row['Tipo_de_Sangre'],
                "IMC": row['IMC'],
                "Alergias": row['Alergias'].split(),
                "Ultima_Consulta": row["Ultima_Consulta"],
                "Padecimientos": row['Padecimientos'].split(),
                "Historial_de_Consultas": row["Historial_de_Consultas"].split('/')
            }

            print(patient)
            # response = requests.post(BASE_URL + "/patient", json=patient)
            # if not response.ok:
            #     print(f"Failed to post patient {response} - {row}")

    # Colección de consultas
    with open("./data/patient_checkupshistory.csv") as fd:
        checkups_csv = csv.DictReader(fd)

        for row in checkups_csv:
            checkup = {
                "NSS": row['NSS'],
            }

    # Colección de medicamentos
    with open("./data/patients_medshistory.csv") as fd:
        prescriptions_csv = csv.DictReader(fd)

        for row in prescriptions_csv:
            prescription = {
                "NSS": row['NSS'],
                "Consulta": "any",
                "Medicamentos": {
                    "Nombre_del_Medicamento": row['Nombre_del_Medicamento'],
                    "Dosis_capsulas": row['Dosis_capsulas'],
                    "Gramaje_mg": row['Gramaje_mg'],
                    "Frecuencia_hrs": row['Frecuencia_hrs'],
                    "Duracion_dias": row['Duracion_dias']
                }
            }

            # response = requests.post(BASE_URL + "/prescription", json=prescription)
            # if not response.ok:
            #     print(f"Failed to post medication {response} - {row}")

    # Colección de pruebas clínicas
    with open("./data/patient_labshistory.csv") as fd:
        lab_tests_csv = csv.DictReader(fd)

        for row in lab_tests_csv:
            print(row)


if __name__ == "__main__":
    main()
