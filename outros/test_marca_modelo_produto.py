from playwright.sync_api import Browser

from test_main import *


"""Cria uma nova marca para produto"""
def test_criacao_marca_produto(browser: Browser):
    # Abre o navegador
    page = new_page(browser)

    # Entra na criação de marca e modelo de produto
    pesquisar_rotina(page, "44.MARCA / MODELO DO PRODUTO", criacao=True)

    # Preenche o nome/descrição
    page.locator("form").get_by_role("textbox").click()
    page.locator("form").get_by_role("textbox").fill("Teste automatizado - GAP")

    # Seleciona como sendo do tipo marca
    page.locator("select").select_option("Marca")

    # Marca como ativo
    page.pause()
    page.get_by_role("checkbox", name="Ativo").check()

    # Salva o registro
    page.get_by_role("button", name="  Salvar").click()

    # Valida se foi salvo
    expect(page.get_by_text("Registro salvo com sucesso")).to_be_visible()

    # Fecha a página
    page.close()


"""Cria um novo modelo para produto"""
def test_criacao_modelo_produto(browser: Browser):
    # Abre o navegador
    page = new_page(browser)

    # Entra na criação de marca e modelo de produto
    pesquisar_rotina(page, "44.MARCA / MODELO DO PRODUTO", criacao=True)

    # Preenche o nome/descrição
    page.locator("form").get_by_role("textbox").click()
    page.locator("form").get_by_role("textbox").fill("Teste automatizado - GAP")

    # Seleciona como sendo do tipo modelo
    page.locator("select").select_option("Modelo")

    # Marca como ativo
    page.pause()
    page.get_by_role("checkbox", name="Ativo").check()

    # Salva o registro
    page.get_by_role("button", name="  Salvar").click()

    # Valida se foi salvo
    expect(page.get_by_text("Registro salvo com sucesso")).to_be_visible()

    # Fecha a página
    page.close()


"""Edita um registro de marca ou de modelo para produto"""
def test_edicao_marca_modelo_produto(browser: Browser):
    # Abre o navegador
    page = new_page(browser)

    # Entra na criação de marca e modelo de produto
    pesquisar_rotina(page, "44.MARCA / MODELO DO PRODUTO")

    # Seleciona o último registro feito por teste automatizado
    page.get_by_role("cell", name="Teste automatizado").last.dblclick()

    # Edita o nome do registro
    page.locator("form").get_by_role("textbox").click()
    page.locator("form").get_by_role("textbox").fill("Teste automatizado não fui eu - GAP")

    # Salva o registro
    page.get_by_role("button", name="  Salvar").click()

    # Valida se foi salvo
    expect(page.get_by_text("Registro salvo com sucesso")).to_be_visible()

    # Fecha a página
    page.close()


"""Exclui um registro de marca ou de modelo para produto"""
def test_exclusao_marca_modelo_produto(browser: Browser):
    # Abre o navegador
    page = new_page(browser)

    # Entra na criação de marca e modelo de produto
    pesquisar_rotina(page, "44.MARCA / MODELO DO PRODUTO")

    # Seleciona o último registro feito por teste automático
    page.get_by_role("cell", name="Teste automatizado").last.dblclick()

    # Clica para excluir e confirma
    page.get_by_role("button", name="  Excluir").click()
    page.get_by_role("button", name="Sim").click()

    # Valida se foi excluído
    expect(page.get_by_text("Registro excluído com sucesso")).to_be_visible()

    # Fecha a página
    page.close()