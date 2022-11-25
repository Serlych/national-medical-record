#!/usr/bin/env python3
import csv
import requests

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
                "NSS": row["NSS"],
                "Nombre": row["Nombre"],
                "Apellidos": row["Apellidos"],
                "Edad": row["Edad"],
                "Fecha de Nacimiento": row["Fecha_de_Nacimiento"],
                "Ciudad de Nacimiento": row["Ciudad_de_Nacimiento"],
                "Tipo de Sangre": row["Tipo_de_Sangre"],
                "IMC": row["IMC"],
                "Alergias": row["Alergias"].split(),
                "Ultima Consulta": row["Ultima_Consulta"],
                "Padecimientos": row["Padecimientos"].split(),
                "Historial de Consultas": row["Historial_de_Consultas"].split("/")
            }

            post("patient", patient)

    # Colección de consultas
    with open("./data/patient_checkupshistory.csv") as fd:
        checkups_csv = csv.DictReader(fd)

        for row in checkups_csv:
            checkup = {
                "NSS": row["NSS"],
                "Fecha": row["Fecha"],
                "Medico Tratante": row["Nombre_del_Medico"],
                "Cedula Profesional": row["Cedula_Profesional"],
                "Diagnostico": row["Diagnostico"],
                "Receta": [],
                "Pruebas de Laboratorio": []
            }

            post("checkup", checkup)

    # Colección de medicamentos
    with open("./data/Meds.csv") as fd:
        prescriptions_csv = csv.DictReader(fd)

        for row in prescriptions_csv:
            prescription = {
                "NSS": row["NSS"],
                "Consulta": "any",
                "Medicamentos": {
                    "Nombre del Medicamento": row["Nombre_del_Medicamento"],
                    "Dosis (capsulas)": row["Dosis_capsulas"],
                    "Gramaje (mg)": row["Gramaje_mg"],
                    "Frecuencia (c/hrs)": row["Frecuencia_hrs"],
                    "Duracion (dias)": row["Duracion_dias"]
                }
            }

            post("prescription", prescription)

    # Colección de pruebas clínicas
    with open("./data/patient_labshistory.csv") as fd:
        lab_tests_csv = csv.DictReader(fd)

        for row in lab_tests_csv:
            lab_test = {
                "NSS": row["NSS"],
                "Consulta": "any",
                "Pruebas": [{
                    "Nombre de la Prueba": row["Pruebas de Laboratorio"],
                    "Fecha": row["Fecha de Consulta"],
                    "URL de Resultados": "cdn.lab-test-results.com/test_url"
                }]
            }

            post("lab_test", lab_test)


if __name__ == "__main__":
    main()
