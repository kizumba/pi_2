# Projeto Integrador 2
Desenvolver um software com framework web que utilize banco de dados, inclua script web (Javascript), nuvem, uso de API, acessibilidade, controle de versão e testes. Opcionalmente, incluir análise de dados

## Ferramentas usadas
- **Python**, precisa ser baixada e instalada.
- **Flask**, framework instalado pelo comando pip dentro do python.
- **Sqlite**, framework instalado pelo comando pip dentro do python. 
- **SQLAlchemy**, framework instalado pelo comando pip dentro do python.
- **Html**, não necessita instalçao.
- **Css**, não necessita instalçao.
- **Javascript**, não necessita instalçao.
- **Db Browser**, baixado e instalado.
- **Sql Studio**, baixado e instalado.
- **Visual Studio Code**, baixado e instalado.
- **Git**, baixado e instalado.
- **Github**, não precisa instalação.
- **Heroku CLI**, baixado e instalado.
- **LibreOffice**

## Progresso do desenvolvimento

# Desenvolvimento
## Sistema atual e projeto
### Sistema atual de formação de grupos para PI
Como funciona hoje o sistema de formação de grupos pela UNIVESP. 
1. O aluno entra em grupos abertos com ou sem integrantes oferecidos automaticamente pela UNIVESP.
2. Não tem nenhuma informação prévia dos integrantes.
3. O aluno selecio um grupo e confirmar para entrar.
### Sistema proposto pelo grupo para do PI2
1. O aluno faz seu login/senha para entrar no sistema
2. Na tela principal é listado todos os alunos que estão no mesmo PI
3. O aluno pode buscar integrantes para seu grupo com os marcadores: Curso, Polo, Interesse Acadêmico, Idioma, Trabalha e Hobby.
4. Informações como Telefone para contato, email alternativo e redes sociais estão disponíveis para o aluno entrar em contato com os integrantes desejados.

## Preparando ambiente de trabalho
### Criar pasta do Projeto
1. Criar pasta do meu_projeto
### Visual Studio Code
1. Abrir visual studio e abrir pasta do meu_projeto
2. Na barra de menu na opção Terminal, abrir novo terminal.
### Criar Ambiente virtual
1. Entrar na pasta cd .\caminho_do_projeto\meu_projeto pelo terminal
2. Digitar no console python -m venv venv
3. Esperar instalação
4. Ativar o ambiente virtuaL com o comando: digitar .\venv\Script\activate
5. O terminal vai ficar com (venv) no canto esquerdo: (venv) C:\caminho_do_projeto\meu_projeto
### Instalando Flask
1. Confirmado que o venv está ativo.
2. Digitar o comando no terminal: pip install flask
### Instalando SQLAlchemy
1. Comando: pip install flask-sqlalchemy

## Codificação
1. Executar .\venv\Scripts\activate
2. Para sair do ambiente virtual use o comando: deactive
### Diretórios e arquivos
#### app.py
1. Criar arquivo _app.py_
1. No terminal executar os comandos abaixo
1. $env:FLASK_APP="app"
1. $env:FLASK_ENV="development" ou $env:FLASK_DEBUG=1
1. flask run
1. _Acessar o endereço_ http://127.0.0.1:5000
1. _Para parar a execução do servidor_ CTRL+C

## Versionamento de código com Git/GitHub

## Usando Heroku para colocar o aplicativo na internet

# REFERÊNCIAS
## Referências Sites das Ferramentas
1. https://flask.palletsprojects.com/en/2.1.x/
2. https://www.sqlalchemy.org/
3. https://www.python.org/
4. https://www.sqlite.org/index.html
5. https://www.heroku.com
6. https://github.com/
7. https://git-scm.com/
8. https://sqlitestudio.pl/
9. https://sqlitebrowser.org/
10. https://pt-br.libreoffice.org/
11. https://code.visualstudio.com/

## Referências de Vídeos (Youtube)
**Não deixe de seguir o canal e curtir os vídeos para apoiá-los!!!**
### Flask
1. **Canal do Prof** https://www.youtube.com/playlist?list=PLAMprkYgnHJE7JITxTnE6M2crc-aZL_my
2. **Profa. Alba Lopes** https://www.youtube.com/c/ProfaAlbaLopes/playlists
3. **Filipe Morelli Developer** https://www.youtube.com/playlist?list=PLWhiA_CuQkbBhvPojHOPY81BmDt2eSfgI
4. **Hashtag Programação** https://www.youtube.com/watch?v=K2ejI4z8Mbg

## Referências Livros Pesquisados
GRINBERG, Miguel. Desenvolvimento web com Flask: desenvolvendo aplicações web com python. São Paulo: Novatec, 2018.

## Referências UNIVESP
ALVES, William Pereira. Projetos de sistemas Web: conceitos, estruturas, criação de banco de dados e ferramentas de desenvolvimento. São Paulo: Érica, 2015. Disponível em: <https://integrada.minhabiblioteca.com.br/reader/books/9788536532462/pageid/0>. Acesso em: 22 mar. 2022.

MACIEL, Francisco Marcelo de Barros. Python e Django: desenvolvimento web moderno e ágil. Rio de Janeiro: Alta Books, 2020. Disponível em: <https://integrada.minhabiblioteca.com.br/reader/books/9786555200973/epubcfi/6/2%5B%3Bvnd.vst.idref%3Dcover%5D!/4/2/2%4051:1>. Acesso em: 22 mar. 2022.

OLIVEIRA, Cláudio Luis Vieira; ZANETTI, Humberto Augusto Piovesana. JavaScript Descomplicado: Programação para Web, IOT e Dispositivos Móveis. São Paulo: Érica, 2020. Disponível em: <https://integrada.minhabiblioteca.com.br/reader/books/9788536533100/pageid/0>. Acesso em: 22 mar. 2022.

OLIVEIRA, Cláudio Luís Vieira; ZANETTI, Humberto Augusto Piovesana. JavaScript descomplicado: programação para web, IoT e dispositivos móveis. São Paulo: Érica, 2020. Disponível em: https://integrada.minhabiblioteca.com.br/reader/books/9788536533100/pageid/0. Acesso em: 01 abr. 2022.