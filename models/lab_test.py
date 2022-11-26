#!/usr/bin/env python3
from typing import Optional
from pydantic import BaseModel, Field


class LabTest(BaseModel):
    _id: str = Field(...)
    nss: str = Field(...)
    consulta: str = Field(...)
    pruebas: list = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "507f1f77bcf86cd799439011",
                "nss": "68c9eb13-a596-43ec-a5d4-984fe0a42f9e",
                "consulta": "507f1f77bcf86cd799439011",
                "pruebas": [{
                    "nombre": "Colesterol",
                    "fecha": "27/03/2022 00:00",
                    "url": "www.laboratorio.com/resultados"
                }]
            }
        }


class LabTestUpdate(BaseModel):
    nss: Optional[str]
    consulta: Optional[str]
    pruebas: Optional[list]

    class Config:
        schema_extra = {
            "example": {
                "nss": "68c9eb13-a596-43ec-a5d4-984fe0a42f9e",
                "consulta": "507f1f77bcf86cd799439011",
                "pruebas": [{
                    "nombre": "Colesterol",
                    "fecha": "27/03/2022 00:00",
                    "url": "www.laboratorio.com/resultados"
                }]
            }
        }
