from fastapi import FastAPI
from src.db.connection import engine, metadata
import src.db.tables
from src.routes.clientes import router as clientes_router
from src.routes.webhooks import router as webhooks_router

app = FastAPI()
metadata.create_all(engine)

app.include_router(clientes_router)
app.include_router(webhooks_router)