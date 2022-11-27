#!/usr/bin/env python3
from typing import Optional
from pydantic import BaseModel, Field, validator


class Prescription(BaseModel):
    id: str = Field(...)
    nss: str = Field(...)
    consulta: str = Field(...)
    medicamentos: list = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "id": "507f1f77bcf86cd799439011",
                "nss": "68c9eb13-a596-43ec-a5d4-984fe0a42f9e",
                "consulta": "507f1f77bcf86cd799439011",
                "medicamentos": [{
                    "nombre": "AMOXICILINA",
                    "dosis": 0,
                    "gramaje": 19,
                    "frecuencia": 65,
                    "duracion": 39
                }]
            }
        }


class PrescriptionUpdate(BaseModel):
    nss: Optional[str]
    consulta: Optional[str]
    medicamentos: Optional[list]

    @validator('consulta', pre=True, always=True)
    def set_consulta(cls, _):
        return ''

    class Config:
        validate_assignment = True
        schema_extra = {
            "example": {
                "nss": "68c9eb13-a596-43ec-a5d4-984fe0a42f9e",
                "consulta": "507f1f77bcf86cd799439011",
                "medicamentos": [{
                    "nombre": "AMOXICILINA",
                    "dosis": 0,
                    "gramaje": 19,
                    "frecuencia": 65,
                    "duracion": 39
                }]
            }
        }
