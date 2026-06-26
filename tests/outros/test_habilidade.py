from playwright.sync_api import Page
from auxiliares import criacao_generica, edicao_generica, exclusao_generica


ROTINA = "HABILIDADE"
"""A rotina para habilidade"""


def test_criacao_habilidade(page: Page):
    """Cria uma nova habilidade"""
    criacao_generica(page, ROTINA)
    

def test_edicao_habilidade(page: Page):
    """Edita uma habilidade"""
    edicao_generica(page, ROTINA)


def test_exclusao_habilidade(page: Page):
    """Exclui uma habilidade"""
    exclusao_generica(page, ROTINA)