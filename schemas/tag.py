def tagEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "nome": item["nome"],
        "descricao": item["descricao"],
    }


def tagsEntity(entity) -> list:
    return [tagEntity(item) for item in entity]
