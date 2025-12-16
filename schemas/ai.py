from pydantic import BaseModel

class AIRecommendationSchema(BaseModel):
    players: int
    user_preferences: str = ""