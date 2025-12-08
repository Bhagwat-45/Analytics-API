from contextlib import asynccontextmanager
from fastapi import FastAPI
from api.events import router as event_router
from api.db.session import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()

    yield

app = FastAPI(
    title = "Analytics API",
    lifespan=lifespan
)

app.include_router(event_router)

@app.get("/",tags=["Root"])
async def root():
    return {
        "message" : "Hello World!!"
    }

@app.get("/healthz",tags=["Health"])
async def read_api_health():
    return {
        "status" : "ok"
    }
