from playwright.sync_api import Page

from auxiliares import criacao_generica, edicao_generica, exclusao_generica


ROTINA = "PORTARIA DO PRODUTO"
"""A rotina para portaria"""


def test_criacao_portaria(page: Page):
    """Cria uma nova portaria"""
    criacao_generica(page, ROTINA)
    

def test_edicao_portaria(page: Page):
    """Edita uma portaria"""
    edicao_generica(page, ROTINA)


def test_exclusao_portaria(page: Page):
    """Exclui uma portaria"""
    exclusao_generica(page, ROTINA)