from playwright.sync_api import Browser, expect

from test_helpers import goto_home_page

# Tenta criar uma venda
def test_criacao_venda(browser: Browser):
    page = goto_home_page(browser)

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

    # Fecha o navegador
    page.close()