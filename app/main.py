from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.routes.students import router as students_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="MVP API",
    description="API REST do projeto MVP",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(students_router)

@app.get("/")
def root():
    return {
        "message": "MVP API funcionando!"
    }