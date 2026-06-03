# EXECUTAR: pytest
# FLAGS DE EXECUÇÃO:
* Com UI: --headed

* Definir navegador: --browser nome
* Vários navegadores: --browser nome --browser nome ...

* Módulo específico: nome_do_teste.py
* Vários módulos: nome_do_teste1.py nome_do_teste2.py ...

* Função específica: -k nome_da_função

* Rodar em paralelo: --numprocesses n (precisa instalar pytest-xdist)

* Depurar: PWDEBUG=1 pytest -s

# GRAVAR TESTES: playwright codegen https://link-para-abrir/

# COMANDOS:
* Dar check em checkbox:        locator.check()
* Tirar check de checkbox:      locator.uncheck()
* Clicar no elemento:           locator.click()
* Passar o mouse sobre:         locator.hover()
* Digitar dados em input:       locator.fill()
* Dar foco em um elemento:      locator.focus()
* "Press single key":           locator.press()
* Fazer upload de arquivo:      locator.set_input_files()
* Selecionar opção em dropdown: locator.select_option()
* Entre outros

# VERIFICAÇÕES:
* Checkbox está marcada:                expect(locator).to_be_checked()
* Controle está habilitado:             expect(locator).to_be_enabled()
* Elemento está visível:                expect(locator).to_be_visible()
* Elemento contém texto:                expect(locator).to_contain_text()
* Elemento tem atributo:                expect(locator).to_have_attribute()
* Lista de elementos tem n elementos:   expect(locator).to_have_count()
* "Element matches text":               expect(locator).to_have_text()	
* Elemento de input contém valor x:     expect(locator).to_have_value()
* Página tem título:                    expect(page).to_have_title()
* Págida tem url (ou está na url):      expect(page).to_have_url()
* Entre outros

# FUNÇÃO ANTES/DEPOIS DE CADA TESTE:
@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):

Fixture é um arranjo feito antes de um teste, para garantir que ele esteja no estado esperado para iniciar.
Autouse é usado para sinalizar que os testes seguintes devem, automaticamente, 
chamar este teste em específico, sem explicitar no próprio código.