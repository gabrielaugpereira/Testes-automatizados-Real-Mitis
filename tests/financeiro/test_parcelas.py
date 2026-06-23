"""Fluxo CRUD para parcelas de financeiro"""

from playwright.sync_api import Browser, Page, TimeoutError, expect
import re
import pytest

from auxiliares.default import pesquisar_rotina, page as new_page


@pytest.fixture(scope="module")
def page(new_page: Page):
    """
    Página customizada para o módulo de parcelas.
    
    """

    # Entra na listagem de financeiros
    pesquisar_rotina(new_page, "568.FINANCEIRO")

    # Escolhe o primeiro financeiro
    new_page.locator(".btn.btn-light").first.click()

    # Retorna a page
    yield new_page

    # Fecha a página
    new_page.close()    


'''Separar os auxiliares para auxiliares/?'''
def add_centro_custo(page: Page):
    """Auxiliar para adicionar centro de custo"""

    # Seleciona um plano de contas
    page.locator("app-mts-plano-contas-dropdown > .btn-group > .p-element.p-inputwrapper > .w-100 > .p-element.p-ripple").click()
    page.get_by_text("1/12 AVOS REPRESENTANTES").click()

    # Seleciona um centro de custo
    page.locator("app-mts-centro-custo-dropdown > .btn-group > .p-element.p-inputwrapper > .w-100 > .p-element.p-ripple").click()
    page.get_by_text("CENTRAL").click()

    # Adiciona ao plano de contas
    page.get_by_role("button", name=" Adicionar").click()

    # Valida se centro de curto foi adicionado
    expect(page.get_by_text("Adicionado!")).to_be_visible()


def add_nova_parcela(page: Page):
    """Auxiliar para adicionar uma nova parcela ao financeiro"""

    # Seleciona uma forma de pagamento
    page.locator("#dropdownFormaPagamento > app-mts-forma-pagamento-dropdown > div > p-autocomplete > div > button").click()
    page.get_by_text("A VISTA - DINHEIRO - 1").click()

    # Informa o valor de vencimento
    page.get_by_role("row", name="Data vencimento").get_by_placeholder("0,00").click()
    page.get_by_role("row", name="Data vencimento").get_by_role("textbox").fill("1")
    page.get_by_role("row", name="Data vencimento").get_by_role("textbox").press("Tab")

    # Adiciona centro de custo
    add_centro_custo(page)

    # Valida se financeiro foi criado
    expect(page.get_by_text("Sucesso"))


'''Usar uma forma de verificar se a page já foi criada, senão se for rodar só edição ou exclusão, não funciona'''
def test_criacao_parcela(page):
    """Cria uma parcela para o primeiro financeiro encontrado"""

    # Seleciona para adicionar, e segue o fluxo de adicionar parcela
    page.get_by_role("button", name=" Adicionar Nova Parcela").click()
    add_nova_parcela(page)

    # Valida se salvou
    expect(page.get_by_text("Adicionado!")).to_be_visible()


def test_edicao_parcela():
    """Edita a primeira parcela do financeiro selecionado"""

    # Volta para a aba de itens
    page.get_by_role("button", name="Itens").click()

    # Escolhe a primeira parcela
    page.get_by_title("Editar", exact=True).first.click()

    # Edita a observação da parcela
    page.locator("textarea[name=\"obs\"]").click()
    page.locator("textarea[name=\"obs\"]").fill("Parcela editada")

    # Valida se valor de vencimento é maior que 0
    try:
        expect(page.locator("#inputValorOriginal > .w-100")).to_have_value(re.compile(r"[1-9][0-9,]*"))
    except TimeoutError:
        # Se não for, insere valor 1 e adiciona centro de custo
        page.locator("#inputValorOriginal > .w-100").click()
        page.locator("#inputValorOriginal > .w-100").fill("1")

        add_centro_custo()

    # Salva e valida se salvou
    page.get_by_role("button", name=" Salvar").click()
    expect(page.get_by_text("Salvo com sucesso!")).to_be_visible()


def test_exclusao_parcela():
    """Exclui a primeira parcela do financeiro válido"""

    # Volta para a aba de itens
    page.get_by_role("button", name="Itens").click()

    # Seleciona para excluir a primeira, e confirma
    page.get_by_title("Excluir").first.click()
    page.get_by_role("button", name="Sim").click()

    # Valida se excluiu
    expect(page.get_by_text("Registro excluído com sucesso!")).to_be_visible()

    # Fecha a página
    page.close()