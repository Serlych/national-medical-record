#!/usr/bin/env python3
from typing import Optional
from pydantic import BaseModel, Field


class Checkup(BaseModel):
    id: str = Field(...)
    nss: str = Field(...)
    fecha: str = Field(...)
    medico_tratante: str = Field(...)
    cedula_profesional: str = Field(...)
    diagnostico: str = Field(...)
    recetas: list = Field(...)
    pruebas_de_laboratorio: list = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "id": "507f1f77bcf86cd799439011",
                "nss": "68c9eb13-a596-43ec-a5d4-984fe0a42f9e",
                "fecha": "27/05/2022 00:00",
                "medico_tratante": "Dr. Carmen Robledo",
                "cedula_profesional": "57918810",
                "diagnostico": "Gastritis",
                "recetas": ["507f1f77bcf86cd799439011"],
                "pruebas_de_laboratorio": ["507f1f77bcf86cd799439011"]
            }
        }


class CheckupUpdate(BaseModel):
    nss: Optional[str]
    fecha: Optional[str]
    medico_tratante: Optional[str]
    cedula_profesional: Optional[str]
    diagnostico: Optional[str]
    recetas: Optional[list]
    pruebas_de_laboratorio: Optional[list]

    class Config:
        schema_extra = {
            "example": {
                "nss": "68c9eb13-a596-43ec-a5d4-984fe0a42f9e",
                "fecha": "27/05/2022 00:00",
                "medico_tratante": "Dr. Carmen Robledo",
                "cedula_profesional": "57918810",
                "diagnostico": "Gastritis",
                "recetas": ["507f1f77bcf86cd799439011"],
                "pruebas_de_laboratorio": ["507f1f77bcf86cd799439011"]
            }
        }
