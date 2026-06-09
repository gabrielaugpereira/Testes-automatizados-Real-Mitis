from playwright.sync_api import Browser, Page, expect
import pytest

from test_main import *

'''
Estava implementando, porém achei melhor focar em testes mais relevantes
'''

# Após o fixture, a página ficará disponível para todos os testes
class _ModuleVariables:
    page: Page = None

# Entra na rotina e disponibilida a página
@pytest.fixture(scope='module', autouse=True)
def test_entra_rotina_financeiro(browser: Browser): 
    # Abre o navegador
    page = goto_home_page(browser)

    # Entra na listagem de financeiros
    pesquisar_rotina(page, "568.FINANCEIRO")

    _ModuleVariables.page = page

# Seleciona três financeiros e entra no menu mais
@pytest.fixture()
def test_seleciona_financeiros():
    page = _ModuleVariables.page

    # Seleciona 3 financeiros do tipo vencido
    page.get_by_role("cell", name="VENCIDO").first.click(modifiers=["ControlOrMeta"])
    page.get_by_role("cell", name="VENCIDO").nth(1).click(modifiers=["ControlOrMeta"])
    page.get_by_role("cell", name="VENCIDO").nth(2).click(modifiers=["ControlOrMeta"])

    # Entra no menu mais e escolhe a alteração em lote
    page.get_by_title("Mais opções").click()
    page.locator("a").filter(has_text="Alterar em lote").click()

# Altera o valor dos financeiros para outro pré definido
def test_novo_valor():
    page = _ModuleVariables.page

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
    
# Incrementa o valor dos financeiros em valor pré definido 
def test_incrementar_valor(): 
    page = _ModuleVariables.page

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

# Decrementa o valor dos financeiros em valor pré definido 
def test_decrementar_valor(): 
    page = _ModuleVariables.page

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

def test_nova_data(): 
    page = _ModuleVariables.page

    # Seleciona a alteração da data
    page.get_by_role("checkbox", name="Alterar data vencimento").check()

    # Insere uma nova data passada
    page.locator("input[name=\"data\"]").fill("2000-01-01")

    # Confirma a alteração
    page.get_by_role("button", name=" Confirmar").click()
    page.get_by_role("button", name="Sim").click()

    # Valida se houve a alteração
    expect(page.get_by_text("Sucesso!")).to_be_visible()

'''Erro na mensagem de confirmação, por conta do input de data vazio'''
def test_incrementar_dias(): 
    page = _ModuleVariables.page

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

def test_decrementar_dias(): 
    page = _ModuleVariables.page

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


'''Futuramente testar também os filtros'''