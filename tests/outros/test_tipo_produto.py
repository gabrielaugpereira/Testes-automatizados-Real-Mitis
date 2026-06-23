from playwright.sync_api import Browser

from auxiliares.genericos import criacao_generica, edicao_generica, exclusao_generica


class _ModuleVariables:
    """A rotina para tipo de produto"""
    rotina: str = "371.TIPO DE PRODUTO"


def test_criacao_tipo_produto(browser: Browser):
    """Cria um novo tipo de produto"""
    criacao_generica(browser, _ModuleVariables.rotina)


def test_edicao_tipo_produto(browser: Browser):
    """Edita um tipo de produto"""
    edicao_generica(browser, _ModuleVariables.rotina)


def test_exclusao_tipo_produto(browser: Browser):
    """Exclui um tipo de produto"""
    exclusao_generica(browser, _ModuleVariables.rotina)