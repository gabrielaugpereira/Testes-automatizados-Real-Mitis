from playwright.sync_api import Browser

from test_main import *
from auxiliares.genericos import *


class _ModuleVariables:
    # A rotina para marca / modelo de produto
    rotina: str = "44.MARCA / MODELO DO PRODUTO"


"""Cria uma nova marca para produto"""
def test_criacao_marca_produto(browser: Browser):
    def incremento(page: Page):
        # Seleciona como sendo do tipo marca
        page.locator("select").select_option("Marca")

    criacao_generica(browser, _ModuleVariables.rotina, incremento)


"""Cria um novo modelo para produto"""
def test_criacao_modelo_produto(browser: Browser):
    def incremento(page: Page):
        # Seleciona como sendo do tipo modelo
        page.locator("select").select_option("Modelo")

    criacao_generica(browser, _ModuleVariables.rotina, incremento)


"""Edita um registro de marca ou de modelo para produto"""
def test_edicao_marca_modelo_produto(browser: Browser):
    edicao_generica(browser, _ModuleVariables.rotina)


"""Exclui um registro de marca ou de modelo para produto"""
def test_exclusao_marca_modelo_produto(browser: Browser):
    exclusao_generica(browser, _ModuleVariables.rotina)