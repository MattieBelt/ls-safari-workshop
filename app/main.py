from fastapi import FastAPI

from app.routers import items, users

app = FastAPI(title="ls-safari demo API")
app.include_router(items.router)
app.include_router(users.router)


@app.get("/")
def root():
    return {"message": "ls-safari demo API - see /docs"}
