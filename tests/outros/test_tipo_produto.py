from playwright.sync_api import Page

from auxiliares.genericos import criacao_generica, edicao_generica, exclusao_generica


ROTINA = "TIPO DE PRODUTO"
"""A rotina para tipo de produto"""


def test_criacao_tipo_produto(page: Page):
    """Cria um novo tipo de produto"""
    criacao_generica(page, ROTINA)


def test_edicao_tipo_produto(page: Page):
    """Edita um tipo de produto"""
    edicao_generica(page, ROTINA)


def test_exclusao_tipo_produto(page: Page):
    """Exclui um tipo de produto"""
    exclusao_generica(page, ROTINA)