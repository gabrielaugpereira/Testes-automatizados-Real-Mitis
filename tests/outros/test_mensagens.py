from playwright.sync_api import Browser, Page
import random

from auxiliares.genericos import criacao_generica, edicao_generica, exclusao_generica


ROTINA = "20.MENSAGENS"
"""A rotina para mensagens"""


def test_criacao_mensagem(page: Page):
    """Cria uma nova mensagem"""

    def incremento(page: Page):
        # Seleciona um tipo de mensagem
        page.locator("select").select_option(str(random.randint(1, 9)))

    criacao_generica(page, ROTINA, incremento)


def test_edicao_mensagem(page: Page):
    """Edita uma mensagem"""

    def incremento(page: Page):
        # Seleciona um tipo de mensagem
        page.locator("select").select_option(str(random.randint(1, 9)))

    edicao_generica(page, ROTINA, incremento)


def test_exclusao_mensagem(page: Page):
    """Exclui uma mensagem"""
    exclusao_generica(page, ROTINA)