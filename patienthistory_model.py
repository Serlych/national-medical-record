#!/usr/bin/env python3
import uuid
from typing import Optional
from pydantic import BaseModel, Field

class Patient(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    NSS: str = Field(...)
    Nombre: str = Field(...)
    Apellidos: str = Field (...)
    Edad: int = Field(...)
    Fecha_de_Nacimiento: str = Field(...)
    Ciudad_de_Nacimiento: str = Field(...)
    Tipo_de_Sangre: str = Field(...)
    IMC: float = Field(...)
    Alergias: str = Field(...)
    Ultima_Consulta: str = Field(...)
    Padecimientos: str = Field(...)
    Historial_de_Consultas: list = Field(...)

    class Config:
        allow_population_by_field_name = True ##
        schema_extra = {
            "example": {
                "_id": "68c9eb13-a596-43ec-a5d4-984fe0a42fee",
                "NSS": "68c9eb13-a596-43ec-a5d4-984fe0a42f9e",
                "Nombre": "Hector",
                "Apellidos": "Merino",
                "Edad": 35,
                "Fecha_de_Nacimiento": "06/09/1998 00:00",
                "Ciudad_de_Nacimiento": "Guadalajara",
                "Tipo_de_Sangre": "A+",
                "IMC": 41.42,
                "Alergias": "Gluten",
                "Ultima Consulta": "29/09/2013 00:00",
                "Padecimientos": "Cirrosis",
                "Historial_de_Consultas": ["23737d5e-8d99-43c8-80d2-8228027408f4"] 
 
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
    Alergias: Optional[str]
    Ultima_Consulta: Optional[str]
    Padecimientos:  Optional[str]
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
                "Alergias": "Gluten",
                "Ultima Consulta": "29/09/2013 00:00",
                "Padecimientos": "Cirrosis",
                "Historial_de_Consultas": ["23737d5e-8d99-43c8-80d2-8228027408f4"] 
            }
        }