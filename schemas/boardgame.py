from pydantic import BaseModel, validator
from typing import Optional, List
from model.boardgame import Boardgame


class BoardgameSchema(BaseModel):
    """ Define como um novo jogo de tabuleiro a ser inserido deve ser representado.
    """
    name: str = "Azul"
    min_players: int = 2
    max_players: int = 4
    image_url: Optional[str] = None
    ludopedia_url: Optional[str] = None


class BoardgameUpdateSchema(BaseModel):
    """ Define como um jogo de tabuleiro pode ser atualizado (campos opcionais).
    """
    name: Optional[str] = None
    min_players: Optional[int] = None
    max_players: Optional[int] = None
    image_url: Optional[str] = None
    ludopedia_url: Optional[str] = None

    @validator("min_players", "max_players", "name", "image_url", "ludopedia_url", pre=True)
    @classmethod
    def empty_string_to_none(cls, v):
        if v == "":
            return None
        return v


class BoardgameViewSchema(BaseModel):
    """ Define como um jogo de tabuleiro será retornado.
    """
    id: int = 1
    name: str = "Azul"
    min_players: int = 2
    max_players: int = 4
    image_url: Optional[str] = None
    ludopedia_url: Optional[str] = None


def show_boardgame(boardgame: Boardgame) -> BoardgameViewSchema:
    """ Retorna uma representação do jogo de tabuleiro seguindo o schema definido em BoardgameViewSchema.
    """
    return {
        "id": boardgame.id,
        "name": boardgame.name,
        "min_players": boardgame.min_players,
        "max_players": boardgame.max_players,
        "image_url": boardgame.image_url,
        "ludopedia_url": boardgame.ludopedia_url
    }


class BoardgameListingSchema(BaseModel):
    """ Define como uma listagem de jogos de tabuleiro será retornada.
    """
    boardgames: List[BoardgameViewSchema]


def show_boardgames(boardgames: List[Boardgame]) -> BoardgameListingSchema:
    """ Retorna uma representação da listagem de jogos de tabuleiro seguindo o schema definido em BoardgameListingSchema.
    """
    result = []
    for boardgame in boardgames:
        result.append({
            "id": boardgame.id,
            "name": boardgame.name,
            "min_players": boardgame.min_players,
            "max_players": boardgame.max_players,
            "image_url": boardgame.image_url,
            "ludopedia_url": boardgame.ludopedia_url
        })

    return {"boardgames": result}


class BoardgameSearchSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca, que será feita com base no id do jogo de tabuleiro.
    """
    id: int = 1


class BoardgameDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    message: str
    name: str
    id: int
