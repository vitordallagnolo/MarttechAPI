def cadernoEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "descricao": item["descricao"],
        "anotacoes": item["anotacoes"],
    }


def cadernosEntity(entity) -> list:
    return [cadernoEntity(item) for item in entity]
