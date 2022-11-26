#!/usr/bin/env python3
import argparse
import logging
import os

import requests

from utils import print_book, filter_none

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

# def post_patient(nss):
#     suffix = f"/patient/{nss}"
#     endpoint = NMR_API_URL + suffix
#     patient = {
#         "nss": "68c9eb13-a596-43ec-a5d4-984fe0a42f9e",
#         "nombre": "Hector",
#         "apellidos": "Merino",
#         "edad": 35,
#         "fecha_de_nacimiento": "06/09/1998 00:00",
#         "ciudad_de_nacimiento": "Guadalajara",
#         "tipo_de_sangre": "A+",
#         "imc": 41.42,
#         "alergias": ["Gluten"],
#         "ultima_consulta": "29/09/2013 00:00",
#         "padecimientos": ["Cirrosis"],
#         "consultas": ["objectId"]
#     }
#     response = requests.post(endpoint, json=patient)
#     if response.ok:
#         print("Patient posted")
#     else:
#         print(f"Error: {response}")

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

# def post_checkup(nss):
#     suffix = f"/checkup/{nss}"
#     endpoint = NMR_API_URL + suffix
#     checkup = {
#                 "nss": "68c9eb13-a596-43ec-a5d4-984fe0a42f9e",
#                 "fecha": "27/05/2022 00:00",
#                 "medico_tratante": "Dr. Carmen Robledo",
#                 "cedula_profesional": "57918810",
#                 "diagnostico": "Gastritis",
#                 "recetas": ["objectId"],
#                 "pruebas_de_laboratorio": ["objectId"]
#             }
#     response = requests.post(endpoint, json=checkup)
#     if response.ok:
#         print("Checkup posted")
#     else:
#         print(f"Error: {response}")

def get_prescription(nss):
    suffix = f"/prescription/{nss}"
    endpoint = NMR_API_URL + suffix
    response = requests.get(endpoint)
    if response.ok:
        json_resp = response.json()
        printer(json_resp)
    else:
        print(f"Error: {response}")

# def post_prescription(nss):
#     suffix = f"/prescription/{nss}"
#     endpoint = NMR_API_URL + suffix
#     prescription = {
#             "nss": "68c9eb13-a596-43ec-a5d4-984fe0a42f9e",
#             "consulta": "objectId",
#             "medicamentos": [{
#                           "nombre": "AMOXICILINA",
#                           "dosis": 0,
#                           "gramaje": 19,
#                           "frecuencia": 65,
#                           "duracion": 39
#                           }]
#          }
#     response = requests.post(endpoint, json=prescription)
#     if response.ok:
#         print("Prescription posted")
#     else:
#         print(f"Error: {response}")

def get_lab_test(nss):
    suffix = f"/lab_test/{nss}"
    endpoint = NMR_API_URL + suffix
    response = requests.get(endpoint)
    if response.ok:
        json_resp = response.json()
        printer(json_resp)
    else:
        print(f"Error: {response}")

# def post_lab_test(nss):
#     suffix = f"/lab_test/{nss}"
#     endpoint = NMR_API_URL + suffix
#     lab_test = {
#                 "nss": "68c9eb13-a596-43ec-a5d4-984fe0a42f9e",
#                 "consulta": "objectId",
#                 "pruebas": [{
#                     "nombre": "Colesterol",
#                     "fecha": "27/03/2022 00:00",
#                     "url": "www.laboratorio.com/resultados"
#                 }]
#             }
#     response = requests.post(endpoint, json=lab_test)
#     if response.ok:
#         print("Lab test posted")
#     else:
#         print(f"Error: {response}")



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
    # parser.add_argument("-r", "--rating",
    #                     help="Search parameter to look for books with average rating equal or above the param (0 to 5)",
    #                     default=None)
    # parser.add_argument("-p", "--pagenum",
    #                     help="Search by number of pages",
    #                     default=None)
    # parser.add_argument("-l", "--limit",
    #                     help="Limit the search to the specified amount",
    #                     default=None)
    # parser.add_argument("-s", "--skip",
    #                     help="Offset the search results by the specified amount",
    #                     default=0)
    # parser.add_argument("-t", "--title",
    #                     help="Search by book title",
    #                     default=None)

    args = parser.parse_args()

    # if args.action == "search":
    #     if args.id:
    #         log.error(f"Can't use argument id with action {args.action}")
    #         exit(1)

    # else:
    #     if args.rating:
    #         log.error("Rating argument can only be used with search action")
    #         exit(1)

    #     if args.limit:
    #         log.error("Limit argument can only be used with search action")
    #         exit(1)

    #     if args.skip:
    #         log.error("Skip argument can only be used with search action")
    #         exit(1)

    #     if args.pagenum:
    #         log.error("Page number argument can only be used with search action")
    #         exit(1)

    #     if args.title:
    #         log.error("Title argument can only be used with search action")
    #         exit(1)

    if args.action == "buscar paciente" and args.nss:
        get_patient(args.nss)
    # elif args.action == "agregar paciente" and args.nss:
    #     post_patient(args.id)
    elif args.action == "actualizar paciente" and args.nss:
        update_patient(args.nss)
    elif args.action == "buscar consulta" and args.nss:
        get_checkup(args.nss)
    # elif args.action == "agregar consulta" and args.nss:
    #     post_checkup(args.id)        
    elif args.action == "buscar recetas" and args.nss:
        get_prescription(args.nss)
    # elif args.action == "agregar receta" and args.nss:
    #     post_prescription(args.id) 
    elif args.action == "buscar resultados de laboratorio" and args.nss:
        get_lab_test(args.nss)
    # elif args.action == "agregar prueba de laboratorio" and args.nss:
    #     post_lab_test(args.id)  



if __name__ == "__main__":
    main()
