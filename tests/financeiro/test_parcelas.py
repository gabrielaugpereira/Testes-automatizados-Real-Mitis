"""Fluxo CRUD para parcelas de financeiro"""

from playwright.sync_api import Page, TimeoutError, expect
import re
import pytest

from auxiliares.default import pesquisar_rotina


@pytest.fixture(scope="module")
def mpage(page: Page):
    """
    Uma mesma página usada por todos os testes do módulo, encerrada apenas no final.

    Entra na rotina de financeiros, escolhe o primeiro mantém-se lá, 
    para que os testes não precisem todos executar o mesmo processo.

    Por baixo dos panos, o resultado dessa função é injetado em todos os testes do módulo.

    Mpage vem de "module page".
    """

    # Entra na listagem de financeiros
    pesquisar_rotina(page, "568.FINANCEIRO")

    # Escolhe o primeiro financeiro
    page.locator(".btn.btn-light").first.click()

    # Retorna a page
    yield page


'''Separar os auxiliares para auxiliares/?'''
def add_centro_custo(mpage: Page):
    """Auxiliar para adicionar centro de custo"""

    # Seleciona um plano de contas
    mpage.locator("app-mts-plano-contas-dropdown > .btn-group > .p-element.p-inputwrapper > .w-100 > .p-element.p-ripple").click()
    mpage.get_by_text("1/12 AVOS REPRESENTANTES").click()

    # Seleciona um centro de custo
    mpage.locator("app-mts-centro-custo-dropdown > .btn-group > .p-element.p-inputwrapper > .w-100 > .p-element.p-ripple").click()
    mpage.get_by_text("CENTRAL").click()

    # Adiciona ao plano de contas
    mpage.get_by_role("button", name=" Adicionar").click()

    # Valida se centro de curto foi adicionado
    expect(mpage.get_by_text("Adicionado!")).to_be_visible()


def add_nova_parcela(mpage: Page):
    """Auxiliar para adicionar uma nova parcela ao financeiro"""

    # Seleciona uma forma de pagamento
    mpage.locator("#dropdownFormaPagamento > app-mts-forma-pagamento-dropdown > div > p-autocomplete > div > button").click()
    mpage.get_by_text("A VISTA - DINHEIRO - 1").click()

    # Informa o valor de vencimento
    mpage.get_by_role("row", name="Data vencimento").get_by_placeholder("0,00").click()
    mpage.get_by_role("row", name="Data vencimento").get_by_role("textbox").fill("1")
    mpage.get_by_role("row", name="Data vencimento").get_by_role("textbox").press("Tab")

    # Adiciona centro de custo
    add_centro_custo(mpage)

    # Valida se financeiro foi criado
    expect(mpage.get_by_text("Sucesso"))


def test_criacao_parcela(mpage: Page):
    """Cria uma parcela para o primeiro financeiro encontrado"""

    # Seleciona para adicionar, e segue o fluxo de adicionar parcela
    mpage.get_by_role("button", name=" Adicionar Nova Parcela").click()
    add_nova_parcela(mpage)

    # Valida se salvou
    expect(mpage.get_by_text("Adicionado!")).to_be_visible()


def test_edicao_parcela(mpage: Page):
    """Edita a primeira parcela do financeiro selecionado"""

    # Volta para a aba de itens
    mpage.get_by_role("button", name="Itens").click()

    # Escolhe a primeira parcela
    mpage.get_by_title("Editar", exact=True).first.click()

    # Edita a observação da parcela
    mpage.locator("textarea[name=\"obs\"]").click()
    mpage.locator("textarea[name=\"obs\"]").fill("Parcela editada")

    # Valida se valor de vencimento é maior que 0
    try:
        expect(mpage.locator("#inputValorOriginal > .w-100")).to_have_value(re.compile(r"[1-9][0-9,]*"))
    except TimeoutError:
        # Se não for, insere valor 1 e adiciona centro de custo
        mpage.locator("#inputValorOriginal > .w-100").click()
        mpage.locator("#inputValorOriginal > .w-100").fill("1")

        add_centro_custo()

    # Salva e valida se salvou
    mpage.get_by_role("button", name=" Salvar").click()
    expect(mpage.get_by_text("Salvo com sucesso!")).to_be_visible()


def test_exclusao_parcela(mpage: Page):
    """Exclui a primeira parcela do financeiro válido"""

    # Volta para a aba de itens
    mpage.get_by_role("button", name="Itens").click()

    # Seleciona para excluir a primeira, e confirma
    mpage.get_by_title("Excluir").first.click()
    mpage.get_by_role("button", name="Sim").click()

    # Valida se excluiu
    expect(mpage.get_by_text("Registro excluído com sucesso!")).to_be_visible()

    # Fecha a página
    mpage.close()