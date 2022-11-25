#!/usr/bin/env python3
import csv

import requests

BASE_URL = "http://localhost:8000"


def main():
    with open("/home/angeles_valencia/national-medical-record/data/Meds.csv") as fd2:
            meds_csv = csv.DictReader(fd2)

            for row in meds_csv:
                medinfo = dict(Nombre_del_Medicamento = row['Nombre_del_Medicamento'], Dosis_capsulas = row['Dosis_capsulas'],
                            Gramaje_mg = row['Gramaje_mg'], Frecuencia_hrs = row['Frecuencia_hrs'], Duracion_dias = row ['Duracion_dias'])
                row['Medicamento'] = [medinfo]
                row['Consulta'] = 'test'
                removes = ['Nombre_del_Medicamento', 'Dosis_capsulas', 'Gramaje_mg', 'Frecuencia_hrs', 'Duracion_dias']
                for i in removes:
                    row.pop(i)
                x = requests.post(BASE_URL + "/presc", json=row)
                #print(row)
                if not x.ok:
                    print(f"Failed to post medication {x} - {row}")                    


if __name__ == "__main__":
    main()
