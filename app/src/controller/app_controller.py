"""
app_controller define rotas e ações
"""
from typing import List
from fastapi import APIRouter
from src.model.models import Item
from src.service.app_service import AppService

my_service = AppService()
router = APIRouter(prefix="")


@router.get("/")
def hello():
    """ Hello World """
    return my_service.hello()

@router.post("/item")
def post(itens: List[Item]):
    """ Post recebe lista de itens e retorna contagem """
    return my_service.contar_itens(itens)
