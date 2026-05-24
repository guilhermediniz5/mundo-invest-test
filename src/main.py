from fastapi import FastAPI
from src.db.connection import engine, metadata

app = FastAPI()

metadata.create_all(engine)