from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from model import Base


class Boardgame(Base):
    __tablename__ = 'boardgames'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    min_players = Column(Integer, nullable=False)
    max_players = Column(Integer, nullable=False)
    image_url = Column(String(255), nullable=True)
    ludopedia_url = Column(String(255), nullable=True)

    def __init__(self, name: str, min_players: int, max_players: int, image_url: Union[str, None], ludopedia_url: Union[str, None]):
        """ Cria um novo objeto Boardgame.
        Esta classe representa um jogo de tabuleiro e suas informações.
        
        Atributos:
            id (int): ID do jogo de tabuleiro.
            name (str): Nome do jogo de tabuleiro.
            min_players (int): Número mínimo de jogadores.
            max_players (int): Número máximo de jogadores.
            image_url (str): URL da imagem do jogo de tabuleiro.
            ludopedia_url (str): URL do jogo na Ludopedia.
        """
        self.name = name
        self.min_players = min_players
        self.max_players = max_players
        self.image_url = image_url
        self.ludopedia_url = ludopedia_url
