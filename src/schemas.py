from pydantic import BaseModel, EmailStr
from datetime import datetime

class ClienteCreate(BaseModel):
    cliente_nome: str
    cliente_email: EmailStr
    tipo_solicitacao: str
    valor_patrimonio: float

class WebhookRequest(BaseModel):
    event_id: str
    card_id: str
    cliente_email: EmailStr
    timestamp: datetime