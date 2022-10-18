from fastapi import APIRouter

from models.Animal import Animal

router = APIRouter()

banco_de_dados = []

@router.post("/")
def add_item(item: Animal):
    banco_de_dados.append(item)
    return item

@router.get("/")
def list_item():
    return banco_de_dados