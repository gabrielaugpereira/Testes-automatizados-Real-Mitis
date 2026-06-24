"""Fluxo CRUD para produto"""

from playwright.sync_api import Page, expect
import re
import pytest

from auxiliares.default import pesquisar_rotina, DESCRICAO_PADRAO


'''Remover decorator'''
# ================================================
# Operações de criação
# ================================================

@pytest.mark.skip("Falha no sistema: a geração de código do real está falhando")
def criacao_produto(page: Page, tipo: int):
    """
    Reutilização das criações de produto.
    O parâmetro tipo pode ter valor 1 ou 2.
    """

    # Insere um id customizado
    # Id máximo no momento de escrita do código: 34244829
    '''page.locator("#codProd").click()
    page.locator("#codProd").fill(str(random.randint(10**8, 35*(10**7))))'''

    # ----- Aba de detalhamento -----
    # Descrição do produto
    page.locator("#dscProd").click()
    page.locator("#dscProd").fill(DESCRICAO_PADRAO)

    # Sub-grupo do produto
    page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(4).click()
    page.get_by_role("option", name="ANGELIN").first.click()

    # Grupo do produto
    page.locator(".p-element.p-inputwrapper.p-autocomplete-clearable.ng-untouched > .w-100 > .p-element.p-ripple").first.click()
    page.get_by_text("Grupo 1").click()

    # Fornecedor do produto
    page.locator(".p-element.p-inputwrapper.p-autocomplete-clearable.ng-untouched > .w-100 > .p-element.p-ripple").click()
    page.get_by_text("37.545.280 WILSON SILVERIO DOS SANTOS JUNIOR").click()

    # Tipo
    page.locator("select[name=\"tipo\"]").select_option(str(tipo))

    # Referência
    page.get_by_role("cell", name="KIT").get_by_role("textbox").click()
    page.get_by_role("cell", name="KIT").get_by_role("textbox").fill("Referência")

    # Kit
    '''page.locator("#chkKit").check()
    Não está sendo possível usar kit, porque senão se torna necessário informar dados na aba de localicação'''

    # ----- Aba fiscal -----
    page.get_by_role("tab", name="Fiscal").click()

    # NCM
    page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(3).click()
    page.get_by_text("0199900").click()

    # Cálculo fiscal
    page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(5).click()
    page.get_by_text("CHECK 1 DUPLICAÇÃO DE CÁLC").click()

    # Tipo fiscal
    page.locator("app-mts-tipo-fiscal-produto-dropdown > .btn-group > .p-element.p-inputwrapper > .w-100 > .p-element.p-ripple").click()
    page.get_by_role("option", name="NORMAL").click()

    '''Foto'''

    # ----- Aba de precificação -----
    page.get_by_role("tab", name="Precificação").click()

    # Preço bruto
    page.get_by_role("row", name="Preço bruto:").get_by_role("textbox").click()
    page.get_by_role("spinbutton").fill("01")

    # ----- Salvar produto -----
    page.get_by_role("button", name=" Salvar").click()
    page.get_by_role("button", name="Sim").click()
    
    # Validação
    expect(page.get_by_text("Produto salvo com sucesso!")).to_be_visible(timeout=9000)

    # Fecha a página
    page.close()


def test_criacao_produto_1(new_prod_page: Page):
    """Primeira criação de produto"""
    criacao_produto(new_prod_page, 1)

def test_criacao_produto_2(new_prod_page: Page):
    """Segunda criação de produto, informando campos que a primeira não informa"""
    criacao_produto(new_prod_page, 2)


# ================================================
# Operações de edição
# ================================================

def test_atualizacao_produto(prod_page: Page):
    """Atualização de produto"""
    pytest.skip("Teste ainda não foi implementado")


# ================================================
# Operações de exclusão
# ================================================

def test_exclusao_produto(prod_page: Page):
    """Exclusão de produto"""

    page = prod_page

    # Ordena pelo código interno, para pegar o último
    page.get_by_role("columnheader", name="Cód. Interno").click()
    page.get_by_role("columnheader", name="Cód. Interno").click()

    # Seleciona o primeiro
    page.locator(".btn.btn-light").first.click()

    # Clica para excluir e confirma
    page.get_by_role("button", name=" Excluir").click()
    page.get_by_role("button", name="Sim").click()

    # Validação
    expect(page.get_by_text("Produto excluído com sucesso.")).to_be_visible()

    # Fecha a página
    page.close()