import pytest
from sqlalchemy import delete
from src.db.connection import engine
from src.db.tables import clientes, webhooks


@pytest.fixture(autouse=True)
def clean_test_data():

    yield

    with engine.begin() as conn:

        conn.execute(
            delete(webhooks).where(
                webhooks.c.event_id.in_([
                    "evt_test"
                ])
            )
        )

        conn.execute(
            delete(clientes).where(
                clientes.c.cliente_email.in_([
                    "joao@teste.com"
                ])
            )
        )