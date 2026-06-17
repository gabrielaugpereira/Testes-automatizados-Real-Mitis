from playwright.sync_api import Browser, Page, expect
import pytest
import os

from conftest import AUTH_PATH, HOME_PAGE_URL, DEFAULT_TIMEOUT
from vault.credenciais import *

# I love playwright

"""Exceções personalizadas"""
class AuthenticationError(BaseException): pass

"""
Realiza a autenticação no sistema.
Se os cookies da sessão anterior ainda forem válidos, autentica usando eles.
Senão, realiza login e salva os cookies
"""
@pytest.fixture(autouse=True, scope='session')
def login(browser: Browser):
    # Garante que o caminho do arquivo de autenticação existe
    if not os.path.exists(AUTH_PATH):
        # Caminho não existe, e arquivo é criado
        open(AUTH_PATH, 'w')
        context = browser.new_context(no_viewport=True)

    else:
        # Caminho existe, então o conteúdo do arquivo é carregado
        context = browser.new_context(storage_state=AUTH_PATH)

    page = context.new_page()
    page.goto(HOME_PAGE_URL)
    
    try:
        page.wait_for_timeout(1000)
        page.wait_for_url(HOME_PAGE_URL, timeout=6500)

        # Login não necessário
    
    except: 
        # Realiza o login comum

        # Informa o domínio
        page.get_by_role("textbox", name="Domínio").fill(DOMINIO)

        # Informa o nome
        page.get_by_role("textbox", name="Login").fill(LOGIN)

        # Informa a SENHA (esconder a senha)
        page.get_by_role("textbox", name="Senha").fill(SENHA)

        # Aperta para entrar
        page.get_by_role("button", name="Entrar").click()
        
    # Valida se entrou
    expect(page).to_have_url(HOME_PAGE_URL, timeout=15000)

    # Salva os cookies da autenticação
    context.storage_state(path="playwright/.auth/user.json")

    # Fecha o navegador
    page.close()


"""Retorna uma página nova na home page, já autenticada e configurada"""
def new_page(browser: Browser) -> Page:
    context = browser.new_context(storage_state=AUTH_PATH)

    # Muda o tempo padrão de timeout
    context.set_default_timeout(DEFAULT_TIMEOUT)

    page = context.new_page()
    page.goto(HOME_PAGE_URL)

    page.wait_for_load_state()
    page.wait_for_timeout(500)

    return page


"""
Pesquisa a rotina a partir do código da rotina e/ou nome da rotina. 
Se estiver no modo de criação, irá clicar no botão "mais", para criar um novo objeto
"""
def pesquisar_rotina(page: Page, nome: str, *_, criacao: bool = False) -> None:
    page.get_by_role("combobox", name="Pesquisar rotina").click()
    page.wait_for_selector(".include-new-to-route")

    # Insere o nome, para não precisar scrollar até o item
    page.locator("input").first.fill(nome)

    try:
        if not criacao:
            page.get_by_label(nome).click()
        else:
            # Clica no "+" dentro do item
            page.get_by_label(nome).first.get_by_role("button").first.click()

    except:
        # Se falhar, tenta apenas dar enter para entrar na rotina
        page.locator("input").first.press("Enter")
        
    # Curto tempo de espera
    page.wait_for_timeout(500)