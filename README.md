# Jogos de Tabuleiro API

Este projeto é uma API para gerenciar informações sobre jogos de tabuleiro. Ele foi desenvolvido como parte do Projeto MVP do curso de Pós-graduação em Engenharia de Software da PUC-Rio, na Sprint de Desenvolvimento Fullstack Básico e, posteriormente, foram adicionadas novas funcionalidades para a Sprint de Arquitetura de Software.

A API permite adicionar, visualizar, editar, listar e remover jogos de tabuleiro de uma base de dados. Além disso, oferece documentação interativa para facilitar o uso.

A API também faz integração com uma API externa, a API do Gemini, para trazer recomendações de jogos para o usuário, utilizando a lista de jogos disponíveis no banco de dados.

---

## Índice

- [Funcionalidades](#funcionalidades)
- [Pré-requisitos](#pré-requisitos)
- [Variáveis de Ambiente](#variáveis-de-ambiente)
- [Configuração inicial](#configuração-inicial)
- [Instalação](#instalação)
- [Como executar](#como-executar)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Arquitetura da Solução](#arquitetura-da-solução)
- [Autora](#👩🏽‍💻-autora)

---

## Funcionalidades

- Adicionar novos jogos de tabuleiro.
- Buscar informações de um jogo específico pelo ID.
- Listar todos os jogos cadastrados.
- Remover jogos da base de dados com base no ID.

### Funcionalidades adicionadas na Sprint de Arquitetura de Software
- Editar informações de um jogo existente.
- Gerar recomendações de jogos de tabuleiro com auxílio de IA, considerando a quantidade de jogadores e preferências do usuário.
- Priorizar recomendações com base nos jogos cadastrados na base de dados.
- Expor endpoint específico para recomendação inteligente de jogos.

---

## Pré-requisitos

Antes de começar, certifique-se de ter os seguintes itens instalados:

- Python 3.8 ou superior **(recomendado: Python 3.11)**
- [pip](https://pip.pypa.io/en/stable/)
- [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) (opcional, mas recomendado)

---

## Variáveis de Ambiente

Este projeto utiliza variáveis de ambiente para integração com serviços externos de IA.

Crie um arquivo chamado `.env` na raiz do projeto com o seguinte conteúdo:

```
GEMINI_API_KEY=coloque_sua_chave_aqui
```

**Importante:**
- Nunca versione sua chave real.
- O arquivo `.env` deve ser incluído no `.gitignore`.
- Para fins de documentação, este repositório inclui apenas as instruções de criação do arquivo, não o valor real da chave.

---

## Configuração inicial

Após clonar o projeto e instalar as dependências, configure as variáveis de ambiente conforme descrito na seção **Variáveis de Ambiente** antes de executar a aplicação.

---

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/luarakerlen/boardgames-backend.git
   cd boardgames-backend
   ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências do projeto:

   ```bash
   pip install -r requirements.txt
   ```

---

## Como executar

1. Certifique-se de estar no diretório raiz do projeto: `/boardgames-backend`.

2. Execute o servidor Flask:

   ```bash
   flask run --host 0.0.0.0 --port 5001
   ```

3. Para desenvolvimento, utilize o parâmetro `--reload` para reiniciar automaticamente o servidor ao alterar o código:

   ```bash
   flask run --host 0.0.0.0 --port 5001 --reload
   ```

4. Acesse a API no navegador ou em ferramentas como Postman:

   - Documentação interativa: [http://localhost:5001/openapi](http://localhost:5001/openapi)
   - Status da API: [http://localhost:5001/#/](http://localhost:5001/#/)

---

## Como executar através do Docker

Certifique-se de ter o [Docker](https://docs.docker.com/engine/install/) instalado e em execução em sua máquina.

Navegue até o diretório que contém o Dockerfile e o requirements.txt no terminal. Execute como administrador o seguinte comando para construir a imagem Docker:

```bash
docker build -t boardgames-api .
```

Após construir a imagem, execute o container com o seguinte comando:

```bash
docker run -p 5001:5001 boardgames-api
```

A API estará disponível em `http://localhost:5001`.

---

## Estrutura do Projeto

- **app.py**: Contém as rotas e lógica principal da API.
- **model/**: Define os modelos de dados e a estrutura do banco de dados.
- **schemas/**: Define os esquemas de validação e serialização dos dados.
- **requirements.txt**: Lista de dependências do projeto.
- **services/**: Camada de serviços externos, incluindo integração com IA (Gemini).

---

## Arquitetura da Solução

Este projeto segue o Cenário 1.1 de Arquitetura, onde:

- O frontend se comunica com um backend próprio;

- O backend é responsável por:

  - Persistência dos dados em banco de dados

  - Comunicação com uma API externa de IA para geração de recomendações

### Diagrama da Arquitetura

> Cenário 1.1 – Frontend conectado ao backend, que por sua vez integra com uma API externa e um banco de dados.

Imagem do modelo arquitetural:

![Diagrama de Arquitetura – Cenário 1.1](./arquitetura-cenario-1-1.png)

---

## 👩🏽‍💻 Autora

<a href="https://www.linkedin.com/in/luarakerlen/" target="_blank">
 <img title="Luara Kerlen" style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/26902816?v=4" width="100px;" alt="Foto da Luara"/>
 </a>

Feito com ❤️ por <a href="https://www.linkedin.com/in/luarakerlen/" target="_blank"><b>Luara Kerlen</b></a> <a href="https://www.linkedin.com/in/luarakerlen/" title="Luara Kerlen"></a>
<br>Entre em contato!

[![Linkedin Badge](https://img.shields.io/badge/-Luara%20Kerlen-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/luarakerlen/)](https://www.linkedin.com/in/luarakerlen/)
[![Gmail Badge](https://img.shields.io/badge/-luarakerlen12@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:luarakerlen12@gmail.com)](mailto:luarakerlen12@gmail.com)
[![Instagram Badge](https://img.shields.io/badge/Luara%20Kerlen-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/luarakerlen)
