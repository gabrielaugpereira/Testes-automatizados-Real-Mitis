from playwright.sync_api import Browser, expect, Error
import random

from test_main import *

"""Fluxo CRUD para financeiros a pagar e a receber"""

'''Ambas as criações de financeiro estão tendendo ao preenchimento mínimo de informações. 
Preferencialmente mudar isso'''

# Criação de financeiro a pagar
def test_criacao_financeiro_pagar(page: Page):
    # Entra na criação de financeiro
    pesquisar_rotina(page, "568.FINANCEIRO", criacao=True)

    # Escreve uma descrição
    page.wait_for_timeout(800)
    page.get_by_text("Adicionar descrição").click()
    page.get_by_role("textbox", name="Descrição do lançamento").fill("Teste automatizado - GAP")
    page.get_by_role("heading", name="Lançamento Teste automatizado").get_by_role("button").click()

    # Escolhe um fornecedor
    page.get_by_role("button").nth(5).click()
    page.get_by_text("791 25.991.826 WASHINGTON").click()

    # Informa um número de documento
    page.get_by_role("textbox", name="Número do Documento").click()
    page.get_by_role("textbox", name="Número do Documento").fill(str(random.randint(100000000000, 999999999999)))

    page.get_by_role("textbox", name="Complemento").click()
    page.get_by_role("textbox", name="Complemento").fill(str(random.randint(10000, 99999)))

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

    # Salva o financeiro
    page.get_by_role("button", name=" Salvar").click()

    # Valida se foi criado
    expect(page.get_by_text("Salvo com sucesso!")).to_be_visible()


'''Depois de criado, o número do pedido deveria ser informado na linha reservada para isso.
Porém, quando você acessa o financeiro, a linha não mostra valor algum'''
# Criação de financeiro a receber
def test_criacao_financeiro_receber(page: Page):
    # Entra na criação de um financeiro
    pesquisar_rotina(page, "568.FINANCEIRO", criacao=True)

    # Informa que é um financeiro a receber
    page.get_by_role("radio", name="Receber").check()

    # Escreve uma descrição
    page.get_by_text("Adicionar descrição").click()
    page.get_by_role("textbox", name="Descrição do lançamento").fill("Teste automatizado - GAP")
    page.get_by_role("heading", name="Lançamento Teste automatizado").get_by_role("button").click()

    # Escolhe um cliente
    page.get_by_role("button").nth(5).click()
    page.get_by_text("109194 $.O.$ - FOMENTO").click()

    # Escolhe uma empresa
    page.get_by_role("button").nth(7).click()
    page.get_by_text("EMPRESA HOMOLOGACAO").click()

    # Informa um número de documento
    page.get_by_role("textbox", name="Número do Documento").click()
    page.get_by_role("textbox", name="Número do Documento").fill(str(random.randint(100000000000, 999999999999)))

    page.get_by_role("textbox", name="Complemento").click()
    page.get_by_role("textbox", name="Complemento").fill(str(random.randint(10000, 99999)))

    # Escolhe um tipo de documento para a nota fiscal
    page.get_by_role("button").nth(9).click()
    page.get_by_text("EMPRESA 02").click()
    
    # Insere o valor do contrato
    page.get_by_role("textbox", name="0,00").nth(1).click()
    page.get_by_role("textbox").nth(4).fill("1")
    page.get_by_role("textbox").nth(4).press("Tab")

    # Insere a data de emissão
    page.locator("input[name=\"dataEmissao\"]").click()
    page.locator("input[name=\"dataEmissao\"]").press("ControlOrMeta+a")
    page.locator("input[name=\"dataEmissao\"]").fill("01/01/2000")

    # Insere a data de entrada/saída
    page.locator("input[name=\"dataEntradaSaida\"]").click()
    page.locator("input[name=\"dataEntradaSaida\"]").press("ControlOrMeta+a")
    page.locator("input[name=\"dataEntradaSaida\"]").fill("01/01/2100")

    # Seleciona uma forma de pagamento
    page.locator("app-mts-forma-pagamento-dropdown > .btn-group > .p-element.p-inputwrapper > .w-100 > .p-element.p-ripple").click()
    page.get_by_text("A VISTA - DINHEIRO - 1").click()

    # Informa o valor
    page.locator("#inputValorOriginal > .w-100").click()
    page.locator("#inputValorOriginal > .w-100").fill("1")

    # Salva o financeiro
    page.get_by_role("button", name=" Salvar").click()
    
    # Valida se foi criado
    expect(page.get_by_text("Salvo com sucesso!")).to_be_visible()


'''Baixa de financeiros baixados é permitida'''
'''Atalhos da tela de financeiros não funcionando'''
'''Quando altera-se a situação de uma parcela de "aberto" para "vencido", ou vice e versa, alteração não acontece. Mesma coisa com pago vencido'''
# Baixa de financeiro pela tela de edição dele
def test_baixa_financeiro_pagar_interna(page: Page):
    # Entra na listagem de financeiros
    pesquisar_rotina(page, "568.FINANCEIRO")

    # Escolhe uma conta vencida
    page.get_by_text("VENCIDO").first.dblclick()

    # Seleciona para editar a primeira parcela
    page.get_by_title("Editar", exact=True).first.click()

    # Seleciona a situação como pago
    page.locator('select[name="situacao"]').select_option("4")

    # Seleciona uma conta
    page.get_by_role("tr").nth(14).get_by_role("button").first.click()
    page.get_by_text("BANCO C6").click()

    # Apaga o caixa selecionado, para não dar o problema de o caixa estar fechado
    page.locator("app-mts-caixa-paf-dropdown > .btn-group > .p-element.p-inputwrapper > .w-100 > timesicon > .p-autocomplete-clear-icon > path").click()

    # Salva as alterações
    page.get_by_role("button", name=" Salvar").click()

    # Valida se alterações foram recebidas
    expect(page.get_by_text("Salvo com sucesso!")).to_be_visible()


'''Não está sendo possível acessar o menu, por responsividade falha'''
# Baixa de financeiro pela tela de listagem de financeiros
def test_baixa_financeiro_pagar_externa(page: Page):
    raise NotImplementedError("Teste não implementado")


# Exclusão de financeiro a partir da exclusão de todas as suas parcelas
def test_exclusao_interna_financeiro(page: Page):
    # Entra na listagem de financeiros
    pesquisar_rotina(page, "568.FINANCEIRO")

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
# Exclusão de finceiro pela tela de listagem de financeiros
def test_exclusao_externa_financeiro(page: Page):
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