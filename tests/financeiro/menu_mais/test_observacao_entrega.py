"""Fluxo CRUD para observação de entrega"""

from playwright.sync_api import Browser, Page, expect
import pytest

from auxiliares.default import new_page, pesquisar_rotina, DESCRICAO_PADRAO

'''Relatar bugs com a table'''

class _ModuleVariables:
    """Mantém a página disponível para todos os testes"""
    page: Page = None

@pytest.fixture(scope='module', autouse=True)
def fixt_abrir_tela_observacoes(browser: Browser):
    """Preparação para os testes"""

    page = new_page(browser)

    # Entra na criação de financeiro
    pesquisar_rotina(page, "568.FINANCEIRO")

    # Seleciona um financeiro
    page.get_by_text("Receita").first.click()

    # Entra nas observações de entrega
    page.get_by_title("Mais opções").click()
    page.locator("a").filter(has_text="Obs. entrega (F9)").click()

    # Disponibiliza a página para todos
    _ModuleVariables.page = page

    yield

    # Garante que a página seja fechada
    _ModuleVariables.page.close()


def test_criar_obs():
    """Criação de observação"""

    page = _ModuleVariables.page

    # Insere conteúdo da observação
    page.get_by_role("textbox", name="Texto da observação").click()
    page.get_by_role("textbox", name="Texto da observação").fill(DESCRICAO_PADRAO)

    # Adiciona a observação
    page.get_by_role("button", name=" Adicionar").click()


def test_ler_obs():
    """Leitura de observação"""

    page = _ModuleVariables.page

    # Valida se observação foi criada
    expect(page.get_by_role("cell", name=DESCRICAO_PADRAO)).to_be_visible()


def test_atualizar_obs():
    """Atualização de observação"""

    page = _ModuleVariables.page

    # Edita e salva conteúdo da observação
    page.get_by_title("Editar").click()
    page.get_by_role("textbox", name="Texto da observação").fill("Teste automatizado editado - GAP")
    page.get_by_role("button", name=" Salvar").click()

    # Valida se conteúdo foi alterado
    expect(page.get_by_role("cell", name="Teste automatizado editado - GAP")).to_be_visible()


def test_remover_obs():
    """Remoção de observação"""
    
    page = _ModuleVariables.page

    # Remove a observação
    page.get_by_title("Remover").click()

    # Valida se foi removida
    expect(page.get_by_role("cell", name="Nenhum registro encontrado.")).to_be_visible()