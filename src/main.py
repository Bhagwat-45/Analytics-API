from fastapi import FastAPI

app = FastAPI(
    title = "Analytics API"
)

@app.get("/")
async def root():
    return {
        "message" : "Hello World!!"
    }

