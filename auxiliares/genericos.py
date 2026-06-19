from playwright.sync_api import Browser
from auxiliares.default import *


"""
Criação genérica de registro. 
Recebe uma função como parâmetro, para incrementar a criação com mais entradas de valores
"""
def criacao_generica(browser: Browser, rotina: str, incremento: function = None):
    # Abre o navegador
    page = new_page(browser)

    # Entra na rotina informada, na parte de criação
    pesquisar_rotina(page, rotina, criacao=True)

    # Insere o nome
    page.locator("form").get_by_role("textbox").click()
    page.locator("form").get_by_role("textbox").fill("Teste automatizado - GAP")

    # Chama a função passada como parâmetro, para informar campos não previstos
    if incremento: incremento(page)

    # Seleciona como ativo
    page.get_by_role("checkbox", name="Ativo").check()

    # Salva e valida se salvou
    page.get_by_role("button", name="  Salvar").click()
    expect(page.get_by_text("Registro salvo com sucesso")).to_be_visible()

    # Fecha a página
    page.close()


"""
Edição genérica de registro
Recebe uma função como parâmetro, para incrementar a criação com mais entradas de valores
"""
def edicao_generica(browser: Browser, rotina: str, incremento: function = None):
    # Abre o navegador
    page = new_page(browser)

    # Entra na rotina, na listagem de registros
    pesquisar_rotina(page, rotina)

    # Escolhe o último registro criado pela automatização
    page.get_by_role("cell", name="Teste automatizado").last.dblclick()

    # Muda o nome do registro
    page.locator("form").get_by_role("textbox").click()
    page.locator("form").get_by_role("textbox").fill("Teste automatizado não fui eu - GAP")

    # Chama a função passada como parâmetro, para informar campos não previstos
    if incremento: incremento(page)

    # Salva o registro e valida se foi salvo
    page.get_by_role("button", name="  Salvar").click()
    expect(page.get_by_text("Registro salvo com sucesso")).to_be_visible()

    # Fecha a página
    page.close()


"""Exclusão genérica"""
def exclusao_generica(browser: Browser, rotina: str):
    # Abre o navegador
    page = new_page(browser)

    # Entra na rotina, na listagem de registros
    pesquisar_rotina(page, rotina)

    # Escolhe o último registro criado pela automatização
    page.get_by_role("cell", name="Teste automatizado").last.dblclick()

    # Exclui e confirma
    page.get_by_role("button", name="  Excluir").click()
    page.get_by_role("button", name="Sim").click()

    # Valida se houve a exclusão
    expect(page.get_by_text("Registro excluído com sucesso")).to_be_visible()

    # Fecha a página
    page.close()