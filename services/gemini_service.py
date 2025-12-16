import os
from google import genai
from dotenv import load_dotenv
from typing import List

load_dotenv()

class GeminiService:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise RuntimeError("GEMINI_API_KEY não encontrada no ambiente")

        self.client = genai.Client(api_key=api_key)

    def recommend_game(self, games: List[str], players: int, user_preferences: str = "") -> str:
        games_text = ", ".join(games)

        prompt = f"""
Você é um especialista em jogos de tabuleiro, capaz de recomendar jogos modernos e clássicos
com base na lista de jogos disponíveis:
{games_text}

Número de jogadores: {players}
Preferências do usuário: {user_preferences}

Ao receber uma solicitação, siga estas diretrizes:

Considere a lista de jogos existente como prioridade para as sugestões.
Sempre leve em conta a quantidade de jogadores informada, sugerindo apenas jogos compatíveis.
Considere também as preferências do usuário, como temas, nível de complexidade, duração ou estilo de jogo (ex: "jogo tranquilo", "jogo sobre plantas", etc).
Se nenhum jogo da lista atender à quantidade de jogadores ou às preferências, sugira um jogo alternativo fora da lista que atenda aos requisitos.
Para cada sugestão, explique brevemente por que o jogo é uma boa escolha para o usuário, relacionando com a quantidade de jogadores e as preferências informadas.
Seja claro, objetivo e mantenha um tom amigável.

Na primeira linha, traga o nome do jogo.
"""

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text.strip()