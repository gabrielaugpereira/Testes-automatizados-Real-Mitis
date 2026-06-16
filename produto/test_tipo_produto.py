from playwright.sync_api import Browser, expect

from test_main import *


"""Cria um novo tipo de produto"""
def test_criacao_tipo_produto(browser: Browser):
    # Abre o navegador
    page = new_page(browser)

    # Entra na criação de tipos de produto
    pesquisar_rotina(page, "371.TIPO DE PRODUTO", criacao=True)
    
    # Insere o nome do tipo
    page.locator("form").get_by_role("textbox").click()
    page.locator("form").get_by_role("textbox").fill("Teste automatizado - GAP")
    
    # Seleciona o tipo como ativo
    page.get_by_role("checkbox", name="Ativo").check()

    # Salva o tipo de produto
    page.get_by_role("button", name="  Salvar").click()

    # Valida se salvou
    expect(page.get_by_text("Registro salvo com sucesso")).to_be_visible()