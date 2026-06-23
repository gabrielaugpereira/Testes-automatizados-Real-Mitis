from playwright.sync_api import Browser, Page
import random

from auxiliares.genericos import criacao_generica, edicao_generica, exclusao_generica


class _ModuleVariables:
    """A rotina para mensagens"""
    rotina: str = "20.MENSAGENS"


def test_criacao_mensagem(browser: Browser):
    """Cria uma nova mensagem"""

    def incremento(page: Page):
        # Seleciona um tipo de mensagem
        page.locator("select").select_option(str(random.randint(1, 9)))

    criacao_generica(browser, _ModuleVariables.rotina, incremento)


def test_edicao_mensagem(browser: Browser):
    """Edita uma mensagem"""

    def incremento(page: Page):
        # Seleciona um tipo de mensagem
        page.locator("select").select_option(str(random.randint(1, 9)))

    edicao_generica(browser, _ModuleVariables.rotina, incremento)


def test_exclusao_mensagem(browser: Browser):
    """Exclui uma mensagem"""
    exclusao_generica(browser, _ModuleVariables.rotina)