from playwright.sync_api import Browser, Page, TimeoutError, expect
import pytest
import random

from test_main import *


class _ModuleVariables:
    # Mantém a page disponível para todos os testes
    page: Page = None

"""Entra na rotina de financeiro e disponibiliza a page"""
@pytest.fixture(scope='module', autouse=True)
def entra_rotina_financeiro(browser: Browser):
    page = new_page(browser)
    _ModuleVariables.page = page
    
    pesquisar_rotina(page, "FINANCEIRO")

    yield

    # Garante que a página seja fechada
    _ModuleVariables.page.close()

"""
Entra na rotina, seleciona dois financeiros de situações diferentes e entra no menu mais
"""
def seleciona_financeiros(page: Page):
    # Seleciona um financeiro de cada tipo
    page.get_by_text("VENCIDO", exact=True).first.click(modifiers=["ControlOrMeta"], timeout=8000)
    page.get_by_text("ABERTO", exact=True).first.click(modifiers=["ControlOrMeta"], timeout=8000)

    # Entra no menu mais e escolhe a alteração em lote
    page.get_by_title("Mais opções").click()
    page.locator("a").filter(has_text="Alterar em lote").click()


"""Altera o valor dos financeiros para outros pré definido"""
def test_alterar_lote_novo_valor():
    page = _ModuleVariables.page
    seleciona_financeiros(page)

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
    

"""Incrementa o valor dos financeiros em valor pré definido"""
def test_alterar_lote_increm_valor():
    page = _ModuleVariables.page
    seleciona_financeiros(page)

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


"""Decrementa o valor dos financeiros em valor pré definido""" 
def test_alterar_lote_decrem_valor(): 
    page = _ModuleVariables.page
    seleciona_financeiros(page)

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


"""Altera a data de vencimento dos financeiros"""
def test_alterar_lote_nova_data():
    page = _ModuleVariables.page
    seleciona_financeiros(page)

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
"""Incrementa dias na data de vencimento dos financeiros"""
def test_alterar_lote_increm_dias():
    page = _ModuleVariables.page
    seleciona_financeiros(page)

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


"""Decrementa dias na data de vencimento dos financeiros"""
def test_alterar_lote_decrem_dias():
    page = _ModuleVariables.page
    seleciona_financeiros(page)

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
"""Seleciona duas contas, uma aberta e outra vencida, e usando o filtro, altera somente a aberta"""
def test_alterar_lote_filtro_aberto():
    page = _ModuleVariables.page
    seleciona_financeiros(page)

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


"""Seleciona duas contas, uma aberta e outra vencida, e usando o filtro, altera somente a vencida"""
def test_alterar_lote_filtro_vencido():
    page = _ModuleVariables.page
    seleciona_financeiros(page)

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