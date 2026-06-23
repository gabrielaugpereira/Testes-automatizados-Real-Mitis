"""Fluxo CRUD para observação de entrega"""

from playwright.sync_api import Page, expect
import pytest
from collections.abc import Iterator

from auxiliares.default import pesquisar_rotina, DESCRICAO_PADRAO

'''Relatar bugs com a table'''

@pytest.fixture(scope="module")
def mpage(page: Page) -> Iterator[Page]:
    """
    Uma mesma página usada por todos os testes do módulo, encerrada apenas no final.

    Entra na rotina de financeiro, seleciona o primeiro do tipo "receita", clica no mais opções e seleciona "observação de entrega".

    Por baixo dos panos, o resultado dessa função é injetado em todos os testes do módulo.

    Mpage vem de "module page".
    """

    # Entra na listagem de financeiros
    pesquisar_rotina(page, "568.FINANCEIRO")

    # Seleciona o primeiro financeiro do tipo "receita"
    page.get_by_text("Receita").first.click()

    # Entra nas observações de entrega
    page.get_by_title("Mais opções").click()
    page.locator("a").filter(has_text="Obs. entrega (F9)").click()

    # Retorna a página
    yield page


def test_criar_obs(mpage: Page):
    """Criação de observação"""
    
    # Insere conteúdo da observação
    mpage.get_by_role("textbox", name="Texto da observação").click()
    mpage.get_by_role("textbox", name="Texto da observação").fill(DESCRICAO_PADRAO)

    # Adiciona a observação
    mpage.get_by_role("button", name=" Adicionar").click()


def test_ler_obs(mpage: Page):
    """Leitura de observação"""

    # Valida se observação foi criada
    expect(mpage.get_by_role("cell", name=DESCRICAO_PADRAO)).to_be_visible()


def test_atualizar_obs(mpage: Page):
    """Atualização de observação"""

    # Edita e salva conteúdo da observação
    mpage.get_by_title("Editar").click()
    mpage.get_by_role("textbox", name="Texto da observação").fill("Teste automatizado editado - GAP")
    mpage.get_by_role("button", name=" Salvar").click()

    # Valida se conteúdo foi alterado
    expect(mpage.get_by_role("cell", name="Teste automatizado editado - GAP")).to_be_visible()


def test_remover_obs(mpage: Page):
    """Remoção de observação"""

    # Remove a observação
    mpage.get_by_title("Remover").click()

    # Valida se foi removida
    expect(mpage.get_by_role("cell", name="Nenhum registro encontrado.")).to_be_visible()