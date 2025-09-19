# Sistema de Ouvidoria
_Projeto desenvolvido para a disciplina de Programação em Linguagem Estruturada._

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)
![Período](https://img.shields.io/badge/Período-2025.1-informational?style=for-the-badge)

Um sistema de ouvidoria simples, baseado em linha de comando (CLI), que permite aos usuários gerenciar manifestações como reclamações, sugestões e elogios. Este projeto foi desenvolvido como requisito avaliativo na cadeira de Programação em Linguagem Estruturada, ministrada pelo Professor Daniel Abella, durante o período letivo de 2025.1.

O sistema interage com um banco de dados MySQL para garantir a persistência dos dados, permitindo que as operações sejam salvas e consultadas a qualquer momento.

## ✨ Funcionalidades

O sistema oferece um menu interativo com as seguintes operações CRUD (Create, Read, Delete):

-   **Listar todas as manifestações:** Exibe um resumo de todas as manifestações cadastradas no banco de dados.
-   **Adicionar uma nova manifestação:** Permite ao usuário registrar um novo evento, escolhende entre os tipos "Reclamação", "Elogio" ou "Sugestão".
-   **Buscar uma manifestação específica:** Procura e exibe os detalhes completos de uma manifestação a partir de seu código único.
-   **Remover uma manifestação:** Exclui um registro do sistema utilizando seu código como identificador.
-   **Exibir a contagem total:** Mostra o número total de manifestações atualmente registradas.

## 💻 Tecnologias Utilizadas

-   **Linguagem de Programação:** Python
-   **Banco de Dados:** MySQL
-   **Interface:** Terminal / Linha de Comando (CLI)
-   **Biblioteca de Conexão:** `mysql-connector-python`

## 🚀 Como Executar o Projeto

Para executar este projeto em sua máquina local, siga os passos abaixo.

### Pré-requisitos

-   Python 3.x instalado.
-   Servidor de banco de dados MySQL ativo.
-   A biblioteca Python para conectar ao MySQL.

    > **Atenção:** É crucial utilizar a versão `8.3.0` do conector para garantir a compatibilidade do projeto. Se você tiver uma versão mais recente instalada, é necessário fazer o downgrade.

    Use o pip para instalar a versão correta:
    ```sh
    pip install mysql-connector-python==8.3.0
    ```

### 1. Configuração do Banco de Dados

Antes de executar o código, você precisa criar o banco de dados e a tabela que o sistema utilizará. Execute os seguintes comandos SQL no seu cliente MySQL:

```sql
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
