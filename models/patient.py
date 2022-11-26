#!/usr/bin/env python3
from typing import Optional

from pydantic import BaseModel, Field


class Patient(BaseModel):
    _id: str = Field(...)
    nss: str = Field(...)
    nombre: str = Field(...)
    apellidos: str = Field(...)
    edad: int = Field(...)
    fecha_de_nacimiento: str = Field(...)
    ciudad_de_nacimiento: str = Field(...)
    tipo_de_sangre: str = Field(...)
    imc: float = Field(...)
    alergias: list = Field(...)
    ultima_consulta: str = Field(...)
    padecimientos: list = Field(...)
    consultas: list = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "ObjectId('638154aad891dfc909b0b17b')",
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
                "consultas": ["objectId"]
            }
        }


class PatientUpdate(BaseModel):
    nss: Optional[str]
    nombre: Optional[str]
    apellidos: Optional[str]
    edad: Optional[int]
    fecha_de_nacimiento: Optional[str]
    ciudad_de_nacimiento: Optional[str]
    tipo_de_sangre: Optional[str]
    imc: Optional[float]
    alergias: Optional[list]
    ultima_consulta: Optional[str]
    padecimientos: Optional[list]
    consultas: Optional[list]

    class Config:
        schema_extra = {
            "example": {
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
                "consultas": ["objectId"]
            }
        }
