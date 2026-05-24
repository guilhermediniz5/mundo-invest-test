from sqlalchemy import Table, Column, Integer, String, Numeric
from .connection import metadata

clientes = Table(
    "clientes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("cliente_nome", String, nullable=False),
    Column("cliente_email", String, unique=True, nullable=False),
    Column("tipo_solicitacao", String, nullable=False),
    Column("valor_patrimonio", Numeric(15, 2), nullable=False),
    Column("status", String, default="Aguardando Análise", nullable=False),
)