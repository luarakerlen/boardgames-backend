from pydantic import BaseModel

class BoardgameRecommendationResponse(BaseModel):
    players: int
    recommendation: str