from playwright.sync_api import Page, Error, TimeoutError, expect
import re

from auxiliares.default import pesquisar_rotina

'''Terminar CRUD'''

def test_criacao_venda(new_vend_page: Page):
    """Criação de venda"""

    page = new_vend_page
    
    # Entra na criação de venda
    pesquisar_rotina(page, "88.VENDAS", criacao=True)

    # Informa o cliente
    page.wait_for_timeout(1000)
    page.get_by_role("button").nth(5).click()
    page.get_by_text(re.compile(r"[0-9]{3}.[0-9]{3}.[0-9]{2}")).first.click()

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

    # Fecha a página
    page.close()

'''Responsividade com valor padrão do início da página'''
def test_exclusao_venda(vend_page: Page):
    """Exclusão de venda"""

    page = vend_page
    
    # Entra na criação de venda
    pesquisar_rotina(page, "88.VENDAS")
    
    # Encontra uma venda que pode ser excluída
    for i in range(3, 10):
        page.get_by_role("cell", name="Nº Nota Fiscal").nth(i).dblclick()

        try:
            # Encontrou uma, e clicou para excluir
            page.get_by_role("button", name=" Excluir").click(timeout=8000)
            break
        except TimeoutError:
            # Não encontrou, e vai procurar a próxima
            pesquisar_rotina(page, "88.VENDAS")

    else:
        raise Error("Não foi possível encontrar uma venda possível de ser excluída")

    # Confirma a exclusão da venda
    page.get_by_role("button", name="Sim").click()

    # Informa o motivo da exclusão
    page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(4).click()
    page.get_by_text("- TESTE DE PEDIDO").click()
    page.get_by_role("dialog").get_by_role("button", name=" Salvar").click()

    # Valida se venda foi excluída
    expect(page.get_by_text("Novo orçamento")).to_be_visible(timeout=15000)

    # Fecha a página
    page.close()