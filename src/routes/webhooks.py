from fastapi import APIRouter
from src.schemas import WebhookRequest
from src.services.webhooks import card_update

router = APIRouter(prefix="/webhooks", tags=["Webhooks"])

@router.post("/pipefy/card-updated")
def create_cliente(payload: WebhookRequest):
    return card_update(payload)