from playwright.sync_api import Browser, expect

from test_main import *


"""Cria ua nova coleção"""
def test_criacao_colecao(browser: Browser):
    # Abre o navegador
    page = new_page(browser)

    # Entra na criação de tipos de produto
    pesquisar_rotina(page, "464.CADASTRO DE COLEÇÃO", criacao=True)
    
    # Insere o nome do tipo
    page.locator("form").get_by_role("textbox").click()
    page.locator("form").get_by_role("textbox").fill("Teste automatizado - GAP")

    # Informa o desconto
    page.get_by_role("spinbutton").click()
    page.get_by_role("spinbutton").fill("10")
    
    # Seleciona a condição
    page.locator("select").select_option("Sempre")

    # Seleciona o tipo como ativo
    page.get_by_role("checkbox", name="Ativo").check()

    # Salva o tipo de produto
    page.get_by_role("button", name="  Salvar").click()

    # Valida se salvou
    expect(page.get_by_text("Registro salvo com sucesso")).to_be_visible()

    # Fecha a página
    page.close()


"""Edita uma coleção"""
def test_edicao_colecao(browser: Browser):
    # Abre o navegador
    page = new_page(browser)

    # Entra na criação de tipos de produto
    pesquisar_rotina(page, "464.CADASTRO DE COLEÇÃO")

    # Escolhe o último registro criado pela automatização
    page.get_by_role("cell", name="Teste automatizado").last.dblclick()

    # Muda o nome do tipo de produto
    page.locator("form").get_by_role("textbox").click()
    page.locator("form").get_by_role("textbox").fill("Teste automatizado não fui eu - GAP")

    # Informa o desconto
    page.get_by_role("spinbutton").click()
    page.get_by_role("spinbutton").fill("1000")

    # Seleciona a condição
    page.locator("select").select_option("1")
    
    # Salva o tipo de produto
    page.get_by_role("button", name="  Salvar").click()

    # Valida se foi salvo
    expect(page.get_by_text("Registro salvo com sucesso")).to_be_visible()

    # Fecha a página
    page.close()


"""Exclui uma coleção"""
def test_exclusao_colecao(browser: Browser):
    # Abre o navegador
    page = new_page(browser)

    # Entra na criação de tipos de produto
    pesquisar_rotina(page, "464.CADASTRO DE COLEÇÃO")

    # Escolhe o último registro criado pela automatização
    page.get_by_role("cell", name="Teste automatizado").last.dblclick()

    # Exclui e confirma
    page.get_by_role("button", name="  Excluir").click()
    page.get_by_role("button", name="Sim").click()

    # Valida se houve a exclusão
    expect(page.get_by_text("Registro excluído com sucesso")).to_be_visible()

    # Fecha a página
    page.close()