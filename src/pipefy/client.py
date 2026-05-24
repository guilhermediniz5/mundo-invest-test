CREATE_CARD_MUTATION = """
mutation CreateCard($title: String!, $email: String!, $patrimonio: String!) {
  createCard(input: {
    pipe_id: 1
    title: $title
    fields_attributes: [
      { field_id: "email", field_value: $email }
      { field_id: "patrimonio", field_value: $patrimonio }
    ]
  }) {
    card {
      id
      title
    }
  }
}"""

def create_card(nome: str, email: str, patrimonio: float):
    payload = {
        "query": CREATE_CARD_MUTATION,
        "variables": {
            "title": nome,
            "email": email, 
            "patrimonio": str(patrimonio)
        }
    }
    
    print('Payload para Pipefy:', payload)

    return payload