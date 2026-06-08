from playwright.sync_api import Browser, Page, expect
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
@pytest.fixture(autouse=True, scope='session')
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

# Retorna uma página nova na home page, já autenticada e configurada
def goto_home_page(browser: Browser):
    context = browser.new_context(storage_state=AUTH_PATH)

    # Muda o tempo padrão de timeout
    context.set_default_timeout(15000)

    page = context.new_page()
    page.goto(HOME_PAGE_URL)

    page.wait_for_load_state()
    page.wait_for_timeout(1000)

    return page

# Pesquisa a rotina a partir do código da rotina e/ou nome da rotina. 
# Se estiver no modo de criação, irá clicar no "mais", para criar um novo objeto
def pesquisar_rotina(page: Page, nome: str, criacao: bool = False):
    page.get_by_role("banner").get_by_role("button").click()

    if not criacao:
        page.get_by_label(nome).click()
    else:
        page.get_by_label(nome).first.get_by_role("button").first.click()

    # Curto tempo de espera
    page.wait_for_timeout(1000)