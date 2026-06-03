from playwright.sync_api import Browser, expect
import pytest
import os

from seguro.credenciais import *

# I love playwright

# O caminho do diretório raíz do projeto
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# O caminho do arquivo dos cookies de autenticação
AUTH_PATH = os.path.join(ROOT_DIR, 'playwright/.auth/user.json')

# A url da página principal do sistema
HOME_PAGE_URL = 'https://erp-qa.mitis.com.br/#/in'

# Realiza o login no sistema, e salva os cookies para as próximas funções
@pytest.fixture(scope='module', autouse=True)
def test_login(browser: Browser):
    context = browser.new_context()
    page = context.new_page()

    # Abre a página
    page.goto(HOME_PAGE_URL)

    # Informa o domínio
    page.get_by_role("textbox", name="Domínio").fill(DOMINIO)

    # Informa o nome
    page.get_by_role("textbox", name="Login").fill(LOGIN)

    # Informa a SENHA (esconder a senha)
    page.get_by_role("textbox", name="Senha").fill(SENHA)

    # Aperta para entrar
    page.get_by_role("button", name="Entrar").click()

    # Valida se entrou
    expect(page).to_have_url(HOME_PAGE_URL, timeout=30000)

    # Salva os cookies da autenticação
    context.storage_state(path="playwright/.auth/user.json")

    # Fecha o navegador
    page.close()

# Modularização e reutilização de código, que retorna uma página nova, já autenticada, e na home page
def goto_home_page(browser: Browser):
    context = browser.new_context(storage_state=AUTH_PATH)
    page = context.new_page()
    page.goto(HOME_PAGE_URL)
    return page