from fastapi import APIRouter
from .schema import EventSchema


router = APIRouter(
    prefix='/api/events',
    tags=["API-Events"]
)

@router.get("/")
def read_events():
    return {
        "items" : [1,2,3]
    }

@router.get("/{event_id}",response_model=EventSchema)
def get_event(event_id: int):
    return EventSchema(id = event_id)