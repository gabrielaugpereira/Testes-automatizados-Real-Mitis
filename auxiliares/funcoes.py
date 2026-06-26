"""
Funções auxiliares e keywords
"""

from playwright.sync_api import Page, TimeoutError


def pesquisar_rotina(page: Page, nome: str, *, criacao: bool = False) -> None:
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