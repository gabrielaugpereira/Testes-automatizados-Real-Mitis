"""Fixtures usadas para autenticar no sistema"""

from playwright.sync_api import Browser, TimeoutError, expect
import pytest
import os
from dotenv import load_dotenv

from conftest import AUTH_PATH, HOME_PAGE_URL, VIDEO_PATH

"""Carrega os dados de .dotenv como variáveis de ambiente"""
load_dotenv()

@pytest.fixture(autouse=True, scope='session')
def fixt_login(browser: Browser):
    """
    Realiza a autenticação no sistema.
    Se os cookies da sessão anterior ainda forem válidos, autentica usando eles.
    Senão, realiza login e salva os cookies
    """
    
    # Garante que o caminho do arquivo de autenticação existe, e que o arquivo não está vazio
    if not os.path.exists(AUTH_PATH) or os.path.getsize(AUTH_PATH) == 0:
        # Se arquivo não existe, é criado; senão, é resetado
        open(AUTH_PATH, 'w')
        context = browser.new_context(
            no_viewport=True, 
            # storage_state=AUTH_PATH, 
            record_video_dir=VIDEO_PATH,
            )
        '''DRY'''

    else:
        # Caminho existe, então o conteúdo do arquivo é carregado
        context = browser.new_context(
            no_viewport=True, 
            storage_state=AUTH_PATH, 
            record_video_dir=VIDEO_PATH,
            )
        '''DRY'''

    page = context.new_page()
    page.goto(HOME_PAGE_URL)
    
    try:
        page.wait_for_timeout(1000)
        page.wait_for_url(HOME_PAGE_URL, timeout=6500)

        # Login não necessário
    
    except TimeoutError: 
        # Realiza o login comum

        # Informa o domínio
        page.get_by_role("textbox", name="Domínio").fill(os.environ["DOMINIO"])

        # Informa o nome
        page.get_by_role("textbox", name="Login").fill(os.environ["LOGIN"])

        # Informa a SENHA (esconder a senha)
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
            pass
        
    # Valida se entrou
    expect(page).to_have_url(HOME_PAGE_URL, timeout=15000)

    # Salva os cookies da autenticação
    context.storage_state(path=AUTH_PATH)

    # Fecha o navegador
    page.close()