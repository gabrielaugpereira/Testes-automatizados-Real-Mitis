from playwright.sync_api import Browser, expect
import random

from helpers import goto_home_page

# Tenta criar um financeiro a pagar
def test_criacao_financeiro_pagar(browser: Browser):
    page = goto_home_page(browser)

    # Entra na criação de financeiro
    page.get_by_role("banner").get_by_role("button").click()
    page.get_by_label("568.FINANCEIRO").first.get_by_role("button").first.click()

    # Escreve uma descrição
    page.wait_for_timeout(800)
    page.get_by_text("Adicionar descrição").click()
    page.get_by_role("textbox", name="Descrição do lançamento").fill("Teste automatizado - GAP")
    page.get_by_role("heading", name="Lançamento Teste automatizado").get_by_role("button").click()

    # Escolhe um fornecedor
    page.get_by_role("button").nth(5).click()
    page.get_by_text("791 25.991.826 WASHINGTON").click()

    # Informa um número de documento
    page.get_by_role("textbox", name="Número do Documento").click()
    page.get_by_role("textbox", name="Número do Documento").fill(str(random.randint(100000000000, 999999999999)))

    page.get_by_role("textbox", name="Complemento").click()
    page.get_by_role("textbox", name="Complemento").fill(str(random.randint(10000, 99999)))

    # Seleciona uma forma de pagamento
    page.locator("#dropdownFormaPagamento > app-mts-forma-pagamento-dropdown > div > p-autocomplete > div > button").click()
    page.get_by_text("A VISTA - DINHEIRO - 1").click()

    # Informa o falor de vencimento
    page.get_by_role("row", name="Data vencimento 03/06/2026").get_by_placeholder("0,00").click()
    page.get_by_role("row", name="Data vencimento 03/06/2026").get_by_role("textbox").fill("1")
    page.get_by_role("row", name="Data vencimento 03/06/2026").get_by_role("textbox").press("Tab")

    # Seleciona um plano de contas
    page.locator("app-mts-plano-contas-dropdown > .btn-group > .p-element.p-inputwrapper > .w-100 > .p-element.p-ripple").click()
    page.get_by_text("1/12 AVOS REPRESENTANTES").click()

    # Seleciona um centro de custo
    page.locator("app-mts-centro-custo-dropdown > .btn-group > .p-element.p-inputwrapper > .w-100 > .p-element.p-ripple").click()
    page.get_by_text("CENTRAL").click()

    # Adiciona ao plano de contas
    page.get_by_role("button", name=" Adicionar").click()

    # Salva o financeiro
    page.get_by_role("button", name=" Salvar").click()

    # Valida se foi criado
    expect(page.get_by_text("Salvo com sucesso!")).to_be_visible()

    # Fecha o navegador
    page.close()

def test_criacao_financeiro_receber(browser: Browser):
    page = goto_home_page(browser)

    # Entra na criação de um financeiro
    page.get_by_role("banner").get_by_role("button").click()
    page.get_by_label("568.FINANCEIRO").first.get_by_role("button").first.click()
    page.wait_for_timeout(800)

    # Informa que é um financeiro a receber
    page.get_by_role("radio", name="Receber").check()

    # Escreve uma descrição
    page.get_by_text("Adicionar descrição").click()
    page.get_by_role("textbox", name="Descrição do lançamento").fill("Teste automatizado - GAP")
    page.get_by_role("heading", name="Lançamento Teste automatizado").get_by_role("button").click()

    # Escolhe um cliente
    page.get_by_role("button").nth(5).click()
    page.get_by_text("109194 $.O.$ - FOMENTO").click()

    # Informa um número de documento
    page.get_by_role("textbox", name="Número do Documento").click()
    page.get_by_role("textbox", name="Número do Documento").fill(str(random.randint(100000000000, 999999999999)))

    page.get_by_role("textbox", name="Complemento").click()
    page.get_by_role("textbox", name="Complemento").fill(str(random.randint(10000, 99999)))
    
    # Seleciona uma forma de pagamento
    page.locator("app-mts-forma-pagamento-dropdown > .btn-group > .p-element.p-inputwrapper > .w-100 > .p-element.p-ripple").click()
    page.get_by_text("A VISTA - DINHEIRO - 1").click()

    # Informa o valor
    page.locator("#inputValorOriginal > .w-100").click()
    page.locator("#inputValorOriginal > .w-100").fill("1")

    # Salva o financeiro
    page.get_by_role("button", name=" Salvar").click()
    
    # Valida se foi criado
    expect(page.get_by_text("Salvo com sucesso!")).to_be_visible()

    # Fecha o navegador
    page.close()