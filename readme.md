# TESTES AUTOMATIZADOS PARA ERP REAL

## Sobre

O sistema é um conjunto extenso de testes para o sistema ERP REAL, da Mitis Tecnologia. O fluxo dos testes automatizados inclue a autenticação no sistema; execução de diversos testes em diferentes rotinas; gravação interativa dos testes que falharam; e log final, informando vários dados sobre a execução.

Também existem outros recursos úteis disponíveis para uso no sistema, como a paralelização dos testes, emulação de dispositivos, variedade de navegadores, entre outros.

O objetivo do projeto é reduzir o esforço manual para garantir a qualidade do ERP; fornecer testes mais rápidos, assertivos e com mais cenários diferentes do que testes manuais; e fornecer uma ferramenta para os desenvolvedores do Real, que pode ser usada para obter um feedback mais ágil sobre se novas atualizações estão funcionando como esperado. O objetivo final, portanto, é eficientemente garantir a qualidade do Real.

## Pré requisitos

- Python 3.14+
- Pip 25+

## Setup

1. Clone o repositório
2. Crie um venv (ambiente virtual): `python -m venv .venv`
3. Ative o venv: `.venv/Scripts/activate`
4. Instale as dependências: `pip install -r requirements.txt`
5. Instale os drives de navegadores: `playwright install`

## Estrutura do projeto

Testes-automatizados-Real-Mitis/        
├─ .playwright/                 # Diretório usado pelo Playwright
|  └─ .auth/                        # Dados da autenticação
|     └─ cookies.json                   # Armazenamento dos cookies da autenticação
├─ auxiliares/                  # Funcionalidades auxiliares, como se fosse uma biblioteca interna
|  ├─ excecoes.py                   # Exceções personalizadas
|  ├─ funcoes.py                    # Funcionalidades úteis na forma de função
|  ├─ genericos.py                  # Fluxos de criação, atualização e remoção genéricos
|  └─ valores_padrao.py             # Valores para serem usados padronizadamente pelo sistema, como descrição para informar nos inputs
├─ fixtures/                    # Diretório para fixtures (funções para preparação do ambiente)
|  ├─ autenticacao.py               # Fixtures para entrar no sistema
|  └─ paginas_customizadas.py       # Fixtures ornecem páginas personalizadas, principalmente usadas para já receber a página na rotina
├─ test-results/                # Feedback em vídeo/tracing dos testes, para descobrir onde deu erro
|  └─ conteudo-interno              # Dividido por diretórios com o nome do teste executado
├─ tests/                       # Todos os testes do sistema. Separado por diretórios, majoritariamente agrupando por rotina
├─ .env                         # Credenciais de login. Tudo o que está nesse arquivo é tratado como variáveis de ambiente
├─ .gitignore                   # Nomes dos arquivos e diretórios a serem ignorados
├─ conftest.py                  # Configuração do sistema, do Pytest e do Playwright. Contém também constantes de caminho e url
├─ lista_comandos.md            # Comandos importantes para usar na criação de novos testes
├─ pytest.ini                   # Arquivo de preferências do pytest. Principalmente usado para adicionar flags permanentemente
├─ README.md                    # Documentação geral do sistema. Você está aqui
└─ requirements.txt             # Dependências do projeto, necessárias para a execução ou para utilizar certos recursos

No momento de instalação, o diretório ".playwright" ainda não existirá no projeto; isso porque ele é criado pelo próprio sistema após a primeira autenticação. Além disso, outros diretórios serão criados dentro do projeto, mas de forma diferente para cada dispositivo. Esses diretórios incluem cache de diversas camadas, o ambiente virtual (venv), e outros.

## Executando testes

Para rodar os testes, abra o terminal no diretório principal. Então, use o comando `pytest` para executar os testes. 
Por padrão, o pytest irá rodar todos eles, mas você pode escolher quais diretórios, módulos e/ou funções serão executados, adicionando o nome depois de pytest. O modelo é esse:

Para diretórios:
`pytest caminho_para_diretorio/diretorio/`

Para arquivos:
`pytest caminho_para_arquivo/test_arquivo.py`

Para funções:
`pytest caminho_para_arquivo/test_arquivo.py::test_funcao`

Você pode colocar vários desses no mesmo comando do terminal, para especificar todos os testes/arquivos/diretórios que você quer rodar.
Além disso, você pode usar a flag -k no terminal para filtrar por nome. Ela costuma ser usada no seguinte padrão:
`pytest -k "produto"`
Nesse modelo, ela é usada para executar todos os testes relacionados a produto. A flag também pode ser usada como um "finder" para o teste que você quer, sem precisar informar todo o caminho.

Após o final da execução dos testes, algumas informações úteis aparecerão no terminal, como as quantidades de testes que falharam/sucederam/entre outros resultados; e o caminho da falha dos testes que falharam, para auxiliar na depuração. A leitura dos dados é intuitiva após entender como funciona, apesar de ser em inglês. Recomendo que você se acostume com a saída do terminal, para poder obter as informações necessárias para usar os testes.

## Configurando a execução

Quando você entra no terminal para executar os testes, você pode adicionar flags que configuram a sua execução. Tanto o Pytest e seus plugins, quanto o Playwright e seus plugins, adicionam várias e várias flags, cada uma fornecendo um recurso diferente. No arquivo "pytest.ini", na configuração "addopts", você também pode adicionar essas flags de forma permanente, para não precisar escrever todas as vezes. Algumas das flags mais relevantes estão aqui explicadas:

* --headed: mostra o que o sistema está vendo, abrindo a página do navegador de forma visível a quem está rodando os testes
* --capture=no: mostra as saídas de print no momento em que elas acontecem, ao invés de capturar elas e mostrar apenas se der erro. alias: -s
* --reruns=n: define a quantidade n de vezes que um teste falho pode ser rodado novamente, tentando alcançar o sucesso, antes de ser considerado uma falha;
* verbosity: o quão detalhado será a saída do terminal em geral. As opções são: -qq, -q (ou --quiet), default (sem informar nada), -v (ou --verbose), -vv e -vvv. Porém, -vv e -vvv são usados apenas por alguns plugins, de forma que para a maior parte dos casos, não fazem diferença
* --tb=s: define o quão extenso será o traceback - o caminho até a falha no teste. As opções para s são: long, short, line e no
* --numprocesses=n: a quantidade de testes para rodar em paralelo. N pode tanto ser o número de testes (a documentação recomenda usar metade da quantidade de núcleos lógicos do dispositivo) quanto auto, onde o sistema define a quantidade ideal de processos
* --video=s e --tracing=s: usados para ativar as funcionalidades de vídeo (uma gravação do teste acontecendo) e tracing (uma gravação avançada e interativa, incluindo também estado do código fonte e do html). As opções para s são: on, off e retain-on-failure

## Criando testes

Para criar novos testes, o processo é relativamente simples, inclusive por conta da ferramenta de gravação do playwright. Porém, alguns padrões precisam ser observados.

- Primeiro, encontre o diretório ideal para o seu teste. Testes relacionados a registros maiores, como de produto, financeiro ou faturamento, recebem seus próprios diretórios, agrupados por rotina. Algumas vezes, inclusive, os testes são colocados dentro de diretórios dentro de diretórios. Um exemplo desse segundo é o "menu_mais/", que agrupa várias funcionalidades que estão dentro da rotina de financeiro.
Quando um teste é relacionado a registros muito pequenos, por outro lado, eles podem ser agrupados dentro do diretório "outros/", que diz respeito justamente a registros menores, e CRUDs simples e genéricos.
Lembre-se que todos os testes são colocados dentro do diretório "tests/", e que você pode sempre criar novos diretórios para colocar seus testes, se não houver um lugar ideal para colocar ele ainda.

- Segundo, encontre o arquivo ideal. Quando você está criando testes de fluxo CRUD, por exemplo, se o objeto for muito simples, todo o fluxo pode ser feito em um único arquivo. Quando o objeto for maior, pode ser melhor separar cada etapa em um arquivo diferente, especialmente se houver mais de uma única forma para uma mesma etapa (2 cadastros diferentes, por exemplo). Novamente, sempre que for necessário, crie um arquivo para escrever seus testes de forma modularizada, e com independência de responsabilidade. Note, porém, que todos os arquivos de testes devem iniciar com "test_".

- Terceiro, escreva o cabeçalho do teste. O cabeçalho deve, também, iniciar com "test_". Recomenda-se usar nomes descritivos, porém não excessivamente longos.

- Quarto, grave seu teste. Usando o comando `playwright codegen http://url_do_sistema`, o Playwright irá abrir duas janelas: uma com o navegador, para você interagir enquanto ele grava seus cliques, e uma com os passos que você tomou, transformados em código. Ao final da gravação, copie o código da segunda janela para o seu teste. Lembre-se de copiar o conteúdo, porque se o navegador for fechado, a janela também será.
Recomendo estudar um pouco sobre o codegen, para poder usar bem os recursos que ele oferece, uma vez que ele está substituindo a escrita manual do teste.

- Quinto, verifique o teste está funcionando. O codegen agiliza bastante o processo, mas ele não é 100% assertivo na escrita do código, e alguns elementos da tela podem não ser encontrados, ou misturados, na hora de rodar seu teste. Assim, execute seu teste pelo terminal, e execute manutenções nele, até que ele faça exatamente o que você espera, e dê sucesso. Para a manutenção do teste, recomendo estudos sobre escrita de testes com Playwright, para que você saiba quais são as principais funções usadas para escrever um teste, e possa executar uma boa manutenção do teste.

## Depurando os testes

A forma mais prática de depurar os testes é ver quais deram falhas, e abrir o tracing correspondente ao teste. O tracing fornece um vídeo interativo, com o qual é muito fácil de saber exatamente onde o teste falhou. Todos os tracings de falhas são automaticamente gravados e armazenados em "test_results/", através de uma flag no pytest.ini. Para abrir o tracing, use o comando `playwright show-trace nome_do_tracing.zip`. Uma janela interativa será aberta, e então é só usar o recurso para saber em qual etapa ocorreu a falha.

## Troubleshooting(mudar nome para português)

## Decisões internas de escrita de código

Uma escolha totalmente arbitrária na escrita dos testes foi o uso de três aspas simples para escrever coisas para fazer pelo código, onde elas aparecem ou perto do que elas se referem. Essa decisão não está dentro da pep8, nem de outra documentação de boas práticas (não até onde eu saiba).

## Resultados

## Referências? Licença?