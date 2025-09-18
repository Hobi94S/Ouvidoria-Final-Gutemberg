Sistema de Ouvidoria
Projeto desenvolvido para a disciplina de Programação em Linguagem Estruturada.

Um sistema de ouvidoria simples, baseado em linha de comando (CLI), que permite aos usuários gerenciar manifestações como reclamações, sugestões e elogios. Este projeto foi desenvolvido como requisito avaliativo na cadeira de Programação em Linguagem Estruturada, ministrada pelo Professor Daniel Abella, durante o período letivo de 2025.1.

O sistema interage com um banco de dados MySQL para garantir a persistência dos dados, permitindo que as operações sejam salvas e consultadas a qualquer momento.

✨ Funcionalidades
O sistema oferece um menu interativo com as seguintes operações CRUD (Create, Read, Delete):

Listar todas as manifestações: Exibe um resumo de todas as manifestações cadastradas no banco de dados.

Adicionar uma nova manifestação: Permite ao usuário registrar um novo evento, escolhendo entre os tipos "Reclamação", "Elogio" ou "Sugestão".

Buscar uma manifestação específica: Procura e exibe os detalhes completos de uma manifestação a partir de seu código único.

Remover uma manifestação: Exclui um registro do sistema utilizando seu código como identificador.

Exibir a contagem total: Mostra o número total de manifestações atualmente registradas.

💻 Tecnologias Utilizadas
Linguagem de Programação: Python

Banco de Dados: MySQL

Interface: Terminal / Linha de Comando (CLI)

Biblioteca de Conexão: mysql-connector-python (ou similar)

🚀 Como Executar o Projeto
Para executar este projeto em sua máquina local, siga os passos abaixo.

Pré-requisitos
Python 3.x instalado.

Servidor de banco de dados MySQL ativo.

A biblioteca Python para conectar ao MySQL. Você pode instalá-la com o pip:

Bash

pip install mysql-connector-python
1. Configuração do Banco de Dados
Antes de executar o código, você precisa criar o banco de dados e a tabela que o sistema utilizará. Execute os seguintes comandos SQL no seu cliente MySQL:

SQL

-- 1. Crie o banco de dados (se ainda não existir)
CREATE DATABASE IF NOT EXISTS Ouvidoria;

-- 2. Use o banco de dados recém-criado
USE Ouvidoria;

-- 3. Crie a tabela para armazenar as manifestações
CREATE TABLE IF NOT EXISTS Ouvidoriav2 (
    Cod INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    autor VARCHAR(255),
    respondente VARCHAR(255),
    tipo VARCHAR(50) NOT NULL,
    descri TEXT NOT NULL
);
2. Configuração da Conexão
Verifique o arquivo operacoesbd.py (ou onde a função criarConexao está localizada) e certifique-se de que as credenciais de conexão com o banco de dados (host, usuário, senha) estão corretas para o seu ambiente local.

3. Execução
Abra um terminal na pasta raiz do projeto e execute o arquivo principal:

Bash

python nome_do_seu_arquivo_principal.py

✒️ Autor:
Gutemberg






