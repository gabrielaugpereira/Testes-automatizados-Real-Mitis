from playwright.sync_api import Browser, expect

from test_main import *
from auxiliares.genericos import *


class _ModuleVariables:
    # A rotina para coleção
    rotina: str = "464.CADASTRO DE COLEÇÃO"


"""Cria uma nova coleção"""
def test_criacao_colecao(browser: Browser):
    def incremento(page: Page):
        # Informa o desconto
        page.get_by_role("spinbutton").click()
        page.get_by_role("spinbutton").fill("10")
        
        # Seleciona a condição
        page.locator("select").select_option("Sempre")

    criacao_generica(browser, _ModuleVariables.rotina, incremento)


"""Edita uma coleção"""
def test_edicao_colecao(browser: Browser):
    def incremento(page: Page):
        # Informa o desconto
        page.get_by_role("spinbutton").click()
        page.get_by_role("spinbutton").fill("1000")

        # Seleciona a condição
        page.locator("select").select_option("1")

    edicao_generica(browser, _ModuleVariables.rotina, incremento)


"""Exclui uma coleção"""
def test_exclusao_colecao(browser: Browser):
    exclusao_generica(browser, _ModuleVariables.rotina)