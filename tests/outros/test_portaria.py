from playwright.sync_api import Browser

from auxiliares.genericos import criacao_generica, edicao_generica, exclusao_generica


class _ModuleVariables:
    """A rotina para portaria"""
    rotina: str = "324.PORTARIA DO PRODUTO"


def test_criacao_portaria(browser: Browser):
    """Cria uma nova portaria"""
    criacao_generica(browser, _ModuleVariables.rotina)
    

def test_edicao_portaria(browser: Browser):
    """Edita uma portaria"""
    edicao_generica(browser, _ModuleVariables.rotina)


def test_exclusao_portaria(browser: Browser):
    """Exclui uma portaria"""
    exclusao_generica(browser, _ModuleVariables.rotina)