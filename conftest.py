import os
import pytest

"""O caminho do diretório raíz do projeto"""
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

"""O caminho do arquivo dos cookies de autenticação"""
AUTH_PATH = os.path.join(ROOT_DIR, 'playwright/.auth/user.json')

"""Urls importantes do sistema"""
AUTH_URL = 'https://erp-qa.mitis.com.br/#/'
HOME_PAGE_URL = AUTH_URL + 'in'

"""Módulos com testes que sempre devem ser executados"""
pytest_plugins = ["test_main"]

"""Configuração do browser"""
@pytest.fixture(scope="session")
def browser_type_launch_args():
    return {
        "headless": False,
    }