from src.db.connection import engine
from src.db.tables import clientes, webhooks
from src.schemas import WebhookRequest
from src.pipefy.update_card_field import update_card_field
from sqlalchemy import select, update, insert

def card_update(payload: WebhookRequest):
    with engine.connect() as conn:
        evento_query = select(webhooks.c.id).where(
            webhooks.c.event_id == payload.event_id
        )
        
        evento = conn.execute(evento_query).fetchone()

        if evento:
            return {
                "error": "Evento já processado"
            }

        insert_evento_query = insert(webhooks).values(
            event_id=payload.event_id,
            card_id=payload.card_id,
            cliente_email=payload.cliente_email,
            timestamp=payload.timestamp
        )

        conn.execute(insert_evento_query)

        cliente_query = select(
            clientes.c.id,
            clientes.c.valor_patrimonio
        ).where(
            clientes.c.cliente_email == payload.cliente_email
        )

        cliente = conn.execute(cliente_query).fetchone()

        if not cliente:
            return {
                "error": "Cliente não encontrado"
            }

        if cliente.valor_patrimonio >= 200000: prioridade = "prioridade_alta"
        else: prioridade = "prioridade_normal"

        update_cliente_query = update(clientes).where(
            clientes.c.id == cliente.id
        ).values(
            status='Processado',
            prioridade=prioridade
        )

        update_card_field(
            card_id=payload.card_id,
            status='Processado'
        )

        conn.execute(update_cliente_query)
        conn.commit()

    return {
        "message": "Evento registrado com sucesso!"
    }