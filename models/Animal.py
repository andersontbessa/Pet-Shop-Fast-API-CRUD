#CADASTRO NA RECEPÇÃO DE PETSHOP(BANHO, TOSA...)
from numpy import number
from pydantic import BaseModel

class Animal(BaseModel):
    Id: int
    Owner: str
    AnimalName: str
    Gender: str
    Breed: str
    Age: str
    Contact: str
    UpdatedOn: str