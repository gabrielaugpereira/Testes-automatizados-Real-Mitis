from playwright.sync_api import Browser

from auxiliares.genericos import criacao_generica, edicao_generica, exclusao_generica


class _ModuleVariables:
    """A rotina para margem"""
    rotina: str = "315.MARGEM"


def test_criacao_margem(browser: Browser):
    """Cria uma nova margem"""
    criacao_generica(browser, _ModuleVariables.rotina)
    

def test_edicao_margem(browser: Browser):
    """Edita uma margem"""
    edicao_generica(browser, _ModuleVariables.rotina)


def test_exclusao_margem(browser: Browser):
    """Exclui uma margem"""
    exclusao_generica(browser, _ModuleVariables.rotina)