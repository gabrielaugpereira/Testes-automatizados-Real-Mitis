"""
Arquivo padrão do pytest para configuração dos testes. 
Foi adotado também nesse sistema para configurações de urls, caminhos e parâmetros em geral.
"""

from playwright.sync_api import Browser, BrowserContext, Page

from datetime import datetime
import os
import pytest
from collections.abc import Iterator


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
"""O caminho do diretório raíz do projeto"""

AUTH_PATH = os.path.join(ROOT_DIR, '.playwright/.auth/user.json')
"""O caminho do arquivo dos cookies de autenticação"""

RESULTS_PATH = os.path.join(ROOT_DIR, '.tests_results/')
"""O caminho para os feedbacks de testes"""

VIDEO_PATH = os.path.join(RESULTS_PATH, 'videos/')
"""O caminho para os vídeos dos testes"""


AUTH_URL = 'https://erp-qa.mitis.com.br/#/'
"""Url da página de login"""

HOME_PAGE_URL = AUTH_URL + 'in'
"""Url da home page"""


DEFAULT_TIMEOUT = 15000
"""Timeout padrão"""


pytest_plugins = [
    "fixtures.autenticacao",
    "fixtures.limpa_ambiente",
    "fixtures.paginas_customizadas",
    ]
"""Módulos com fixtures que sempre devem ser executadas"""


@pytest.fixture(scope="session")
def browser_type_launch_args():
    """Configuração do browser"""

    return {
        "headless": False,
        "args": ["--start-maximized"],
    }


'''Modularizar para fixtures'''
@pytest.fixture
def context(browser: Browser):
    """
    Configuração do context.
    Se o arquivo de cookies não existir, será criado; se existir mas estiver vazio, será reiniciado.
    Em ambas, o context não usará o arquivo, e será necessário autenticar
    """

    # Parâmetros que serão passados para criar um context.
    # no_viewport: para abrir em tela cheia;
    # record_video_dir: o diretório de vídeos gravados.
    kwargs = {
        "no_viewport": True, 
        "record_video_dir": VIDEO_PATH,
    }

    # Se não existir, ou se estiver vazio
    if not os.path.exists(AUTH_PATH) or os.path.getsize(AUTH_PATH) == 0:
        # Cria se não existir, reinicia se existir
        open(AUTH_PATH, 'w')
    else:
        # Adiciona o caminho dos cookies como parâmetro
        kwargs["storage_state"] = AUTH_PATH

    # Cria um contexto e configura
    _context = browser.new_context(**kwargs)
    _context.set_default_timeout(DEFAULT_TIMEOUT)

    # Configura o rastreamento do context
    _context.tracing.start(
        screenshots=True, 
        snapshots=True, 
        # sources=True
    )

    # Retorna o context
    yield _context

    # Formato da data a ser usada como nome para o trace
    format = r"%Y-%m-%d-%H-%M-%S"

    # Caminho relativo do arquivo
    path = os.path.join(RESULTS_PATH, f"{datetime.now().strftime(format)}.zip")

    # Caminho absoluto do arquivo
    path = os.path.join(ROOT_DIR, path)

    # Encerra o tracing e fecha o context
    _context.tracing.stop(path=path)
    _context.close()


@pytest.fixture
def page(context: BrowserContext) -> Iterator[Page]:
    """
    Criação personalizada de page.
    Retorna uma página nova na home page, já autenticada e configurada.
    """

    # Cria uma página e vai até a home page
    _page = context.new_page()
    _page.goto(HOME_PAGE_URL)

    # Garante que tudo esteja carregado
    _page.wait_for_load_state()
    _page.wait_for_timeout(500)

    # Retorna a page
    yield _page