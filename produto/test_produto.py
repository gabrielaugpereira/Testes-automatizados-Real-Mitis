from playwright.sync_api import Browser, expect
import re

from helpers import goto_home_page

# Tenta criar um produto
def test_criacao_produto(browser: Browser):
    page = goto_home_page(browser)

    # Entra na criação de produto
    page.get_by_role("banner").get_by_role("button").click()
    page.get_by_label("2.PRODUTO").first.get_by_role("button").first.click()

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

    # Fecha o navegador
    page.close()