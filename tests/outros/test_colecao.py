from playwright.sync_api import Page

from auxiliares.genericos import criacao_generica, edicao_generica, exclusao_generica


ROTINA: str = "CADASTRO DE COLEÇÃO"
"""A rotina de coleção"""


'''
Em outros lugares, a página é recebida da fixture, já na rotina desejada.
Para manter a consistência, seria melhor fazer isso aqui também, ao invés de passar a rotina
para o genérico.
'''


def test_criacao_colecao(page: Page):
    """Cria uma nova coleção"""

    def incremento(page: Page):
        # Informa o desconto
        page.get_by_role("spinbutton").click()
        page.get_by_role("spinbutton").fill("10")
        
        # Seleciona a condição
        page.locator("select").select_option("Sempre")

    criacao_generica(page, ROTINA, incremento)


def test_edicao_colecao(page: Page):
    """Edita uma coleção"""

    def incremento(page: Page):
        # Informa o desconto
        page.get_by_role("spinbutton").click()
        page.get_by_role("spinbutton").fill("1000")

        # Seleciona a condição
        page.locator("select").select_option("1")

    edicao_generica(page, ROTINA, incremento)


def test_exclusao_colecao(page: Page):
    """Exclui uma coleção"""
    exclusao_generica(page, ROTINA)