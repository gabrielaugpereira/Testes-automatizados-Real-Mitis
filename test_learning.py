import re
from playwright.sync_api import Page, Browser, expect
import pytest

from seguro.credenciais import *

# I love playwright

@pytest.fixture(scope='function', autouse=True)
def test_login(page: Page):
    # Abre a página
    page.goto('https://erp-qa.mitis.com.br/#/')

    # Informa o domínio
    page.get_by_role("textbox", name="Domínio").fill(DOMINIO)

    # Informa o nome
    page.get_by_role("textbox", name="Login").fill(LOGIN)

    # Informa a SENHA (esconder a senha)
    page.get_by_role("textbox", name="Senha").fill(SENHA)

    # Aperta para entrar
    page.get_by_role("button", name="Entrar").click()

    # Valida se entrou
    page.wait_for_url('https://erp-qa.mitis.com.br/#/in')
    

def test_criacao_produto(page: Page):
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


def test_criacao_venda(page: Page):
    # Entra na criação de venda
    page.get_by_role("banner").get_by_role("button").click()
    page.get_by_label("88.VENDAS").first.get_by_role("button").first.click()

    # Informa o cliente
    page.wait_for_timeout(1000)
    page.get_by_role("button").nth(5).click()
    page.get_by_text("109194 $.O.$ - FOMENTO").click()

    # Fecha o popup
    page.get_by_role("button", name="Não").click()

    # Informa o vendedor
    page.locator(".p-element.p-inputwrapper.p-autocomplete-clearable.ng-untouched > .w-100 > .p-element.p-ripple").click()
    page.get_by_text("00106697000180").click()

    # Informa o funil
    page.locator(".p-element.p-inputwrapper.ng-untouched > .p-input-custom > .p-element.p-ripple").click()
    page.get_by_text("- Vendas Inicio").click()

    # Salva a venda
    page.get_by_role("button", name=" Salvar").click()

    # Valida se salvou
    expect(page.get_by_text("Pedido salvo com sucesso!")).to_be_visible()





# import re
# from playwright.sync_api import Playwright, sync_playwright, expect


# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()

#     test_login(page)

#     context = browser.new_context(storage_state="user.json")
#     storage = context.storage_state(path="user.json")

#     # ---------------------
#     context.close()
#     browser.close()


# with sync_playwright() as playwright:
#     run(playwright)