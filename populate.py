#!/usr/bin/env python3
import csv
import requests

BASE_URL = "http://localhost:8000"

def main():
    with open("/home/angeles_valencia/Proyecto Code/Data/patients_medicalhistory.csv") as fd:
        patients_csv = csv.DictReader(fd)
        for patient in patients_csv:
            patient["Historial_de_Consultas"] = patient["Historial_de_Consultas"].split("/")
            x = requests.post(BASE_URL+"/patient", json = patient)
            if not x.ok:
                print(f"Failed to post patient {x} - {patient}")

if __name__ == "__main__":
    main()