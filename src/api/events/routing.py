from typing import List
from fastapi import APIRouter
from .schema import EventListSchema, EventSchema, EventCreateSchema

router = APIRouter(
    prefix='/api/events',
    tags=["API-Events"]
)

@router.get("/",response_model=EventListSchema)
def read_events():
    return EventListSchema.results

@router.get("/{event_id}",response_model=EventSchema)
def get_event(event_id: int):
    return EventSchema(id = event_id)

@router.post("/",response_model=EventSchema)
def create_events(payload: EventCreateSchema):
    return EventSchema(id = 123)