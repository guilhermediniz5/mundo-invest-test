from fastapi.testclient import TestClient
from sqlalchemy import select
from src.main import app
from src.db.connection import engine
from src.db.tables import clientes

client = TestClient(app)


def criar_cliente():
    payload = {
        "cliente_nome": "João Teste",
        "cliente_email": "joao@teste.com",
        "tipo_solicitacao": "Aguardando Análise",
        "valor_patrimonio": 300000
    }

    client.post("/clientes/", json=payload)


def test_webhook_prioridade_alta():

    criar_cliente()

    payload = {
        "event_id": "evt_test",
        "card_id": "123",
        "cliente_email": "joao@teste.com",
        "timestamp": "2025-01-01T10:00:00Z"
    }

    response = client.post(
        "/webhooks/pipefy/card-updated",
        json=payload
    )

    assert response.status_code == 200

    query = select(
        clientes.c.prioridade
    ).where(
        clientes.c.cliente_email == "joao@teste.com"
    )

    with engine.connect() as conn:
        result = conn.execute(query)
        cliente = result.fetchone()

    assert cliente.prioridade == "prioridade_alta"


def test_webhook_duplicado():

    criar_cliente()

    payload = {
        "event_id": "evt_test",
        "card_id": "123",
        "cliente_email": "joao@teste.com",
        "timestamp": "2025-01-01T10:00:00Z"
    }

    first = client.post(
        "/webhooks/pipefy/card-updated",
        json=payload
    )

    second = client.post(
        "/webhooks/pipefy/card-updated",
        json=payload
    )

    assert first.status_code == 200
    assert second.status_code == 200

    assert second.json() == {
        "error": "Evento já processado"
    }