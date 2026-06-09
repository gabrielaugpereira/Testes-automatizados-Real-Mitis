from playwright.sync_api import Browser, expect
import pytest

from test_main import *

'''
Estava implementando, porém achei melhor focar em testes mais relevantes

@pytest.fixture()
def test_escolher_financeiros(browser: Browser): 

    # Abre o navegador
    page = goto_home_page(browser)

    # Entra na criação de financeiro
    pesquisar_rotina(page, "568.FINANCEIRO", criacao=True)

    # Seleciona 3 financeiros do tipo vencido
    page.get_by_text("VENCIDO").first.click(modifiers=["ControlOrMeta"])
    page.get_by_text("VENCIDO").nth(1).click(modifiers=["ControlOrMeta"])
    page.get_by_text("VENCIDO").nth(2).click(modifiers=["ControlOrMeta"])

def test_novo_valor(): pass
    
def test_incrementar_valor(): pass

def test_decrementar_valor(): pass

def test_nova_data(): pass

def test_incrementar_dias(): pass

def test_decrementar_dias(): pass'''

'''Futuramente testar também os filtros'''