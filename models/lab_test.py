#!/usr/bin/env python3
from typing import Optional

from pydantic import BaseModel, Field


class LabTest(BaseModel):
    NSS: str = Field(...)
    Consulta: str = Field(...)
    Pruebas: list = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "NSS": "68c9eb13-a596-43ec-a5d4-984fe0a42f9e",
                "Consulta": "objectId",
                "Pruebas": [{
                    "Nombre de la Prueba": "Colesterol",
                    "Fecha": "27/03/2022 00:00",
                    "URL de Resultados": "www.laboratorio.com/resultados"
                }]
            }
        }


class LabTestUpdate(BaseModel):
    NSS: Optional[str]
    Consulta: Optional[str]
    Pruebas: Optional[list]

    class Config:
        schema_extra = {
            "example": {
                "NSS": "68c9eb13-a596-43ec-a5d4-984fe0a42f9e",
                "Consulta": "objectId",
                "Pruebas": [{
                    "Nombre de la Prueba": "Colesterol",
                    "Fecha": "27/03/2022 00:00",
                    "URL de Resultados": "www.laboratorio.com/resultados"
                }]
            }
        }
