from playwright.sync_api import expect, Error
import random
import re

from test_main import *

"""Fluxo CRUD para financeiros a pagar e a receber"""

'''Ambas as criações de financeiro estão tendendo ao preenchimento mínimo de informações. 
Preferencialmente mudar isso'''

# ================================================
# Operações de criação
# ================================================

"""Adiciona uma nova parcela ao financeiro"""
def add_nova_parcela(page: Page):
    # Seleciona uma forma de pagamento
    page.locator("#dropdownFormaPagamento > app-mts-forma-pagamento-dropdown > div > p-autocomplete > div > button").click()
    page.get_by_text("A VISTA - DINHEIRO - 1").click()

    # Informa o falor de vencimento
    page.get_by_role("row", name="Data vencimento").get_by_placeholder("0,00").click()
    page.get_by_role("row", name="Data vencimento").get_by_role("textbox").fill("1")
    page.get_by_role("row", name="Data vencimento").get_by_role("textbox").press("Tab")

    # Seleciona um plano de contas
    page.locator("app-mts-plano-contas-dropdown > .btn-group > .p-element.p-inputwrapper > .w-100 > .p-element.p-ripple").click()
    page.get_by_text("1/12 AVOS REPRESENTANTES").click()

    # Seleciona um centro de custo
    page.locator("app-mts-centro-custo-dropdown > .btn-group > .p-element.p-inputwrapper > .w-100 > .p-element.p-ripple").click()
    page.get_by_text("CENTRAL").click()

    # Adiciona ao plano de contas
    page.get_by_role("button", name=" Adicionar").click()

    # Valida se parcela foi adicionada
    expect(page.get_by_text("Adicionado!")).to_be_visible()

    # Valida se financeiro foi criado
    expect(page.get_by_text("Sucesso"))

"""Criação de financeiro a pagar"""
def test_criacao_financeiro_pagar(browser: Browser):
    # Entra na criação de financeiro
    page = home_page_e_rotina(browser, "568.FINANCEIRO", criacao=True)

    # Escreve uma descrição
    page.wait_for_timeout(800)
    descricao = "Teste automatizado - GAP"
    page.get_by_text("Adicionar descrição").click()
    page.get_by_role("textbox", name="Descrição do lançamento").fill(descricao)
    page.get_by_role("heading", name="Lançamento Teste automatizado").get_by_role("button").click()
    
    expect(page.locator("app-financeiro-cadastro")).to_contain_text(descricao)

    # Escolhe um fornecedor
    page.get_by_role("button").nth(5).click()
    page.get_by_text(re.compile("[0-9]{2}.[0-9]{3}.[0-9]{3}")).first.click()

    # Informa um número de documento
    page.get_by_role("textbox", name="Número do Documento").click()
    page.get_by_role("textbox", name="Número do Documento").fill(str(random.randint(10 ** 11, 10 ** 12 - 1)))

    page.get_by_role("textbox", name="Complemento").click()
    page.get_by_role("textbox", name="Complemento").fill(str(random.randint(10000, 99999)))

    # Adiciona uma parcela
    add_nova_parcela(page)

    # Salva o financeiro
    page.get_by_role("button", name=" Salvar").click()

    # Valida se foi criado
    expect(page.get_by_text("Salvo com sucesso!")).to_be_visible()


'''Depois de criado, o número do pedido deveria ser informado na linha reservada para isso.
Porém, quando você acessa o financeiro, a linha não mostra valor algum'''
"""Criação de financeiro a receber"""
def test_criacao_financeiro_receber(browser: Browser):
    # Entra na criação de um financeiro
    page = home_page_e_rotina(browser, "568.FINANCEIRO", criacao=True)

    # Informa que é um financeiro a receber
    page.get_by_role("radio", name="Receber").check()

    # Escreve uma descrição
    page.wait_for_timeout(800)
    descricao = "Teste automatizado - GAP"
    page.get_by_text("Adicionar descrição").click()
    page.get_by_role("textbox", name="Descrição do lançamento").fill(descricao)
    page.get_by_role("heading", name="Lançamento Teste automatizado").get_by_role("button").click()

    expect(page.locator("app-financeiro-cadastro")).to_contain_text(descricao)

    # Escolhe um cliente
    page.get_by_role("button").nth(5).click()
    page.get_by_text(re.compile("[0-9]{2}.[0-9]{3}.[0-9]{3}")).first.click()

    # Escolhe uma empresa
    page.get_by_role("button").nth(7).click()
    page.get_by_text("EMPRESA HOMOLOGACAO").click()

    # Informa um número de documento
    page.get_by_role("textbox", name="Número do Documento").click()
    page.get_by_role("textbox", name="Número do Documento").fill(str(random.randint(10 ** 11, 10 ** 12 - 1)))

    page.get_by_role("textbox", name="Complemento").click()
    page.get_by_role("textbox", name="Complemento").fill(str(random.randint(10000, 99999)))

    # Adiciona uma parcela
    add_nova_parcela(page)

    # Salva o financeiro
    page.get_by_role("button", name=" Salvar").click()
    
    # Valida se foi criado
    expect(page.get_by_text("Salvo com sucesso!")).to_be_visible()


# ================================================
# Operações de edição
# ================================================

'''Baixa de financeiros baixados é permitida'''
'''Atalhos da tela de financeiros não funcionando'''
'''Quando altera-se a situação de uma parcela de "aberto" para "vencido", ou vice e versa, alteração não acontece. Mesma coisa com pago vencido'''
"""Baixa de financeiro pela tela de edição dele"""
def test_baixa_financeiro_pagar_interna(browser: Browser):
    # Entra na listagem de financeiros
    page = home_page_e_rotina(browser, "568.FINANCEIRO")

    # Escolhe uma conta vencida
    page.get_by_text("VENCIDO").first.dblclick()

    # Seleciona para editar a primeira parcela
    page.get_by_title("Editar", exact=True).first.click()

    # Seleciona a situação como pago
    page.locator('select[name="situacao"]').select_option("4")

    # Seleciona uma conta
    page.get_by_role("button").nth(23).click()
    page.get_by_text("BANCO C6").click()

    # Apaga o caixa selecionado, para não dar o problema de o caixa estar fechado
    page.locator("app-mts-caixa-paf-dropdown > .btn-group > .p-element.p-inputwrapper > .w-100 > timesicon > .p-autocomplete-clear-icon > path").click()

    # Salva as alterações
    page.get_by_role("button", name=" Salvar").click()

    # Valida se alterações foram recebidas
    expect(page.get_by_text("Salvo com sucesso!")).to_be_visible()


'''Não está sendo possível acessar o menu, por responsividade falha'''
"""Baixa de financeiro pela tela de listagem de financeiros"""
def test_baixa_financeiro_pagar_externa(browser: Browser):
    raise NotImplementedError("Teste não implementado")


"""Executa criação, edição e exclusão de uma parcela"""
def test_fluxo_parcelas(browser: Browser):
    # Entra na listagem de financeiros
    page = home_page_e_rotina(browser, "568.FINANCEIRO")

    # Escolhe o primeiro financeiro
    page.locator(".btn.btn-light").first.click()

    # ----- Adiciona nova parcela -----
    page.get_by_role("button", name=" Adicionar Nova Parcela").click()
    add_nova_parcela(page)

    expect(page.get_by_text("Adicionado!")).to_be_visible()
    page.get_by_role("button", name="Itens").click()

    # ----- Edita a primeira parcela -----
    page.get_by_title("Editar", exact=True).click()
    page.locator("textarea[name=\"obs\"]").click()
    page.locator("textarea[name=\"obs\"]").fill("Parcela editada")
    page.get_by_role("button", name=" Salvar").click()

    expect(page.get_by_text("Salvo com sucesso!")).to_be_visible()
    page.get_by_role("button", name="Itens").click()

    # ----- Exclui a primeira parcela -----
    page.get_by_title("Excluir").first.click()
    page.get_by_role("button", name="Sim").click()

    expect(page.get_by_text("Registro excluído com sucesso!")).to_be_visible()


'''Número de tentativas de login é ilimitado?'''
"""Edita um financeiro a receber, adicionando valores a maioria dos campos"""
def test_edicao_financeiro_receber(browser: Browser):
    # Entra na listagem de financeiros
    page = home_page_e_rotina(browser, "568.FINANCEIRO")

    # Escolhe o primeiro financeiro a receber, e sua primeira parcela
    page.get_by_text("Receita").nth(8).dblclick()
    page.get_by_title("Editar").nth(1).click()

    # Preenche o funil
    page.get_by_role("button").nth(13).click()
    page.get_by_text("- Vendas Inicio").click()

    # Muda a situação
    page.locator("select[name=\"situacao\"]").select_option(label="Pago")

    # Muda a forma de pagamento do vencimento
    page.locator("app-mts-forma-pagamento-dropdown > .btn-group > .p-element.p-inputwrapper > .w-100 > .p-element.p-ripple").first.click()
    page.get_by_text("CARTÃO DE CRÉDITO - REDE - 32").click()

    # Muda a data do vencimento
    page.locator("input[name=\"dataVencimento\"]").click()
    page.get_by_text("12", exact=True).first.click()

    # Muda o valor de vencimento
    page.locator("#inputValorOriginal input").first.click()
    page.locator("#inputValorOriginal input").first.fill("200")

    # Preenche o valor de acréscimo
    page.pause()
    page.get_by_text("Acrésc($)").locator("xpath=ancestor::tr").locator("td").nth(1).click()
    page.get_by_text("Acrésc($)").locator("xpath=ancestor::tr").locator("td").nth(1).fill("20")

    # Valida o valor final
    expect(page.get_by_text("Valor final").locator("xpath=ancestor::tr").locator("td").last).to_have_value("220,00")

    # Preenche Desc($) Vencimento
    page.get_by_role("button", name=" Exibir mais detalhes").click()
    page.locator("#inputValorDesconto > .w-100").fill("40")

    # Preenche juros e multa
    page.locator("#inputJuros > .w-100").fill("80")
    page.locator("#inputMulta > .w-100").fill("160")

    # Preenche Ad($) e Desc($) real
    page.locator("#inputAcrescimo > .w-100").fill("10")
    page.locator(".table.border.mb-0 > tr:nth-child(8) > td:nth-child(4) > app-mts-monetario-input > .w-100").fill("5")

    # Preenche Forma de pagamento e data reais
    page.locator("#dropdownFormaPagamentoReal > app-mts-forma-pagamento-dropdown > .btn-group > .p-element.p-inputwrapper > .w-100 > .p-element.p-ripple").click()
    page.get_by_text("CARTÃO DÉBITO - REDE - 16").click()
    page.locator("input[name=\"dataPagamento\"]").click()
    page.get_by_text("20", exact=True).click()

    # Valida o valor real
    expect(page.locator("#inputValorPago > .w-100")).to_have_value("394,07")

    # Preenche assistente: Duplicar, fixo e dias
    '''Não entendi'''

    # Preenche SQ
    expect(page.locator("input[name=\"itemSq\"]")).to_have_value("1")

    # Preenche observação
    page.locator("textarea[name=\"obs\"]").fill("Pausa para observação")

    # Preenche departamento
    page.locator("app-mts-departamento-dropdown > .btn-group > .p-element.p-inputwrapper > .w-100 > .p-element.p-ripple").click()
    page.get_by_text("MITIS").click()

    # Preenche local carteira
    page.locator("app-mts-local-carteira-dropdown > .btn-group > .p-element.p-inputwrapper > .w-100 > .p-element.p-ripple").click()
    page.get_by_text("CONTA CAIXA 1379-0 (EUNÁPOLIS)").click()

    # Valida caixa e dá check em prejuízo
    expect(page.locator("input[name=\"caixa\"]")).not_to_have_value("")
    page.get_by_role("checkbox", name="Prejuizo").check()

    # Altera uma checkbox (previsão) do controle
    page.get_by_role("checkbox", name="Previsão").check()

    # Preenche Nº referência
    page.locator("input[name=\"numReferencia\"]").fill(str(random.randint(10 ** 10, 10 ** 11 - 1)))

    # Preenche conta
    page.locator("app-mts-conta-dropdown > .btn-group > .p-element.p-inputwrapper > .w-100 > .p-element.p-ripple").click()
    page.get_by_text("BANCO C6").click()

    # Preenche caixa paf
    page.locator("app-mts-caixa-paf-dropdown > .btn-group > .p-element.p-inputwrapper > .w-100 > .p-element.p-ripple").click()
    page.get_by_text(re.compile(r"[0-9]{11}")).click()

    # Preenche tipo do caixa paf
    page.locator("select[name=\"tipoCadastroCq\"]").select_option("1: 1")

    '''Está escrito carência jurso'''
    # Valida carência juros (dias)
    expect(page.get_by_role("spinbutton")).to_have_value("0")

    # Preenche documento externo, e seleciona a segunda checkbox
    page.locator("input[name=\"invoice\"]").fill(random.randint(10 ** 10, 10 ** 11 - 1))
    page.get_by_role("checkbox", name="Data recibo").check()

    # Preenche duplicata
    page.locator("input[name=\"numeroDuplicata\"]").fill(random.randint(10 ** 10, 10 ** 11 - 1))

    # Valida edição
    page.get_by_role("button", name=" Salvar").click()
    expect(page.get_by_text("Salvo com sucesso!")).to_be_visible()


# ================================================
# Operações de exclusão
# ================================================

"""Exclusão de financeiro a partir da exclusão de todas as suas parcelas"""
def test_exclusao_interna_financeiro(browser: Browser):
    # Entra na listagem de financeiros
    page = home_page_e_rotina(browser, "568.FINANCEIRO")

    # Seleciona o primeiro financeiro
    page.locator(".btn.btn-light").first.click()

    # Espera até que o botão de excluir apareça
    page.wait_for_selector(".pi-trash")

    # Exclui as parcelas do financeiro
    while page.is_visible(".pi-trash"):
        page.get_by_title("Excluir").first.click()

        # Confirma a exclusão
        page.get_by_role("button", name="Sim").click()

        # Valida se parcela foi excluída
        expect(page.get_by_text("Registro excluído com sucesso!")).to_be_visible()

        # Recarrega a página, para atualizar as informações
        page.reload()

        # Espera até que a página recarregue
        page.wait_for_selector(".btn-success")


'''Não está sendo possível acessar o menu, por responsividade falha'''
"""Exclusão de finceiro pela tela de listagem de financeiros"""
def test_exclusao_externa_financeiro(browser: Browser):
    raise Error("Falha no Real")

    # Entra na listagem de financeiros
    pesquisar_rotina(page, "568.FINANCEIRO")

    # Seleciona o financeiro e clica no menu mais
    page.get_by_text("ABERTO").first.click()
    page.get_by_title("Mais opções").click()

    # Seleciona para excluir e confirma
    
    page.get_by_role("button").get_by_text("Sim").click()

    # Valida se financeiro foi excluído
    expect(page.get_by_text("Sucesso!")).to_be_visible()