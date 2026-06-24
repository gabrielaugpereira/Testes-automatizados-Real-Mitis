"""
Funções para fazer um fluxo CRUD genérico, e reduzir repetição de código através do sistema
"""

from collections.abc import Callable

from playwright.sync_api import Page, expect
from auxiliares.default import pesquisar_rotina, DESCRICAO_PADRAO, DESCRICAO_EDIT_PADRAO


def criacao_generica(page: Page, rotina: str, incremento: Callable[[Page], None] = None) -> None:
    """
    Criação genérica de registro. 
    Recebe uma função como parâmetro, para incrementar a criação com mais entradas de valores
    """

    # Entra na rotina informada, na parte de criação
    pesquisar_rotina(page, rotina, criacao=True)

    # Insere o nome
    page.locator("form").get_by_role("textbox").click()
    page.locator("form").get_by_role("textbox").fill(DESCRICAO_PADRAO)

    # Chama a função passada como parâmetro, para informar campos não previstos
    if incremento: 
        incremento(page)

    # Seleciona como ativo
    page.get_by_role("checkbox", name="Ativo").check()

    # Salva e valida se salvou
    page.get_by_role("button", name="  Salvar").click()
    expect(page.get_by_text("Registro salvo com sucesso")).to_be_visible()


def edicao_generica(page: Page, rotina: str, incremento: Callable[[Page], None] = None) -> None:
    """
    Edição genérica de registro
    Recebe uma função como parâmetro, para incrementar a criação com mais entradas de valores
    """

    # Entra na rotina, na listagem de registros
    pesquisar_rotina(page, rotina)

    # Escolhe o último registro criado pela automatização
    page.get_by_role("cell", name="Teste automatizado").last.dblclick()

    # Muda o nome do registro
    page.locator("form").get_by_role("textbox").click()
    page.locator("form").get_by_role("textbox").fill(DESCRICAO_EDIT_PADRAO)

    # Chama a função passada como parâmetro, para informar campos não previstos
    if incremento: 
        incremento(page)

    # Salva o registro e valida se foi salvo
    page.get_by_role("button", name="  Salvar").click()
    expect(page.get_by_text("Registro salvo com sucesso")).to_be_visible()


def exclusao_generica(page: Page, rotina: str) -> None:
    """Exclusão genérica"""

    # Entra na rotina, na listagem de registros
    pesquisar_rotina(page, rotina)

    # Escolhe o último registro criado pela automatização
    page.get_by_role("cell", name="Teste automatizado").last.dblclick()

    # Exclui e confirma
    page.get_by_role("button", name="  Excluir").click()
    page.get_by_role("button", name="Sim").click()

    # Valida se houve a exclusão
    expect(page.get_by_text("Registro excluído com sucesso")).to_be_visible()