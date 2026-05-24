from fastapi import APIRouter
from src.schemas import ClienteCreate
from src.services.clientes import cliente_create

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.post("/")
def create_cliente(payload: ClienteCreate):
    return cliente_create(payload)