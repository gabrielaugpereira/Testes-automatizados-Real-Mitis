from playwright.sync_api import Browser, Page, expect
import pytest

from test_main import *

"""Fluxo CRUD para observação de entrega"""

# Armazena a página que será usada pelos outros testes.
# Seu valor inicial é colocado pelo "test_abrir_rotina_financeiro"
class _ModuleVariables: 
    page: Page = None

# ======================================================
# Preparação para os testes
# ======================================================
@pytest.fixture(scope="module", autouse=True)
def test_abrir_rotina_financeiro(browser: Browser):
    # Abre o navegador
    page = goto_home_page(browser)

    # Entra na criação de financeiro
    pesquisar_rotina(page, "568.FINANCEIRO")

    # Seleciona um financeiro
    page.get_by_text("Receita").first.click()

    # Entra nas observações de entrega
    page.get_by_title("Mais opções").click()
    page.locator("a").filter(has_text="Obs. entrega (F9)").click()

    _ModuleVariables.page = page

# ======================================================
# Criação de observação
# ======================================================
def test_criar_obs():
    page = _ModuleVariables.page

    # Insere conteúdo da observação
    page.get_by_role("textbox", name="Texto da observação").click()
    page.get_by_role("textbox", name="Texto da observação").fill("Teste automatizado - GAP")

    # Adiciona a observação
    page.get_by_role("button", name=" Adicionar").click()

# ======================================================
# Leitura de observação
# ======================================================
def test_ler_obs():
    page = _ModuleVariables.page

    # Valida se observação foi criada
    expect(page.get_by_role("cell", name="Teste automatizado - GAP")).to_be_visible()

# ======================================================
# Atualização de observação
# ======================================================
def test_atualizar_obs():
    page = _ModuleVariables.page

    # Edita e salva conteúdo da observação
    page.get_by_title("Editar").click()
    page.get_by_role("textbox", name="Texto da observação").fill("Teste automatizado editado - GAP")
    page.get_by_role("button", name=" Salvar").click()

    # Valida se conteúdo foi alterado
    expect(page.get_by_role("cell", name="Teste automatizado editado - GAP")).to_be_visible()

# ======================================================
# Remoção de observação
# ======================================================
def test_remover_obs():
    page = _ModuleVariables.page

    # Remove a observação
    page.get_by_title("Remover").click()

    # Valida se foi removida
    expect(page.get_by_role("cell", name="Nenhum registro encontrado.")).to_be_visible()