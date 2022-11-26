#!/usr/bin/env python3
import argparse
import logging
import os

import requests

# Set logger
log = logging.getLogger()
log.setLevel('INFO')
handler = logging.FileHandler('nmr.log')
handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
log.addHandler(handler)

# Read env vars related to API connection
NMR_API_URL = os.getenv("NMR_API_URL", "http://localhost:8000")

def printer(object):
    for k in object.keys():
        print(f"{k}: {object[k]}")
    print("="*50)

def get_patient(nss):
    suffix = f"/patient/{nss}"
    endpoint = NMR_API_URL + suffix
    response = requests.get(endpoint)
    if response.ok:
        json_resp = response.json()
        printer(json_resp)
    else:
        print(f"Error: {response}")

def post_patient():
    suffix = "/patient"
    endpoint = NMR_API_URL + suffix

    assoc_checkup_suffix = "/patient/associate_checkup"
    checkup_endpoint = NMR_API_URL + assoc_checkup_suffix

    patient = {
        "nss": "68c9eb13-a596-43ec-a5d4-984fe0a42f9e",
        "nombre": "Hector",
        "apellidos": "Merino",
        "edad": 35,
        "fecha_de_nacimiento": "06/09/1998 00:00",
        "ciudad_de_nacimiento": "Guadalajara",
        "tipo_de_sangre": "A+",
        "imc": 41.42,
        "alergias": ["Gluten"],
        "ultima_consulta": "29/09/2013 00:00",
        "padecimientos": ["Cirrosis"],
        "consultas": []
    }
    response = requests.post(endpoint, json=patient)
    if response.ok:
        print("Patient posted")
        requests.post(checkup_endpoint, json=patient)
    else:
        print(f"Error: {response}")

def update_patient(nss):
    suffix = f"/patient/{nss}"
    endpoint = NMR_API_URL + suffix
    patient = {
        "imc": 25.5
    }
    response = requests.put(endpoint, json=patient)
    if response.ok:
        print("Patient updated")
    else:
        print(f"Error: {response}")

def get_checkup(nss):
    suffix = f"/checkup/{nss}"
    endpoint = NMR_API_URL + suffix
    response = requests.get(endpoint)
    if response.ok:
        json_resp = response.json()
        printer(json_resp)
    else:
        print(f"Error: {response}")

def post_checkup():
    suffix = "/checkup"
    endpoint = NMR_API_URL + suffix

    assoc_prescription_suffix = "/checkup/associate_prescription"
    prescription_endpoint = NMR_API_URL + assoc_prescription_suffix

    assoc_lab_test_suffix = "/checkup/associate_lab_test"
    lab_test_endpoint = NMR_API_URL + assoc_lab_test_suffix

    checkup = {
                "nss": "68c9eb13-a596-43ec-a5d4-984fe0a42f9e",
                "fecha": "27/05/2022 00:00",
                "medico_tratante": "Dr. Carmen Robledo",
                "cedula_profesional": "57918810",
                "diagnostico": "Gastritis",
                "recetas": [],
                "pruebas_de_laboratorio": []
            }
    response = requests.post(endpoint, json=checkup)
    if response.ok:
        print("Checkup posted")
        requests.post(prescription_endpoint, json=checkup)
        requests.post(lab_test_endpoint, json=checkup)
    else:
        print(f"Error: {response}")

def get_prescription(nss):
    suffix = f"/prescription/{nss}"
    endpoint = NMR_API_URL + suffix
    response = requests.get(endpoint)
    if response.ok:
        json_resp = response.json()
        printer(json_resp)
    else:
        print(f"Error: {response}")

def post_prescription():
    suffix = "/prescription"
    endpoint = NMR_API_URL + suffix

    assoc_checkup_suffix = "/prescription/associate_checkup"
    checkup_endpoint = NMR_API_URL + assoc_checkup_suffix

    prescription = {
            "nss": "68c9eb13-a596-43ec-a5d4-984fe0a42f9e",
            "consulta": "",
            "medicamentos": [{
                          "nombre": "AMOXICILINA",
                          "dosis": 0,
                          "gramaje": 19,
                          "frecuencia": 65,
                          "duracion": 39
                          }]
         }
    response = requests.post(endpoint, json=prescription)
    if response.ok:
        print("Prescription posted")
        requests.post(checkup_endpoint, json=prescription)
    else:
        print(f"Error: {response}")

def get_lab_test(nss):
    suffix = f"/lab_test/{nss}"
    endpoint = NMR_API_URL + suffix
    response = requests.get(endpoint)
    if response.ok:
        json_resp = response.json()
        printer(json_resp)
    else:
        print(f"Error: {response}")

def post_lab_test():
    suffix = "/lab_test"
    endpoint = NMR_API_URL + suffix

    assoc_checkup_suffix = "/lab_test/associate_checkup"
    checkup_endpoint = NMR_API_URL + assoc_checkup_suffix

    lab_test = {
                "nss": "68c9eb13-a596-43ec-a5d4-984fe0a42f9e",
                "consulta": "",
                "pruebas": [{
                    "nombre": "Colesterol",
                    "fecha": "27/03/2022 00:00",
                    "url": "www.laboratorio.com/resultados"
                }]
            }
    response = requests.post(endpoint, json=lab_test)
    if response.ok:
        print("Lab test posted")
        requests.post(checkup_endpoint, json=lab_test)
    else:
        print(f"Error: {response}")



def main():
    log.info(f"Historial Médico Nacional. App requests to: {NMR_API_URL}")

    parser = argparse.ArgumentParser()

    list_of_actions = ["buscar paciente", "agregar paciente", "actualizar paciente",
                        "buscar consulta", "agregar consulta", "buscar recetas", 
                        "agregar receta", "buscar resultados de laboratorio", "agregar prueba de laboratorio"]

    parser.add_argument("action",
                        choices=list_of_actions,
                        help="Acciones a realizar por la aplicación")
    parser.add_argument("-n", "--nss",
                        help="Proporcionar un NSS relacionado con la acción que desea",
                        default=None)

    args = parser.parse_args()

    if args.action == "buscar paciente" and args.nss:
        get_patient(args.nss)
    elif args.action == "agregar paciente" and args.nss:
        post_patient()
    elif args.action == "actualizar paciente" and args.nss:
        update_patient(args.nss)
    elif args.action == "buscar consulta" and args.nss:
        get_checkup(args.nss)
    elif args.action == "agregar consulta" and args.nss:
        post_checkup()        
    elif args.action == "buscar recetas" and args.nss:
        get_prescription(args.nss)
    elif args.action == "agregar receta" and args.nss:
        post_prescription() 
    elif args.action == "buscar resultados de laboratorio" and args.nss:
        get_lab_test(args.nss)
    elif args.action == "agregar prueba de laboratorio" and args.nss:
        post_lab_test()  



if __name__ == "__main__":
    main()
