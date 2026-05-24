from fastapi import HTTPException
from src.db.connection import engine
from src.db.tables import clientes
from src.schemas import ClienteCreate
from src.pipefy.client import create_card
from sqlalchemy import insert
from sqlalchemy.exc import IntegrityError

def cliente_create(payload: ClienteCreate):
    try:
        query = insert(clientes).values(
            cliente_nome=payload.cliente_nome,
            cliente_email=payload.cliente_email,
            tipo_solicitacao=payload.tipo_solicitacao,
            valor_patrimonio=payload.valor_patrimonio,
        ).returning(clientes)

        with engine.connect() as conn:
            result = conn.execute(query)
            conn.commit()
            cliente = result.fetchone()

        create_card(
            nome=payload.cliente_nome,
            email=payload.cliente_email,
            patrimonio=payload.valor_patrimonio
        )

        return {
            "cliente_nome": payload.cliente_nome,
            "cliente_email": payload.cliente_email,
            "tipo_solicitacao": payload.tipo_solicitacao,
            "valor_patrimonio": payload.valor_patrimonio,
            "status": "Aguardando Análise"
        }
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Email já cadastrado")