from pydantic import BaseModel

class AIRecommendationSchema(BaseModel):
    players: int
    user_preferences: str = ""

    model_config = {
        "json_schema_extra": {
            "example": {
                "players": 2,
                "user_preferences": "jogo estratégico, tranquilo"
            }
        }
    }