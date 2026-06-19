from playwright.sync_api import Browser, expect

from auxiliares.default import *
from auxiliares.genericos import *


class _ModuleVariables:
    # A rotina para tipo de produto
    rotina: str = "371.TIPO DE PRODUTO"


"""Cria um novo tipo de produto"""
def test_criacao_tipo_produto(browser: Browser):
    criacao_generica(browser, _ModuleVariables.rotina)


"""Edita um tipo de produto"""
def test_edicao_tipo_produto(browser: Browser):
    edicao_generica(browser, _ModuleVariables.rotina)


"""Exclui um tipo de produto"""
def test_exclusao_tipo_produto(browser: Browser):
    exclusao_generica(browser, _ModuleVariables.rotina)