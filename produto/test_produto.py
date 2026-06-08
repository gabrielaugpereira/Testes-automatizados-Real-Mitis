from playwright.sync_api import Browser, expect
import re

from test_main import *

"""Fluxo CRUD para produto"""

# ======================================================
# Criação de produto
# ======================================================
def test_criacao_produto(browser: Browser):
    # Abre o navegador
    page = goto_home_page(browser)

    # Entra na criação de produto
    pesquisar_rotina(page, "2.PRODUTO", criacao=True)

    # ----- Aba de detalhamento -----
    # Descrição do produto
    page.locator("#dscProd").click()
    page.locator("#dscProd").fill("Teste automatizado - GAP")

    # Sub-grupo do produto
    page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(4).click()
    page.get_by_role("option", name="ANGELIN").click()

    # Grupo do produto
    page.locator(".p-element.p-inputwrapper.p-autocomplete-clearable.ng-untouched > .w-100 > .p-element.p-ripple").first.click()
    page.get_by_text("Grupo 1").click()

    # Fornecedor do produto
    page.locator(".p-element.p-inputwrapper.p-autocomplete-clearable.ng-untouched > .w-100 > .p-element.p-ripple").click()
    page.get_by_text("852 26.867.066 FABIO BASTOS").click()

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

    # ----- Aba de precificação -----
    page.get_by_role("tab", name="Precificação").click()

    # Preço bruto
    page.get_by_role("row", name="Preço bruto:").get_by_role("textbox").click()
    page.get_by_role("spinbutton").fill("01")

    # ----- Salvar produto -----
    page.get_by_role("button", name=" Salvar").click()
    page.get_by_role("button", name="Sim").click()
    
    # Validação
    expect(page.get_by_text("Produto salvo com sucesso!")).to_be_visible()

# ======================================================
# Atualização de produto
# ======================================================
def test_atualizacao_produto(browser: Browser):
    raise NotImplementedError("Teste ainda não foi implementado")

# ======================================================
# Atualização de produto
# ======================================================
def test_atualizacao_produto(browser: Browser):
    raise NotImplementedError("Teste ainda não foi implementado")

# ======================================================
# Exclusão de produto
# ======================================================
def test_exclusao_produto(browser: Browser):
    raise NotImplementedError("Teste ainda não foi implementado")

# ======================================================
# Exclusão de produto
# ======================================================
def test_exclusao_produto(browser: Browser):
    page = goto_home_page(browser)

    # Entra na listagem de produtos
    pesquisar_rotina(page, "2.PRODUTO")

    # Seleciona o primeiro
    page.locator(".btn.btn-light").first.click()

    # Clica para excluir e confirma
    page.get_by_role("button", name=" Excluir").click()
    page.get_by_role("button", name="Sim").click()

    # Validação
    expect(page.get_by_text("Produto excluído com sucesso.")).to_be_visible()