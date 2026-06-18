from playwright.sync_api import Browser, expect

from test_main import *
from auxiliares.genericos import *


class _ModuleVariables:
    # A rotina para portaria
    rotina: str = "324.PORTARIA DO PRODUTO"


"""Cria uma nova portaria"""
def test_criacao_portaria(browser: Browser):
    criacao_generica(browser, _ModuleVariables.rotina)
    

"""Edita uma portaria"""
def test_edicao_portaria(browser: Browser):
    edicao_generica(browser, _ModuleVariables.rotina)


"""Exclui uma portaria"""
def test_exclusao_portaria(browser: Browser):
    exclusao_generica(browser, _ModuleVariables.rotina)