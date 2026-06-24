"""
Páginas customizadas para rotinas específicas, usados por várias partes do sistema.
Entram na rotina esperada, e eventualmente realizam outros procedimentos dentro dela.
"""

from playwright.sync_api import Page
import pytest
from collections.abc import Iterator

from auxiliares.default import pesquisar_rotina


@pytest.fixture
def fin_page(page: Page) -> Iterator[Page]:
    """
    Page personalizada para financeiro.
    Apenas entra na rotina.
    """

    pesquisar_rotina(page, "FINANCEIRO")
    yield page


@pytest.fixture
def new_fin_page(page: Page) -> Iterator[Page]:
    """
    Page personalizada para criação de financeiro.
    Entra na rotina, na parte de criação.
    """

    pesquisar_rotina(page, "FINANCEIRO", criacao=True)
    yield page


@pytest.fixture
def first_fin_page(fin_page: Page) -> Iterator[Page]:
    """
    Página personalizada para interagir com um financeiro.
    Entra na rotina de financeiro, dentro do primeiro deles.
    """

    # Escolhe o primeiro financeiro
    fin_page.locator(".btn.btn-light").first.click()

    yield fin_page


@pytest.fixture
def prod_page(page: Page) -> Iterator[Page]:
    """
    Página personalizada para a rotina de produto.
    Apenas entra na rotina.
    """

    pesquisar_rotina(page, "PRODUTO")
    yield page


@pytest.fixture
def new_prod_page(page: Page) -> Iterator[Page]:
    """
    Página personalizada para criação de produto.
    Entra na rotina, na parte de criação.
    """

    pesquisar_rotina(page, "PRODUTO", criacao=True)
    yield page


@pytest.fixture
def vend_page(page: Page) -> Iterator[Page]:
    """
    Página personalizada para a rotina de vendas.
    Apenas entra na rotina.
    """

    pesquisar_rotina(page, "VENDAS")
    yield page


@pytest.fixture
def new_vend_page(page: Page) -> Iterator[Page]:
    """
    Página personalizada para criação de vendas.
    Entra na rotina, na parte de criação.
    """

    pesquisar_rotina(page, "VENDAS", criacao=True)
    yield page