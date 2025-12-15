# Jogos de Tabuleiro API

Este projeto é uma API para gerenciar informações sobre jogos de tabuleiro. Ele foi desenvolvido como parte do Projeto MVP do curso de Pós-graduação em Engenharia de Software da PUC-Rio, na Sprint de Desenvolvimento Fullstack Básico.

A API permite adicionar, visualizar, listar e remover jogos de tabuleiro de uma base de dados. Além disso, oferece documentação interativa para facilitar o uso.

---

## Índice

- [Funcionalidades](#funcionalidades)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Como executar](#como-executar)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Autora](#👩🏽‍💻-autora)

---

## Funcionalidades

- Adicionar novos jogos de tabuleiro.
- Buscar informações de um jogo específico pelo ID.
- Editar informações de um jogo existente.
- Listar todos os jogos cadastrados.
- Remover jogos da base de dados com base no ID.

---

## Pré-requisitos

Antes de começar, certifique-se de ter os seguintes itens instalados:

- Python 3.8 ou superior **(recomendado: Python 3.11)**
- [pip](https://pip.pypa.io/en/stable/)
- [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) (opcional, mas recomendado)

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

## Alguns comandos úteis do Docker

Para verificar se a imagem foi criada você pode executar o seguinte comando:

```bash
docker images
```

Caso queira remover uma imagem, basta executar o comando:

```bash
docker rmi <nome-da-imagem>
```
Substituindo `<nome-da-imagem>` pelo nome ou ID da imagem que deseja remover.

Para verificar se o container está em execução você pode executar o seguinte comando:

```bash
docker container ls --all
```

Caso queira parar um container, basta executar o comando:

```bash
docker stop <nome-ou-id-do-container>
```
Substituindo `<nome-ou-id-do-container>` pelo nome ou ID do container que deseja parar.

Caso queira destruir um container, basta executar o comando:

```bash
docker rm <nome-ou-id-do-container>
```

Para mais comandos, veja a [documentação oficial do Docker](https://docs.docker.com/reference/).

---

## Estrutura do Projeto

- **app.py**: Contém as rotas e lógica principal da API.
- **model/**: Define os modelos de dados e a estrutura do banco de dados.
- **schemas/**: Define os esquemas de validação e serialização dos dados.
- **requirements.txt**: Lista de dependências do projeto.

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
