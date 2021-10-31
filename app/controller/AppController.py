from typing import List
from app.model.Models import Item
from app.service.AppService import AppService
from fastapi import APIRouter
 
my_service = AppService()
router = APIRouter(prefix="")
 

@router.get("/")
def hello():
    return my_service.hello()

@router.post("/item")
def post(itens: List[Item]):
    return my_service.contar_itens(itens)
