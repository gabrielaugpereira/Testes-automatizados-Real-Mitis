from playwright.sync_api import Browser
from auxiliares.genericos import criacao_generica, edicao_generica, exclusao_generica


class _ModuleVariables:
    """A rotina para habilidade"""
    rotina: str = "554.HABILIDADE"


def test_criacao_habilidade(browser: Browser):
    """Cria uma nova habilidade"""
    criacao_generica(browser, _ModuleVariables.rotina)
    

def test_edicao_habilidade(browser: Browser):
    """Edita uma habilidade"""
    edicao_generica(browser, _ModuleVariables.rotina)


def test_exclusao_habilidade(browser: Browser):
    """Exclui uma habilidade"""
    exclusao_generica(browser, _ModuleVariables.rotina)