from playwright.sync_api import Page, expect, sync_playwright
from seguro.credenciais import *
import pytest
import os

# Diretório com os dados de autenticação
AUTH_DIR = 'playwright/.auth/'

@pytest.fixture(scope='session', autouse=True)
def iniciar():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        # login(page)

        context.storage_state(path=os.path.join(AUTH_DIR, 'user.json'))

        browser.close()