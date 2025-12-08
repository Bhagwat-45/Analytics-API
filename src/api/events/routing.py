from typing import List
from fastapi import APIRouter, Depends, HTTPException,status
from .models import EventListSchema, EventModel, EventCreateSchema, EventUpdateSchema, get_utc_now
from ..db.config import DATABASE_URL
from api.db.session import get_session
from sqlmodel import Session, select

router = APIRouter(
    prefix='/api/events',
    tags=["API-Events"]
)

@router.get("/", response_model=EventListSchema)
def read_events(session: Session = Depends(get_session)):
    query = select(EventModel).order_by(EventModel.id).limit(10)
    result = session.exec(query).all()

    return {
        "results": result,
        "count": len(result)
    }

@router.post("/",response_model=EventModel)
def create_events(payload: EventCreateSchema,session: Session = Depends(get_session)):
    data = payload.model_dump()
    obj = EventModel.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj

@router.get("/{event_id}",response_model=EventModel)
def get_event(event_id: int, session : Session = Depends(get_session)):
    query = select(EventModel).where(EventModel.id == event_id)
    result = session.exec(query).first()
    if not result: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detial = f"The event with {event_id} was not found!")
    return result

@router.put("/{event_id}", response_model=EventModel)
def update_event(event_id: int,payload: EventUpdateSchema, session : Session = Depends(get_session)):
    query = select(EventModel).where(EventModel.id == event_id)
    obj = session.exec(query).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The event with {event_id} was not found!")
    
    data = payload.model_dump()

    for k,v in data.items():
        if k == 'id':
            continue
        setattr(obj,k,v)
    
    obj.updated_at = get_utc_now()

    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj

@router.delete("/{event_id}",response_model=EventModel)
def delete_event(event_id: int, session: Session = Depends(get_session)):
    query = select(EventModel).where(EventModel.id == event_id)
    obj = session.exec(query).first()

    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The event with {event_id} was not found!")
    
    session.delete(obj)
    session.commit()