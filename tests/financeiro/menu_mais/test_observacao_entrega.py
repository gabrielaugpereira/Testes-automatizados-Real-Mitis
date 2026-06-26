"""Fluxo CRUD para observação de entrega"""

from playwright.sync_api import Page, expect
import pytest
from collections.abc import Iterator

from auxiliares import DESCRICAO_PADRAO

'''Relatar bugs com a table'''

@pytest.fixture
def obs_page(fin_page: Page) -> Iterator[Page]:
    """
    Página personalizada para observação de entrega.

    Entra na rotina de financeiro, seleciona o primeiro do tipo "receita", 
    clica no mais opções e seleciona "observação de entrega".
    """

    # Seleciona o primeiro financeiro do tipo "receita"
    fin_page.get_by_text("Receita").first.click()

    # Entra nas observações de entrega
    fin_page.get_by_title("Mais opções").click()
    fin_page.locator("a").filter(has_text="Obs. entrega (F9)").click()

    # Retorna a página
    yield fin_page


def test_criar_obs(obs_page: Page):
    """Criação de observação"""
    
    # Insere conteúdo da observação
    obs_page.get_by_role("textbox", name="Texto da observação").click()
    obs_page.get_by_role("textbox", name="Texto da observação").fill(DESCRICAO_PADRAO)

    # Adiciona a observação
    obs_page.get_by_role("button", name=" Adicionar").click()


def test_ler_obs(obs_page: Page):
    """Leitura de observação"""

    # Valida se observação foi criada
    expect(obs_page.get_by_role("cell", name=DESCRICAO_PADRAO)).to_be_visible()


def test_atualizar_obs(obs_page: Page):
    """Atualização de observação"""

    # Edita e salva conteúdo da observação
    obs_page.get_by_title("Editar").click()
    obs_page.get_by_role("textbox", name="Texto da observação").fill("Teste automatizado editado - GAP")
    obs_page.get_by_role("button", name=" Salvar").click()

    # Valida se conteúdo foi alterado
    expect(obs_page.get_by_role("cell", name="Teste automatizado editado - GAP")).to_be_visible()


def test_remover_obs(obs_page: Page):
    """Remoção de observação"""

    # Remove a observação
    obs_page.get_by_title("Remover").click()

    # Valida se foi removida
    expect(obs_page.get_by_role("cell", name="Nenhum registro encontrado.")).to_be_visible()