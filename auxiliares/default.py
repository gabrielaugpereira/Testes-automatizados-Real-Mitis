"""
Funções e keywords para serem usadas com frequência, 
minimizando repetição de código
"""

from playwright.sync_api import Browser, Page, TimeoutError
from collections.abc import Iterator

from conftest import AUTH_PATH, VIDEO_PATH, DEFAULT_TIMEOUT, HOME_PAGE_URL


"""Valor padrão a ser inserido como descrição em um novo registro"""
DESCRICAO_PADRAO = "Teste automatizado - GAP"

"""Valor padrão a ser inserido como descrição na edição de um registro"""
DESCRICAO_EDIT_PADRAO = "Teste automatizado não fui eu - GAP"


def page(browser: Browser) -> Iterator[Page]:
    """Retorna uma página nova na home page, já autenticada e configurada"""

    '''Tentar não fazer isso, apenas usar o context configurado pelo conftest, para DRY'''
    context = browser.new_context(
        no_viewport=True, 
        storage_state=AUTH_PATH, 
        record_video_dir=VIDEO_PATH,
        )
    '''DRY'''

    # Muda o tempo padrão de timeout
    context.set_default_timeout(DEFAULT_TIMEOUT)

    # Cria uma página e vai até a home page
    page = context.new_page()
    page.goto(HOME_PAGE_URL)

    # Garante que tudo esteja carregado
    page.wait_for_load_state()
    page.wait_for_timeout(500)

    # Retorna a page
    yield page

    # Fecha o browser, encerrando todo o contexto interno junto
    browser.close()


def pesquisar_rotina(page: Page, nome: str, *_, criacao: bool = False) -> None:
    """
    Pesquisa a rotina a partir do código da rotina e/ou nome da rotina. 
    Se estiver no modo de criação, irá clicar no botão "mais", para criar um novo objeto
    """
    
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

    except TimeoutError:
        # Se falhar, tenta apenas dar enter para entrar na rotina
        page.locator("input").first.press("Enter")
        
    # Curto tempo de espera
    page.wait_for_timeout(500)