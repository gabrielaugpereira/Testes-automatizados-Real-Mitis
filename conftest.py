"""
Arquivo padrão do pytest para configuração dos testes. 
Foi adotado também nesse sistema para configurações de urls, caminhos e parâmetros em geral.
"""


import os
import pytest

"""O caminho do diretório raíz do projeto"""
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

"""O caminho do arquivo dos cookies de autenticação"""
AUTH_PATH = os.path.join(ROOT_DIR, 'playwright/.auth/user.json')

"""O caminho para salvar os vídeos das falhas"""
VIDEO_PATH = os.path.join(ROOT_DIR, 'video/')


"""Urls importantes do sistema"""
AUTH_URL = 'https://erp-qa.mitis.com.br/#/'
HOME_PAGE_URL = AUTH_URL + 'in'


"""Timeout padrão"""
DEFAULT_TIMEOUT = 15000


"""Módulos com testes que sempre devem ser executados"""
pytest_plugins = ["test_main", "auxiliares/autenticacao", "auxiliares/limpa_ambiente"]


"""Configuração do browser"""
@pytest.fixture(scope="session")
def browser_type_launch_args():
    return {
        "headless": False,
        "args": ["--start-maximized"],
    }


"""Configurações do context"""
@pytest.fixture(scope="session")
def browser_context_args():
    return {
        "no_viewport": True,
        "storage_state": AUTH_PATH,
        "record_video_dir": "video/",
    }