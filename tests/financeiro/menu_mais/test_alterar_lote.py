from playwright.sync_api import Page, expect
import pytest
import random
from collections.abc import Iterator

from auxiliares.default import pesquisar_rotina


'''mpage é um erro'''
@pytest.fixture(scope="module")
def mpage(page: Page) -> Iterator[Page]:
    """
    Uma mesma página usada por todos os testes do módulo, encerrada apenas no final.

    Apenas entra na rotina de financeiros.

    Por baixo dos panos, o resultado dessa função é injetado em todos os testes do módulo.

    Mpage vem de "module page".
    """

    '''Possivelmente criar fin_page'''
    
    pesquisar_rotina(page, "FINANCEIRO")

    yield page


@pytest.fixture(scope="function", autouse=True)
def seleciona_financeiros(mpage: Page):
    """
    Seleciona dois financeiros de situações diferentes e entra no menu mais
    """

    # Seleciona um financeiro de cada tipo
    mpage.get_by_text("VENCIDO", exact=True).first.click(modifiers=["ControlOrMeta"], timeout=8000)
    mpage.get_by_text("ABERTO", exact=True).first.click(modifiers=["ControlOrMeta"], timeout=8000)

    # Entra no menu mais e escolhe a alteração em lote
    mpage.get_by_title("Mais opções").click()
    mpage.locator("a").filter(has_text="Alterar em lote").click()


def test_alterar_lote_novo_valor(mpage: Page):
    """Altera o valor dos financeiros para outros pré definido"""

    # Seleciona a alteração do valor
    mpage.get_by_role("checkbox", name="Alterar valor vencimento").check()

    # Insere novo valor
    mpage.get_by_role("textbox", name="0,00").click()
    mpage.get_by_role("cell", name="0").get_by_role("textbox").fill("153")

    # Confirma a alteração
    mpage.get_by_role("button", name=" Confirmar").click()
    mpage.get_by_role("button", name="Sim").click()

    # Valida se houve a alteração
    expect(mpage.get_by_text("Sucesso!")).to_be_visible()
    

def test_alterar_lote_increm_valor(mpage: Page):
    """Incrementa o valor dos financeiros em valor pré definido"""

    # Seleciona o incremento do valor
    mpage.get_by_role("checkbox", name="Alterar valor vencimento").check()
    mpage.get_by_role("cell", name="Novo valor").get_by_role("combobox").select_option("1: 2")

    # Insere o valor de acréscimo
    mpage.get_by_role("textbox", name="0,00").click()
    mpage.get_by_role("cell", name="0").get_by_role("textbox").fill("20")

    # Confirma a alteração
    mpage.get_by_role("button", name=" Confirmar").click()
    mpage.get_by_role("button", name="Sim").click()

    # Valida se houve a alteração
    expect(mpage.get_by_text("Sucesso!")).to_be_visible()


def test_alterar_lote_decrem_valor(mpage: Page): 
    """Decrementa o valor dos financeiros em valor pré definido""" 

    # Seleciona o decremento do valor
    mpage.get_by_role("checkbox", name="Alterar valor vencimento").check()
    mpage.get_by_role("cell", name="Novo valor").get_by_role("combobox").select_option("2: 3")

    # Insere o valor de decréscimo
    mpage.get_by_role("textbox", name="0,00").click()
    mpage.get_by_role("cell", name="0").get_by_role("textbox").fill("2000")

    # Confirma a alteração
    mpage.get_by_role("button", name=" Confirmar").click()

    # Valida se foi-se percebido um valor muito alto de redução
    expect(mpage.locator("#swal2-html-container")).to_contain_text("As parcelas com valor menor que o valor de redução serão zeradas")

    # Finaliza a confirmação da alteração
    mpage.get_by_role("button", name="Sim").click()

    # Valida se houve a alteração
    expect(mpage.get_by_text("Sucesso!")).to_be_visible()


def test_alterar_lote_nova_data(mpage: Page):
    """Altera a data de vencimento dos financeiros"""

    # Seleciona a alteração da data
    mpage.get_by_role("checkbox", name="Alterar data vencimento").check()

    # Insere uma nova data. 
    # A condição serve apenas para evitar de consumir todos os financeiros de uma situação
    if random.choice([True, False]):
        mpage.locator("input[name=\"data\"]").fill("2100-01-01")
    else:
        mpage.locator("input[name=\"data\"]").fill("2000-01-01")

    # Confirma a alteração
    mpage.get_by_role("button", name=" Confirmar").click()
    mpage.get_by_role("button", name="Sim").click()

    # Valida se houve a alteração
    expect(mpage.get_by_text("Sucesso!")).to_be_visible()


'''Erro na mensagem de confirmação, por conta do input de data vazio'''
def test_alterar_lote_increm_dias(mpage: Page):
    """Incrementa dias na data de vencimento dos financeiros"""

    # Seleciona o incremento de dias
    mpage.get_by_role("checkbox", name="Alterar data vencimento").check()
    mpage.get_by_role("cell", name="Nova data").get_by_role("combobox").select_option("1: 2")

    # Insere uma quantidade de dias
    mpage.get_by_role("row", name="Alterar data vencimento").get_by_role("spinbutton").click()
    mpage.get_by_role("row", name="Alterar data vencimento").get_by_role("spinbutton").fill("50")

    # Confirma a alteração
    mpage.get_by_role("button", name=" Confirmar").click()
    mpage.get_by_role("button", name="Sim").click()

    # Valida se houve a alteração
    expect(mpage.get_by_text("Sucesso!")).to_be_visible()


def test_alterar_lote_decrem_dias(mpage: Page):
    """Decrementa dias na data de vencimento dos financeiros"""

    # Seleciona o decremento de dias
    mpage.get_by_role("checkbox", name="Alterar data vencimento").check()
    mpage.get_by_role("cell", name="Nova data").get_by_role("combobox").select_option("2: 3")

    # Insere uma quantidade de dias
    mpage.get_by_role("row", name="Alterar data vencimento").get_by_role("spinbutton").click()
    mpage.get_by_role("row", name="Alterar data vencimento").get_by_role("spinbutton").fill("50")

    # Confirma a alteração
    mpage.get_by_role("button", name=" Confirmar").click()
    mpage.get_by_role("button", name="Sim").click()

    # Valida se houve a alteração
    expect(mpage.get_by_text("Sucesso!")).to_be_visible()


'''Cada vez que você fecha a confirmação e abre de novo, a quantidade de financeiros disponíveis
para alteração é incrementada pela quantidade real de financeiros disponível'''
def test_alterar_lote_filtro_aberto(mpage: Page):
    """Seleciona duas contas, uma aberta e outra vencida, e usando o filtro, altera somente a aberta"""

    # Seleciona o incremento do valor
    mpage.get_by_role("checkbox", name="Alterar valor vencimento").check()
    mpage.get_by_role("cell", name="Novo valor").get_by_role("combobox").select_option("1: 2")

    # Desmarca as parcelas vencidas
    mpage.get_by_role("checkbox", name="Parcelas vencidas").uncheck()

    # Confirma a alteração
    mpage.get_by_role("button", name=" Confirmar").click()

    # Valida se o filtro funcionou
    expect(mpage.locator("#swal2-html-container")).to_contain_text("1 conta(s) válida(s) para alteração. Deseja prosseguir?")

    # Finaliza a confirmação
    mpage.get_by_role("button", name="Sim").click()

    # Valida se houve a alteração
    expect(mpage.get_by_text("Sucesso!")).to_be_visible()


def test_alterar_lote_filtro_vencido(mpage: Page):
    """Seleciona duas contas, uma aberta e outra vencida, e usando o filtro, altera somente a vencida"""

    # Seleciona o incremento do valor
    mpage.get_by_role("checkbox", name="Alterar valor vencimento").check()
    mpage.get_by_role("cell", name="Novo valor").get_by_role("combobox").select_option("1: 2")

    # Desmarca as parcelas abertas
    mpage.get_by_role("checkbox", name="Parcelas em aberto").uncheck()

    # Confirma a alteração
    mpage.get_by_role("button", name=" Confirmar").click()

    # Valida se o filtro funcionou
    expect(mpage.locator("#swal2-html-container")).to_contain_text("1 conta(s) válida(s) para alteração. Deseja prosseguir?")

    # Finaliza a confirmação
    mpage.get_by_role("button", name="Sim").click()

    # Valida se houve a alteração
    expect(mpage.get_by_text("Sucesso!")).to_be_visible()


'''Implementar teste do filtro de número de parcela'''