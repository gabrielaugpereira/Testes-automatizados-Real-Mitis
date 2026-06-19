from playwright.sync_api import Browser
from auxiliares.genericos import *


class _ModuleVariables:
    # A rotina para habilidade
    rotina: str = "554.HABILIDADE"


"""Cria uma nova habilidade"""
def test_criacao_habilidade(browser: Browser):
    criacao_generica(browser, _ModuleVariables.rotina)
    

"""Edita uma habilidade"""
def test_edicao_habilidade(browser: Browser):
    edicao_generica(browser, _ModuleVariables.rotina)


"""Exclui uma habilidade"""
def test_exclusao_habilidade(browser: Browser):
    exclusao_generica(browser, _ModuleVariables.rotina)