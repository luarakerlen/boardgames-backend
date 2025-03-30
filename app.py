from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Boardgame
from schemas import *
from logger import logger
from flask_cors import CORS

info = Info(title="Jogos de tabuleiro API", version="0.0.1")
app = OpenAPI(__name__, info=info)
CORS(app)

# DEFINIÇÃO DE TAGS
home_tag = Tag(name="Documentação",
               description="Seleção de documentação: Swagger, Redoc ou RapiDoc.")
boardgame_tag = Tag(name="Jogos de Tabuleiro",
                    description="Adição, visualização e remoção de jogos de tabuleiro na base de dados.")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/boardgame', tags=[boardgame_tag],
          responses={"200": BoardgameViewSchema, "409": ErrorSchema, "400": ErrorSchema, "500": ErrorSchema})
def add_boardgame(form: BoardgameSchema):
    """ Adiciona um jogo de tabuleiro na base de dados.
    Retorna uma representação do jogo de tabuleiro adicionado.
    """
    boardgame = Boardgame(
        name=form.name,
        min_players=form.min_players,
        max_players=form.max_players,
        image_url=form.image_url,
        description=form.description,
        ludopedia_url=form.ludopedia_url
    )
    logger.debug(
        f"Adicionando o jogo de tabuleiro {boardgame.name} na base de dados.")

    try:
        session = Session()
        session.add(boardgame)
        session.commit()
        logger.debug(
            f"Jogo de tabuleiro {boardgame.name} adicionado com sucesso.")
        return show_boardgame(boardgame)

    except IntegrityError as e:
        error_message = f"O jogo de tabuleiro {boardgame.name} já existe na base de dados."
        logger.warning(
            f"Erro ao adicionar o jogo de tabuleiro {boardgame.name} na base de dados: {error_message}")
        return {"message": error_message}, 409

    except Exception as e:
        error_message = f"Erro ao adicionar o jogo de tabuleiro {boardgame.name} na base de dados: {str(e)}"
        logger.warning(
            f"Erro ao adicionar o jogo de tabuleiro {boardgame.name} na base de dados: {str(e)}")
        return {"message": error_message}, 500


@app.get('/boardgame', tags=[boardgame_tag],
         responses={"200": BoardgameViewSchema, "404": ErrorSchema})
def get_boardgame(query: BoardgameSearchSchema):
    """ Faz a busca de um jogo de tabuleiro a partir do id do jogo.
    Retorna uma representação do jogo de tabuleiro encontrado.
    """
    id = query.id
    logger.debug(
        f"Buscando o jogo de tabuleiro com id {id} na base de dados.")

    session = Session()
    boardgame = session.query(Boardgame).filter(Boardgame.id == id).first()
    if not boardgame:
        error_message = f"Jogo de tabuleiro com id {id} não encontrado na base de dados."
        logger.warning(
            f"Erro ao buscar o jogo de tabuleiro com id {id} na base de dados: {error_message}")
        return {"message": error_message}, 404
    else:
        logger.debug(
            f"Jogo de tabuleiro com id {id} encontrado na base de dados.")
        return show_boardgame(boardgame)


@app.get('/boardgames', tags=[boardgame_tag],
         responses={"200": BoardgameListingSchema, "404": ErrorSchema})
def get_boardgames():
    """ Faz a busca de todos os jogos de tabuleiro na base de dados.
    Retorna uma representação da listagem de jogos de tabuleiro encontrados.
    """
    logger.debug(
        f"Buscando todos os jogos de tabuleiro na base de dados.")

    session = Session()
    boardgames = session.query(Boardgame).all()

    if not boardgames:
        logger.debug("Nenhum jogo de tabuleiro encontrado na base de dados.")
        return {"boardgames": []}, 200
    else:
        logger.debug(
            f"{len(boardgames)} jogos de tabuleiro encontrados na base de dados.")
        return show_boardgames(boardgames), 200


@app.delete('/boardgame', tags=[boardgame_tag],
            responses={"200": ProdutoDelSchema, "404": ErrorSchema})
def delete_boardgame(query: BoardgameSearchSchema):
    """ Faz a remoção de um jogo de tabuleiro a partir do id do jogo.
    Retorna uma mensagem de confirmação da remoção.
    """
    id = query.id
    logger.debug(
        f"Removendo o jogo de tabuleiro com id {id} na base de dados.")

    session = Session()
    boardgame = session.query(Boardgame).filter(Boardgame.id == id).first()

    if not boardgame:
        error_message = f"Jogo de tabuleiro com id {id} não encontrado na base de dados."
        logger.warning(
            f"Erro ao remover o jogo de tabuleiro com id {id} na base de dados: {error_message}")
        return {"message": error_message}, 404
    else:
        name = boardgame.name
        session.delete(boardgame)
        session.commit()
        logger.debug(
            f"Jogo de tabuleiro com id {id} removido da base de dados.")
        return {"message": f"Jogo de tabuleiro com id {id} removido da base de dados.", "id": id, "name": name}, 200
