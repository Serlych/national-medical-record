#!/usr/bin/env python3
import uuid
from typing import Optional
from pydantic import BaseModel, Field

class Prescription(BaseModel):
    NSS: str = Field(...)
    Consulta: str = Field(...)
    Medicamento: list = Field(...)

    class Config:
        allow_population_by_field_name = True ##
        schema_extra = {
            "example": {
                "NSS": "68c9eb13-a596-43ec-a5d4-984fe0a42f9e",
                "Consulta": "4ab7a800b1eddedbd9fcc513",
                "Medicamento": [
                    {"Nombre_del_Medicamento": "AMOXICILINA",
                    "Dosis (capsulas)": 0,
                    "Gramaje (mg)": 19,
                    "Frecuencia (c/hrs)": 65,
                    "Duracion (dias)": 39}
                    ]
                }
        }


class PrescriptionUpdate(BaseModel):
    NSS: Optional[str]
    Consulta: Optional[str]
    Medicamento: Optional[list]

    class Config:
        schema_extra = {
            "example": {
                "NSS": "68c9eb13-a596-43ec-a5d4-984fe0a42f9e",
                "Consulta": "4ab7a800b1eddedbd9fcc513",
                "Medicamento": [
                    {"Nombre_del_Medicamento": "AMOXICILINA",
                    "Dosis (capsulas)": 0,
                    "Gramaje (mg)": 19,
                    "Frecuencia (c/hrs)": 65,
                    "Duracion (dias)": 39}
                    ]
                }
        }