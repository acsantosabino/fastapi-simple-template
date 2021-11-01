"""
app_service define classe de acesso a um serviço
"""
import logging
from typing import List
from model.models import Item

class AppService():
    """ Classe de acesso a um serviço """
    def __init__(self):
        logging.info("Inicializando o AppService")

    @classmethod
    def hello(cls):
        """ Hello World """
        return "Hello world"

    @classmethod
    def contar_itens(cls, lista_itens : List[Item]):
        """ Conta itens de uma lista """
        return f"{len(lista_itens)} salvos"
