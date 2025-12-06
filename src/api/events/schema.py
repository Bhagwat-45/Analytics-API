from pydantic import BaseModel,Field

class EventSchema(BaseModel):
    id: int = Field(gt = 0)



