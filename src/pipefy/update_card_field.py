UPDATE_CARD_FIELD = """
mutation UpdateCardField($card_id: ID!, $status: String!) {
    updateCardField(input: {
        card_id: $card_id
        field_id: "status"
        new_value: $status
    }) {
        success
    }
}"""

def update_card_field(card_id: int, status: str):
    payload = {
        "query": UPDATE_CARD_FIELD,
        "variables": {
            "card_id": card_id,
            "status": status
        }
    }
    
    print('Payload para Pipefy:', payload)