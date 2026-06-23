from playwright.sync_api import Page

from auxiliares.genericos import criacao_generica, edicao_generica, exclusao_generica


ROTINA = "315.MARGEM"
"""A rotina para margem"""


def test_criacao_margem(page: Page):
    """Cria uma nova margem"""
    criacao_generica(page, ROTINA)
    

def test_edicao_margem(page: Page):
    """Edita uma margem"""
    edicao_generica(page, ROTINA)


def test_exclusao_margem(page: Page):
    """Exclui uma margem"""
    exclusao_generica(page, ROTINA)