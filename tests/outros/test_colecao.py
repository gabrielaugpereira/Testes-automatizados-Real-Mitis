from playwright.sync_api import Browser, Page

from auxiliares.genericos import criacao_generica, edicao_generica, exclusao_generica


class _ModuleVariables:
    """A rotina para coleção"""
    rotina: str = "464.CADASTRO DE COLEÇÃO"


def test_criacao_colecao(browser: Browser):
    """Cria uma nova coleção"""

    def incremento(page: Page):
        # Informa o desconto
        page.get_by_role("spinbutton").click()
        page.get_by_role("spinbutton").fill("10")
        
        # Seleciona a condição
        page.locator("select").select_option("Sempre")

    criacao_generica(browser, _ModuleVariables.rotina, incremento)


def test_edicao_colecao(browser: Browser):
    """Edita uma coleção"""

    def incremento(page: Page):
        # Informa o desconto
        page.get_by_role("spinbutton").click()
        page.get_by_role("spinbutton").fill("1000")

        # Seleciona a condição
        page.locator("select").select_option("1")

    edicao_generica(browser, _ModuleVariables.rotina, incremento)


def test_exclusao_colecao(browser: Browser):
    """Exclui uma coleção"""
    exclusao_generica(browser, _ModuleVariables.rotina)