from pydantic import BaseModel,Field
from typing import List, Optional
"""
id 
path
description
"""

class EventCreateSchema(BaseModel):
    path: str

class EventUpdateSchema(BaseModel):
    description: str

class EventSchema(BaseModel):
    id: int = Field(gt = 0)



class EventListSchema(BaseModel):
    results: List[EventSchema]
    count: Optional[int]