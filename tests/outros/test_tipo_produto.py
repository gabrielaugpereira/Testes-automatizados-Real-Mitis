from playwright.sync_api import Browser

from auxiliares.genericos import criacao_generica, edicao_generica, exclusao_generica


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