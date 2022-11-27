#!/usr/bin/env python3
import argparse
import logging

from routes.patient import coll as patient_endpoint
from routes.checkup import coll as checkup_endpoint
from routes.prescription import coll as prescription_endpoint
from routes.lab_test import coll as lab_test_endpoint

from models.patient import Patient
from models.checkup import Checkup
from models.prescription import Prescription
from models.lab_test import LabTest

from lib.api import api_factory

# Set logger
log = logging.getLogger()
log.setLevel('INFO')
handler = logging.FileHandler('nmr.log')
handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
log.addHandler(handler)


def patient_api(nss: str, action: str):
    return api_factory(action, patient_endpoint, {
        'get': f"{nss}",
        'post': '',
        'patch': f"{nss}"
    }, Patient)


def checkup_api(nss: str, action: str):
    return api_factory(action, checkup_endpoint, {
        'get': f"{nss}",
        'post': '',
    }, Checkup)


def prescription_api(nss: str, action: str):
    return api_factory(action, prescription_endpoint, {
        'get': f"{nss}",
        'post': '',
    }, Prescription)


def lab_test_api(nss: str, action: str):
    return api_factory(action, lab_test_endpoint, {
        'get': f"{nss}",
        'post': '',
    }, LabTest)


paciente = "paciente"
consulta = "consulta"
receta = "receta"
prueba = "prueba"


def main():
    log.info(f"===== Historial Médico Nacional =====")

    parser = argparse.ArgumentParser()

    # Actions
    list_of_actions = ["buscar", "crear", "actualizar"]
    parser.add_argument("action",
                        choices=list_of_actions,
                        help="Acciones a realizar por la aplicación")

    # Entities
    list_of_entities = [paciente, consulta, receta, prueba]
    parser.add_argument("entity",
                        choices=list_of_entities,
                        help="Entidad sobre la cual realizar la acción")

    # Arguments
    parser.add_argument("-n", "--nss",
                        help="Proporcionar un NSS relacionado con la acción",
                        default=None)

    args = parser.parse_args()
    action = ''

    if args.action == "buscar":
        action = 'get'

        if not args.nss:
            print('Para buscar, es necesario introducir un NSS')
            return

    if args.action == "crear":
        action = 'post'

    if args.action == "actualizar":
        action = 'patch'

        if args.entity != paciente:
            print("No es posible actualizar otra entidad diferente a un paciente")
            return

    # Call endpoints
    if args.entity == paciente:
        patient_api(args.nss, action)

    if args.entity == consulta:
        checkup_api(args.nss, action)

    if args.entity == receta:
        prescription_api(args.nss, action)

    if args.entity == prueba:
        lab_test_api(args.nss, action)


if __name__ == "__main__":
    main()
