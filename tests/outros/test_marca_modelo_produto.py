from playwright.sync_api import Browser, Page

from auxiliares.genericos import criacao_generica, edicao_generica, exclusao_generica


class _ModuleVariables:
    """A rotina para marca / modelo de produto"""
    rotina: str = "44.MARCA / MODELO DO PRODUTO"


def test_criacao_marca_produto(browser: Browser):
    """Cria uma nova marca para produto"""
    
    def incremento(page: Page):
        # Seleciona como sendo do tipo marca
        page.locator("select").select_option("Marca")

    criacao_generica(browser, _ModuleVariables.rotina, incremento)


def test_criacao_modelo_produto(browser: Browser):
    """Cria um novo modelo para produto"""
    
    def incremento(page: Page):
        # Seleciona como sendo do tipo modelo
        page.locator("select").select_option("Modelo")

    criacao_generica(browser, _ModuleVariables.rotina, incremento)


def test_edicao_marca_modelo_produto(browser: Browser):
    """Edita um registro de marca ou de modelo para produto"""
    edicao_generica(browser, _ModuleVariables.rotina)


def test_exclusao_marca_modelo_produto(browser: Browser):
    """Exclui um registro de marca ou de modelo para produto"""
    exclusao_generica(browser, _ModuleVariables.rotina)