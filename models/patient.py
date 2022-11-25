#!/usr/bin/env python3
from typing import Optional

from pydantic import BaseModel, Field


class Patient(BaseModel):
    NSS: str = Field(...)
    Nombre: str = Field(...)
    Apellidos: str = Field(...)
    Edad: int = Field(...)
    Fecha_de_Nacimiento: str = Field(...)
    Ciudad_de_Nacimiento: str = Field(...)
    Tipo_de_Sangre: str = Field(...)
    IMC: float = Field(...)
    Alergias: list = Field(...)
    Ultima_Consulta: str = Field(...)
    Padecimientos: list = Field(...)
    Historial_de_Consultas: list = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "NSS": "68c9eb13-a596-43ec-a5d4-984fe0a42f9e",
                "Nombre": "Hector",
                "Apellidos": "Merino",
                "Edad": 35,
                "Fecha_de_Nacimiento": "06/09/1998 00:00",
                "Ciudad_de_Nacimiento": "Guadalajara",
                "Tipo_de_Sangre": "A+",
                "IMC": 41.42,
                "Alergias": ["Gluten"],
                "Ultima_Consulta": "29/09/2013 00:00",
                "Padecimientos": ["Cirrosis"],
                "Historial_de_Consultas": ["objectId"]
            }
        }


class PatientUpdate(BaseModel):
    NSS: Optional[str]
    Nombre: Optional[str]
    Apellidos: Optional[str]
    Edad: Optional[int]
    Fecha_de_Nacimiento: Optional[str]
    Ciudad_de_Nacimiento: Optional[str]
    Tipo_de_Sangre: Optional[str]
    IMC: Optional[float]
    Alergias: Optional[list]
    Ultima_Consulta: Optional[str]
    Padecimientos: Optional[list]
    Historial_de_Consultas: Optional[list]

    class Config:
        schema_extra = {
            "example": {
                "NSS": "68c9eb13-a596-43ec-a5d4-984fe0a42f9e",
                "Nombre": "Hector",
                "Apellidos": "Merino",
                "Edad": 35,
                "Fecha_de_Nacimiento": "06/09/1998 00:00",
                "Ciudad_de_Nacimiento": "Guadalajara",
                "Tipo_de_Sangre": "A+",
                "IMC": 41.42,
                "Alergias": ["Gluten"],
                "Ultima Consulta": "29/09/2013 00:00",
                "Padecimientos": ["Cirrosis"],
                "Historial_de_Consultas": ["objectId"]
            }
        }
