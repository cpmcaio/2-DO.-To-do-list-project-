# Projeto To-Do List (Full-Stack)

Este repositório contém o código completo para uma aplicação de lista de tarefas, incluindo o back-end (API) desenvolvido com FastAPI e o front-end desenvolvido com HTML, CSS e JavaScript puros.

## Visão Geral da Arquitetura

O projeto é dividido em duas partes principais:

1.  **`api_todolist_simples/`**: Contém a API RESTful construída com Python e FastAPI. É responsável por toda a lógica de negócios, interações com o banco de dados e por servir os dados.
2.  **`frontend_todolist/`**: Contém a interface do usuário construída com tecnologias web padrão. É responsável pela apresentação dos dados e pela interação com o usuário, consumindo a API do back-end.

---

## Tecnologias Utilizadas

### Back-end (API)
* Python 3.13
* FastAPI
* SQLAlchemy
* Uvicorn
* SQLite

### Front-end (UI)
* HTML5
* CSS3
* JavaScript (ES6+)
* Fetch API

---

## Como Rodar o Projeto Completo

Para executar a aplicação, você precisará iniciar o servidor do back-end e o servidor do front-end separadamente.

### 1. Configurando e Rodando o Back-end

**Pré-requisito:** Ter o Python 3 instalado.

1.  **Navegue até a pasta do back-end:**
    ```bash
    cd api_todolist_simples
    ```

2.  **Crie e ative um ambiente virtual:**
    * No Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\Activate.ps1
        ```
        *(Pode ser necessário ajustar a política de execução no PowerShell com `Set-ExecutionPolicy RemoteSigned -Scope Process`)*
    * No macOS/Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Instale as dependências necessárias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Inicie o servidor da API:**
    ```bash
    uvicorn app.main:app --reload
    ```

✅ **Sucesso!** O servidor do back-end agora está rodando em `http://127.0.0.1:8000`. Deixe este terminal aberto.

### 2. Configurando e Rodando o Front-end

**Pré-requisito:** Ter um navegador web e, idealmente, a extensão "Live Server" no Visual Studio Code para a melhor experiência.

1.  **Abra uma nova janela de terminal.**

2.  **Navegue até a pasta do front-end:**
    ```bash
    cd frontend_todolist
    ```

3.  **Inicie o servidor local:**
    * **Método Recomendado (com VS Code):**
        1.  Abra a pasta `frontend_todolist` no VS Code.
        2.  Clique com o botão direito no arquivo `index.html`.
        3.  Selecione **"Open with Live Server"**.

    * **Método Alternativo (com Python):**
        Se você não tiver a extensão Live Server, pode usar o Python para criar um servidor simples:
        ```bash
        python -m http.server
        ```
        Neste caso, acesse `http://localhost:8000` no seu navegador (pode haver um conflito de porta se o back-end também estiver na porta 8000; o Live Server gerencia isso melhor, geralmente usando a porta 5500).

✅ **Pronto!** Seu navegador abrirá a aplicação de To-Do List, que se comunicará automaticamente com o back-end. Agora você pode adicionar, visualizar, atualizar e deletar tarefas.

---

## Estrutura da API (Endpoints)

A API fornece os seguintes endpoints:

| Método | URL                  | Descrição                                  |
|--------|----------------------|--------------------------------------------|
| `POST` | `/tarefas/`          | Cria uma nova tarefa.                      |
| `GET`  | `/tarefas/`          | Lista todas as tarefas existentes.         |
| `GET`  | `/tarefas/{id}`      | Obtém os detalhes de uma única tarefa.     |
| `PUT`  | `/tarefas/{id}`      | Atualiza uma tarefa existente.             |
| `DELETE`| `/tarefas/{id}`     | Deleta uma tarefa.                         |

A documentação interativa completa da API (Swagger UI) pode ser acessada em `http://127.0.0.1:8000/docs` enquanto o servidor do back-end estiver rodando.
