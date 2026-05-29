from fastapi.testclient import TestClient
from sqlalchemy import select
from src.main import app
from src.db.connection import engine
from src.db.tables import clientes

client = TestClient(app)

def test_create_cliente():
    payload = {
        "cliente_nome": "João Teste",
        "cliente_email": "joao@teste.com",
        "tipo_solicitacao": "Atualização cadastral",
        "valor_patrimonio": 300000
    }

    response = client.post("/clientes/", json=payload)

    assert response.status_code == 200

    query = select(clientes).where(
        clientes.c.cliente_email == "joao@teste.com"
    )

    with engine.connect() as conn:
        result = conn.execute(query)
        cliente = result.fetchone()

    assert cliente is not None
    assert cliente.cliente_nome == "João Teste"