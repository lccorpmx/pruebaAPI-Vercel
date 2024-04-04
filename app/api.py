from fastapi import FastAPI

app = FastAPI()

@app.get("/", tags=["Root"])
async def hello():
    return {"te amo mi novia hermosa"}