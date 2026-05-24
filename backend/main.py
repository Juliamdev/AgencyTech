from fastapi import FastAPI

from app.routes.user_routes import router

from app.config.database import Base
from app.config.database import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"message": "API funcionando"}