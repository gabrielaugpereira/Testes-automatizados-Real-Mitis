"""
Funções e keywords para serem usadas com frequência, 
minimizando repetição de código
"""


from playwright.sync_api import Browser, Page

from conftest import AUTH_PATH, DEFAULT_TIMEOUT, HOME_PAGE_URL


"""Retorna uma página nova na home page, já autenticada e configurada"""
def new_page(browser: Browser):
    '''Tentar não fazer isso, apenas usar o context configurado pelo conftest, para DRY'''
    context = browser.new_context(
        no_viewport=True, 
        storage_state=AUTH_PATH, 
        record_video_dir='video/',
        )

    # Muda o tempo padrão de timeout
    context.set_default_timeout(DEFAULT_TIMEOUT)

    # Cria uma página e vai até a home page
    page = context.new_page()
    page.goto(HOME_PAGE_URL)

    # Garante que tudo esteja carregado
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