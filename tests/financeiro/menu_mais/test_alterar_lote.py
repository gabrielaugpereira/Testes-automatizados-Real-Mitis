from playwright.sync_api import Page, expect
import pytest
import random


@pytest.fixture
def alt_page(fin_page: Page):
    """
    Página personalizada para alteração em lote.

    Entra na rotina de financeiro, seleciona dois financeiros de situações diferentes, 
    entra no menu mais e seleciona "Alterar em lote"
    """

    page = fin_page

    # Seleciona um financeiro de cada tipo
    page.get_by_text("VENCIDO", exact=True).first.click(modifiers=["ControlOrMeta"], timeout=8000)
    page.get_by_text("ABERTO", exact=True).first.click(modifiers=["ControlOrMeta"], timeout=8000)

    # Entra no menu mais e escolhe a alteração em lote
    page.get_by_title("Mais opções").click()
    page.locator("a").filter(has_text="Alterar em lote").click()


def test_alterar_lote_novo_valor(alt_page: Page):
    """Altera o valor dos financeiros para outros pré definido"""

    page = alt_page

    # Seleciona a alteração do valor
    page.get_by_role("checkbox", name="Alterar valor vencimento").check()

    # Insere novo valor
    page.get_by_role("textbox", name="0,00").click()
    page.get_by_role("cell", name="0").get_by_role("textbox").fill("153")

    # Confirma a alteração
    page.get_by_role("button", name=" Confirmar").click()
    page.get_by_role("button", name="Sim").click()

    # Valida se houve a alteração
    expect(page.get_by_text("Sucesso!")).to_be_visible()
    

def test_alterar_lote_increm_valor(alt_page: Page):
    """Incrementa o valor dos financeiros em valor pré definido"""

    page = alt_page

    # Seleciona o incremento do valor
    page.get_by_role("checkbox", name="Alterar valor vencimento").check()
    page.get_by_role("cell", name="Novo valor").get_by_role("combobox").select_option("1: 2")

    # Insere o valor de acréscimo
    page.get_by_role("textbox", name="0,00").click()
    page.get_by_role("cell", name="0").get_by_role("textbox").fill("20")

    # Confirma a alteração
    page.get_by_role("button", name=" Confirmar").click()
    page.get_by_role("button", name="Sim").click()

    # Valida se houve a alteração
    expect(page.get_by_text("Sucesso!")).to_be_visible()


def test_alterar_lote_decrem_valor(alt_page: Page): 
    """Decrementa o valor dos financeiros em valor pré definido""" 
    
    page = alt_page

    # Seleciona o decremento do valor
    page.get_by_role("checkbox", name="Alterar valor vencimento").check()
    page.get_by_role("cell", name="Novo valor").get_by_role("combobox").select_option("2: 3")

    # Insere o valor de decréscimo
    page.get_by_role("textbox", name="0,00").click()
    page.get_by_role("cell", name="0").get_by_role("textbox").fill("2000")

    # Confirma a alteração
    page.get_by_role("button", name=" Confirmar").click()

    # Valida se foi-se percebido um valor muito alto de redução
    expect(page.locator("#swal2-html-container")).to_contain_text("As parcelas com valor menor que o valor de redução serão zeradas")

    # Finaliza a confirmação da alteração
    page.get_by_role("button", name="Sim").click()

    # Valida se houve a alteração
    expect(page.get_by_text("Sucesso!")).to_be_visible()


def test_alterar_lote_nova_data(alt_page: Page):
    """Altera a data de vencimento dos financeiros"""

    page = alt_page

    # Seleciona a alteração da data
    page.get_by_role("checkbox", name="Alterar data vencimento").check()

    # Insere uma nova data. 
    # A condição serve apenas para evitar de consumir todos os financeiros de uma situação
    if random.choice([True, False]):
        page.locator("input[name=\"data\"]").fill("2100-01-01")
    else:
        page.locator("input[name=\"data\"]").fill("2000-01-01")

    # Confirma a alteração
    page.get_by_role("button", name=" Confirmar").click()
    page.get_by_role("button", name="Sim").click()

    # Valida se houve a alteração
    expect(page.get_by_text("Sucesso!")).to_be_visible()


'''Erro na mensagem de confirmação, por conta do input de data vazio'''
def test_alterar_lote_increm_dias(alt_page: Page):
    """Incrementa dias na data de vencimento dos financeiros"""

    page = alt_page

    # Seleciona o incremento de dias
    page.get_by_role("checkbox", name="Alterar data vencimento").check()
    page.get_by_role("cell", name="Nova data").get_by_role("combobox").select_option("1: 2")

    # Insere uma quantidade de dias
    page.get_by_role("row", name="Alterar data vencimento").get_by_role("spinbutton").click()
    page.get_by_role("row", name="Alterar data vencimento").get_by_role("spinbutton").fill("50")

    # Confirma a alteração
    page.get_by_role("button", name=" Confirmar").click()
    page.get_by_role("button", name="Sim").click()

    # Valida se houve a alteração
    expect(page.get_by_text("Sucesso!")).to_be_visible()


def test_alterar_lote_decrem_dias(alt_page: Page):
    """Decrementa dias na data de vencimento dos financeiros"""

    page = alt_page

    # Seleciona o decremento de dias
    page.get_by_role("checkbox", name="Alterar data vencimento").check()
    page.get_by_role("cell", name="Nova data").get_by_role("combobox").select_option("2: 3")

    # Insere uma quantidade de dias
    page.get_by_role("row", name="Alterar data vencimento").get_by_role("spinbutton").click()
    page.get_by_role("row", name="Alterar data vencimento").get_by_role("spinbutton").fill("50")

    # Confirma a alteração
    page.get_by_role("button", name=" Confirmar").click()
    page.get_by_role("button", name="Sim").click()

    # Valida se houve a alteração
    expect(page.get_by_text("Sucesso!")).to_be_visible()


'''Cada vez que você fecha a confirmação e abre de novo, a quantidade de financeiros disponíveis
para alteração é incrementada pela quantidade real de financeiros disponível'''
def test_alterar_lote_filtro_aberto(alt_page: Page):
    """Seleciona duas contas, uma aberta e outra vencida, e usando o filtro, altera somente a aberta"""

    page = alt_page

    # Seleciona o incremento do valor
    page.get_by_role("checkbox", name="Alterar valor vencimento").check()
    page.get_by_role("cell", name="Novo valor").get_by_role("combobox").select_option("1: 2")

    # Desmarca as parcelas vencidas
    page.get_by_role("checkbox", name="Parcelas vencidas").uncheck()

    # Confirma a alteração
    page.get_by_role("button", name=" Confirmar").click()

    # Valida se o filtro funcionou
    expect(page.locator("#swal2-html-container")).to_contain_text("1 conta(s) válida(s) para alteração. Deseja prosseguir?")

    # Finaliza a confirmação
    page.get_by_role("button", name="Sim").click()

    # Valida se houve a alteração
    expect(page.get_by_text("Sucesso!")).to_be_visible()


def test_alterar_lote_filtro_vencido(alt_page: Page):
    """Seleciona duas contas, uma aberta e outra vencida, e usando o filtro, altera somente a vencida"""

    page = alt_page

    # Seleciona o incremento do valor
    page.get_by_role("checkbox", name="Alterar valor vencimento").check()
    page.get_by_role("cell", name="Novo valor").get_by_role("combobox").select_option("1: 2")

    # Desmarca as parcelas abertas
    page.get_by_role("checkbox", name="Parcelas em aberto").uncheck()

    # Confirma a alteração
    page.get_by_role("button", name=" Confirmar").click()

    # Valida se o filtro funcionou
    expect(page.locator("#swal2-html-container")).to_contain_text("1 conta(s) válida(s) para alteração. Deseja prosseguir?")

    # Finaliza a confirmação
    page.get_by_role("button", name="Sim").click()

    # Valida se houve a alteração
    expect(page.get_by_text("Sucesso!")).to_be_visible()


'''Implementar teste do filtro de número de parcela'''