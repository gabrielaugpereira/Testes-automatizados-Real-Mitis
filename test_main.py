from playwright.sync_api import Browser, Page, expect
import pytest
import os

from vault.credenciais import *

# I love playwright

# Exceções personalizadas
class AuthenticationError(BaseException): pass

# Keywords personalizadas
'''def try_wait_for'''

# O caminho do diretório raíz do projeto
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# O caminho do arquivo dos cookies de autenticação
AUTH_PATH = os.path.join(ROOT_DIR, 'playwright/.auth/user.json')

# A url da página principal do sistema
AUTH_URL = 'https://erp-qa.mitis.com.br/#/'
HOME_PAGE_URL = AUTH_URL + 'in'

'''Usuário excedeu o número de "tentivas" de acesso'''
'''Novos submits de login, após o primeiro ter dado erro, não apagam a mensagem de erro, a menos
que ele próprio tenha mensagem de erro'''
'''Vários dos usuários válidos não entram, mas nenhuma mensagem aparece'''
# Realiza a autenticação no sistema.
# Se os cookies da sessão anterior ainda forem válidos, autentica usando eles.
# Senão, realiza login e salva os cookies
@pytest.fixture(autouse=True, scope='session')
def test_login(browser: Browser):
    return

    # Garante que o caminho do arquivo de autenticação existe
    if not os.path.exists(AUTH_PATH):
        # Caminho não existe, e arquivo é criado
        open(AUTH_PATH, 'w')
        context = browser.new_context()

    else:
        # Caminho existe, então o conteúdo do arquivo é carregado
        context = browser.new_context(storage_state=AUTH_PATH)

    page = context.new_page()

    # Abre a página
    page.goto(HOME_PAGE_URL)
    
    # Realiza o login comum
    try:
        page.wait_for_url(HOME_PAGE_URL, timeout=10000)

        # Informa o domínio
        page.get_by_role("textbox", name="Domínio").fill(DOMINIO)

        # Informa o nome
        page.get_by_role("textbox", name="Login").fill(LOGIN)

        # Informa a SENHA (esconder a senha)
        page.get_by_role("textbox", name="Senha").fill(SENHA)

        # Aperta para entrar
        page.get_by_role("button", name="Entrar").click()

    except: 
        # Login não necessário
        pass

    # Valida se entrou
    expect(page).to_have_url(HOME_PAGE_URL, timeout=15000)

    # Erro na autenticação
    '''try:
        elem = page.locator(".text-center.aviso")
        raise AuthenticationError("Erro na autenticação: " + elem.inner_text())
    except: pass'''

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
    page.wait_for_timeout(500)

    return page

# Pesquisa a rotina a partir do código da rotina e/ou nome da rotina. 
# Se estiver no modo de criação, irá clicar no "mais", para criar um novo objeto
def pesquisar_rotina(page: Page, nome: str, criacao: bool = False):
    page.get_by_role("combobox", name="Pesquisar rotina").click()

    if not criacao:
        page.get_by_label(nome).click()
    else:
        page.get_by_label(nome).first.get_by_role("button").first.click()

    # Curto tempo de espera
    page.wait_for_timeout(500)