import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy import MetaData

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("Banco de dados não encontrado!")

engine = create_engine(DATABASE_URL)

metadata = MetaData()