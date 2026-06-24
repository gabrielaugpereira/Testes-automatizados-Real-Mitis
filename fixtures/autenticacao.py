"""Fixtures usadas para autenticar no sistema"""

from playwright.sync_api import BrowserContext, Page, TimeoutError, expect
import pytest
import os
from dotenv import load_dotenv

from conftest import AUTH_PATH, HOME_PAGE_URL

"""Carrega os dados de .dotenv como variáveis de ambiente"""
load_dotenv()


def login(page: Page):
    """
    Realiza o login. É necessário já estar na tela de login.
    """
    
    # Informa os campos necessários
    page.get_by_role("textbox", name="Domínio").fill(os.environ["DOMINIO"])
    page.get_by_role("textbox", name="Login").fill(os.environ["LOGIN"])
    page.get_by_role("textbox", name="Senha").fill(os.environ["SENHA"])

    # Aperta para entrar
    page.get_by_role("button", name="Entrar").click()

    try:
        # Verifica se é necessário selecionar a empresa
        page.get_by_role("heading", name="109").hover(timeout=4000)

        # Seleciona a empresa 109
        page.get_by_role("textbox", name="Informe a empresa").click()
        page.get_by_role("textbox", name="Informe a empresa").fill("109")
        page.get_by_text("Selecione").first.click()

    except TimeoutError: 
        # Se chegou aqui, não é necessário selecionar a empresa
        pass


@pytest.fixture(autouse=True, scope='session')
def autenticacao(context: BrowserContext):
    """
    Realiza a autenticação no sistema.
    Se os cookies da sessão anterior ainda forem válidos, autentica usando eles.
    Senão, realiza login e salva os cookies
    """

    page = context.new_page()
    page.goto(HOME_PAGE_URL)
    
    try:
        page.wait_for_timeout(1000)
        page.wait_for_url(HOME_PAGE_URL, timeout=6500)

        # Se chegou até aqui, os cookies funcionaram, e autenticação foi bem sucedida
    
    except TimeoutError: 
        # Se chegou aqui, os cookies não funcionaram, ou não foram usados, e login é necessário

        login(page)
        
    # Valida se entrou
    expect(page).to_have_url(HOME_PAGE_URL, timeout=15000)

    # Salva os cookies da autenticação
    context.storage_state(path=AUTH_PATH)

    # Fecha o navegador
    page.close()