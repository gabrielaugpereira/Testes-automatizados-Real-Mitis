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
├─.playwright/
├─auxiliares/
├─fixtures/
├─test-results/
├─tests/
├─.env
├─.gitignore
├─conftest.py
├─lista_comandos.md
├─pytest.ini
├─README.md
└─requirements.txt


## Configurando o sistema

Quando você entra no terminal para executar os testes, você pode adicionar flags que configuram a sua execução. Tanto o Pytest e seus plugins, quanto o Playwright e seus plugins, adicionam várias e várias flags, cada uma fornecendo um recurso diferente. No arquivo "pytest.ini", na configuração "addopts", você também pode adicionar essas flags de forma permanente, para não precisar escrever todas as vezes. Algumas das flags mais relevantes estão aqui explicadas:

* --headed: mostra o que o sistema está vendo, abrindo a página do navegador de forma visível a quem está rodando os testes
* --capture=no: mostra as saídas de print no momento em que elas acontecem, ao invés de capturar elas e mostrar apenas se der erro. alias: -s
* --reruns=n: define a quantidade n de vezes que um teste falho pode ser rodado novamente, tentando alcançar o sucesso, antes de ser considerado uma falha;
* verbosity: o quão detalhado será a saída do terminal em geral. As opções são: -qq, -q (ou --quiet), default (sem informar nada), -v (ou --verbose), -vv e -vvv. Porém, -vv e -vvv são usados apenas por alguns plugins, de forma que para a maior parte dos casos, não fazem diferença
* --tb=s: define o quão extenso será o traceback - o caminho até a falha no teste. As opções para s são: long, short, line e no
* --numprocesses=n: a quantidade de testes para rodar em paralelo. N pode tanto ser o número de testes (a documentação recomenda usar metade da quantidade de núcleos lógicos do dispositivo) quanto auto, onde o sistema define a quantidade ideal de processos
* --video=s e --tracing=s: usados para ativar as funcionalidades de vídeo (uma gravação do teste acontecendo) e tracing (uma gravação avançada e interativa, incluindo também estado do código fonte e do html). As opções para s são: on, off e retain-on-failure

## Executando testes

Todos / só um / por diretório

## Criando testes

Falar sobre padrão test_*

## Depurando o teste


## Resultados

## Referências? Licença?