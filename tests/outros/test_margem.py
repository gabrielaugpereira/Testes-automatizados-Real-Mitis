from playwright.sync_api import Browser, expect

from auxiliares.default import *
from auxiliares.genericos import *


class _ModuleVariables:
    # A rotina para margem
    rotina: str = "315.MARGEM"


"""Cria uma nova margem"""
def test_criacao_margem(browser: Browser):
    criacao_generica(browser, _ModuleVariables.rotina)
    

"""Edita uma margem"""
def test_edicao_margem(browser: Browser):
    edicao_generica(browser, _ModuleVariables.rotina)


"""Exclui uma margem"""
def test_exclusao_margem(browser: Browser):
    exclusao_generica(browser, _ModuleVariables.rotina)