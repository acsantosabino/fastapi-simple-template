import logging
from typing import List

from app.model.Models import Item

class AppService():

    def __init__(self):
        logging.info("Inicializando o AppService")

    def hello(self):
        return "Hello world"


    def contar_itens(self, lista_itens : List[Item]):
        return f"{len(lista_itens)} salvos"
