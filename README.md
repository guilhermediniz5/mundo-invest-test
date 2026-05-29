# Mundo Invest Test

API backend desenvolvida com FastAPI para cadastro de clientes e processamento de webhooks do Pipefy.

## Tecnologias Utilizadas

* Python 3.14
* FastAPI
* SQLAlchemy
* PostgreSQL
* Docker
* Pytest

---

# Como executar o projeto

## 1. Clonar o repositório

```bash
git clone https://github.com/guilhermediniz5/mundo-invest-test.git
cd mundo-invest-test
```

---

## 2. Criar ambiente virtual

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 4. Subir PostgreSQL com Docker

```bash
docker compose up -d
```

---

## 5. Configurar variáveis de ambiente

Criar arquivo `.env`:

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/mundoinvest
```

---

## 6. Executar aplicação

```bash
uvicorn src.main:app --reload
```

Aplicação disponível em:

```txt
http://127.0.0.1:8000
```

---

# Executar Testes

```bash
pytest
```

---

# Endpoints

## Criar Cliente

### Endpoint

```http
POST /clientes
```

### Exemplo curl

```bash
curl -X POST "http://127.0.0.1:8000/clientes/" ^
-H "Content-Type: application/json" ^
-d "{\"cliente_nome\":\"João Teste\",\"cliente_email\":\"joao@teste.com\",\"tipo_solicitacao\":\"Aguardando Análise\",\"valor_patrimonio\":300000}"
```

### Payload

```json
{
  "cliente_nome": "João Teste",
  "cliente_email": "joao@teste.com",
  "tipo_solicitacao": "Aguardando Análise",
  "valor_patrimonio": 300000
}
```

---

## Processar Webhook Pipefy

### Endpoint

```http
POST /webhooks/pipefy/card-updated
```

### Exemplo curl

```bash
curl -X POST "http://127.0.0.1:8000/webhooks/pipefy/card-updated" ^
-H "Content-Type: application/json" ^
-d "{\"event_id\":\"evt_test\",\"card_id\":\"123\",\"cliente_email\":\"joao@teste.com\",\"timestamp\":\"2025-01-01T10:00:00Z\"}"
```

### Payload

```json
{
  "event_id": "evt_test",
  "card_id": "123",
  "cliente_email": "joao@teste.com",
  "timestamp": "2025-01-01T10:00:00Z"
}
```

---

# Visão de Produção (AWS)

Em ambiente de produção na AWS, essa arquitetura poderia escalar utilizando:

## API Gateway

Responsável pela exposição segura dos endpoints HTTP.

## AWS Lambda

Executaria:

* criação de clientes;
* processamento de webhooks;
* integração com Pipefy.

Permitindo escalabilidade automática baseada em volume de requisições.

## RDS PostgreSQL

Responsável pela persistência relacional dos dados de clientes e eventos processados.

## DynamoDB

Poderia ser utilizado especificamente para controle de idempotência dos webhooks, devido à baixa latência e alta escalabilidade.

## SQS

Poderia desacoplar o recebimento do webhook do processamento de negócio, evitando perda de eventos em picos de carga.

Fluxo recomendado:

```txt
Pipefy -> API Gateway -> Lambda -> SQS -> Worker Lambda -> Banco de Dados
```
