#!/usr/bin/env python3
from typing import Optional
from pydantic import BaseModel, Field


class Checkup(BaseModel):
    NSS: str = Field(...)
    Fecha: str = Field(...)
    Medico_Tratante: str = Field(...)
    Cedula_Profesional: str = Field(...)
    Diagnostico: str = Field(...)
    Receta: list = Field(...)
    Pruebas_de_Laboratorio: list = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "NSS": "68c9eb13-a596-43ec-a5d4-984fe0a42f9e",
                "Fecha": "27/05/2022 00:00",
                "Medico Tratante": "Dr. Carmen Robledo",
                "Cedula Profesional": "57918810",
                "Diagnostico": "Gastritis",
                "Receta": ["objectId"],
                "Pruebas de Laboratorio": ["objectId"]
            }
        }


class CheckupUpdate(BaseModel):
    NSS: Optional[str]
    Consulta: Optional[str]
    Pruebas: Optional[list]

    class Config:
        schema_extra = {
            "example": {
                "NSS": "68c9eb13-a596-43ec-a5d4-984fe0a42f9e",
                "Fecha": "27/05/2022 00:00",
                "Medico Tratante": "Dr. Carmen Robledo",
                "Cedula Profesional": "57918810",
                "Diagnostico": "Gastritis",
                "Receta": ["objectId"],
                "Pruebas de Laboratorio": ["objectId"]
            }
        }
