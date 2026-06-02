import re
from playwright.sync_api import Page, expect

from seguro.credenciais import *

# I love playwright
def test_login(page: Page):
    # Abre o navegador
    page.goto('https://erp-qa.mitis.com.br/#/')

    # Informa o domínio
    page.get_by_role("textbox", name="Domínio").click()
    page.get_by_role("textbox", name="Domínio").fill(DOMINIO)

    # Informa o nome
    page.get_by_role("textbox", name="Domínio").press("Tab")
    page.get_by_role("textbox", name="Login").fill(LOGIN)

    # Informa a SENHA (esconder a senha)
    page.get_by_role("textbox", name="Login").press("Tab")
    page.get_by_role("textbox", name="Senha").fill(SENHA)

    # Aperta para entrar
    page.get_by_role("button", name="Entrar").click()

    # Valida se entrou
    page.wait_for_url('https://erp-qa.mitis.com.br/#/in')
    expect(page).to_have_url('https://erp-qa.mitis.com.br/#/in')

def test_criacao_produto(page: Page):
    # Entra na criação de produto
    page.get_by_role("banner").get_by_role("button").click()
    page.get_by_role("button").nth(3).click()

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