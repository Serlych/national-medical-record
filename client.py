#!/usr/bin/env python3
import argparse
import json

from routes.patient import coll as patient_endpoint
from routes.checkup import coll as checkup_endpoint
from routes.prescription import coll as prescription_endpoint
from routes.lab_test import coll as lab_test_endpoint

from models.patient import Patient
from models.checkup import Checkup
from models.prescription import Prescription
from models.lab_test import LabTest

from lib.api import api_factory


def patient_api(nss: str, action: str):
    return api_factory(action, patient_endpoint, {
        "buscar": f"{nss}",
        "crear": "",
        "actualizar": f"{nss}"
    }, Patient)


def checkup_api(nss: str, action: str, data_override=None):
    return api_factory(action, checkup_endpoint, {
        "buscar": f"{nss}",
        "crear": "",
        "asociar_prueba": "associate_lab_test",
        "asociar_receta": "associate_prescription"
    }, Checkup, data_override)


def prescription_api(nss: str, action: str, data_override=None):
    return api_factory(action, prescription_endpoint, {
        "buscar": f"{nss}",
        "crear": "",
        "asociar": "associate_checkup"
    }, Prescription, data_override)


def lab_test_api(nss: str, action: str, data_override=None):
    return api_factory(action, lab_test_endpoint, {
        "buscar": f"{nss}",
        "crear": "",
        "asociar": "associate_checkup"
    }, LabTest, data_override)


paciente = "paciente"
consulta = "consulta"
receta = "receta"
prueba = "prueba"


def main():
    print(f"===== Historial Médico Nacional =====")

    parser = argparse.ArgumentParser()

    # Actions
    list_of_actions = ["buscar", "crear", "actualizar", "visita"]
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

    # ==================================================

    if args.action == "visita":
        if args.entity != paciente:
            print("Las visitas son sólo para pacientes")
            return

        # patient = patient_api(args.nss, "crear")
        checkup = checkup_api(args.nss, "crear")
        prescription = prescription_api(args.nss, "crear")
        lab_test = lab_test_api(args.nss, "crear")

        checkup = json.loads(checkup)
        prescription = json.loads(prescription)
        lab_test = json.loads(lab_test)

        prescription_api(args.nss, "asociar", data_override={
            "prescription_id": prescription["id"],
            "checkup_id": checkup["id"]
        })

        lab_test_api(args.nss, "asociar", data_override={
            "lab_test_id": lab_test["id"],
            "checkup_id": checkup["id"]
        })

        checkup_api(args.nss, "asociar_receta", data_override={
            "prescription_id": prescription["id"],
            "checkup_id": checkup["id"]
        })

        checkup_api(args.nss, "asociar_prueba", data_override={
            "lab_test_id": lab_test["id"],
            "checkup_id": checkup["id"]
        })

        return

    elif args.action == "buscar":
        if not args.nss:
            print("Para buscar, es necesario introducir un NSS")
            return

    elif args.action == "actualizar":
        if args.entity != paciente:
            print("No es posible actualizar otra entidad diferente a un paciente")
            return

    # Call endpoints
    if args.entity == paciente:
        patient_api(args.nss, args.action)

    if args.entity == consulta:
        checkup_api(args.nss, args.action)

    if args.entity == receta:
        prescription_api(args.nss, args.action)

    if args.entity == prueba:
        lab_test_api(args.nss, args.action)


if __name__ == "__main__":
    main()
