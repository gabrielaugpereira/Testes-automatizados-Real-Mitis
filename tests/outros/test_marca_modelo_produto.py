from playwright.sync_api import Page

from auxiliares import criacao_generica, edicao_generica, exclusao_generica


ROTINA = "MARCA / MODELO DO PRODUTO"
"""A rotina para marca / modelo de produto"""


def test_criacao_marca_produto(page: Page):
    """Cria uma nova marca para produto"""
    
    def incremento(page: Page):
        # Seleciona como sendo do tipo marca
        page.locator("select").select_option("Marca")

    criacao_generica(page, ROTINA, incremento)


def test_criacao_modelo_produto(page: Page):
    """Cria um novo modelo para produto"""
    
    def incremento(page: Page):
        # Seleciona como sendo do tipo modelo
        page.locator("select").select_option("Modelo")

    criacao_generica(page, ROTINA, incremento)


def test_edicao_marca_modelo_produto(page: Page):
    """Edita um registro de marca ou de modelo para produto"""
    edicao_generica(page, ROTINA)


def test_exclusao_marca_modelo_produto(page: Page):
    """Exclui um registro de marca ou de modelo para produto"""
    exclusao_generica(page, ROTINA)