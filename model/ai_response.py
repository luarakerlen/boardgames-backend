from pydantic import BaseModel

class BoardgameRecommendationResponse(BaseModel):
    name: str
    explanation: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Azul",
                "explanation": "Azul é uma excelente escolha para 2 jogadores por oferecer decisões táticas diretas, alta interação e regras simples com profundidade estratégica."
            }
        }
    }