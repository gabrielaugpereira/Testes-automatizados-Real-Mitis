"""
Arquivo padrão do pytest para configuração dos testes. 
Foi adotado também nesse sistema para configurações de urls, caminhos e parâmetros em geral.
"""

from playwright.sync_api import Browser, BrowserContext, Page

import os
import pytest
from collections.abc import Iterator


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
"""O caminho do diretório raíz do projeto"""

AUTH_PATH = os.path.join(ROOT_DIR, '.playwright/.auth/user.json')
"""O caminho do arquivo dos cookies de autenticação"""

VIDEO_PATH = os.path.join(ROOT_DIR, '.tests_videos/')
"""O caminho para salvar os vídeos das falhas"""


AUTH_URL = 'https://erp-qa.mitis.com.br/#/'
"""Url da página de login"""

HOME_PAGE_URL = AUTH_URL + 'in'
"""Url da home page"""


DEFAULT_TIMEOUT = 15000
"""Timeout padrão"""


pytest_plugins = [
    "fixtures.autenticacao", 
    "fixtures.limpa_ambiente"
    ]
"""Módulos com fixtures que sempre devem ser executadas"""


@pytest.fixture(scope="session")
def browser_type_launch_args():
    """Configuração do browser"""

    return {
        # "headless": False,
        "args": ["--start-maximized"],
    }


@pytest.fixture
def context(browser: Browser):
    """Configuração do context"""

    # Cria um contexto sem viewport, com o caminho dos cookies e o caminho dos vídeos de feedback
    context = browser.new_context(
        no_viewport = True, 
        storage_state = AUTH_PATH, 
        record_video_dir = VIDEO_PATH,
    )

    # Muda o tempo padrão de timeout
    context.set_default_timeout(DEFAULT_TIMEOUT)

    # Retorna o context
    yield context

    # Fecha o context
    context.close()


@pytest.fixture
def page(context: BrowserContext) -> Iterator[Page]:
    """
    Criação personalizada de page.
    Retorna uma página nova na home page, já autenticada e configurada.
    """

    # Cria uma página e vai até a home page
    page = context.new_page()
    page.goto(HOME_PAGE_URL)

    # Garante que tudo esteja carregado
    page.wait_for_load_state()
    page.wait_for_timeout(500)

    # Retorna a page
    yield page