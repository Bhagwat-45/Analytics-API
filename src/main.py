from fastapi import FastAPI
from api.events import router as event_router
app = FastAPI(
    title = "Analytics API"
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
