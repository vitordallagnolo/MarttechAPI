from beanie import PydanticObjectId


def anotacaoEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "titulo": item["titulo"],
        "data_criacao": item["data_criacao"],
        "data_modificacao": item["data_modificacao"],
        "texto": item["texto"],
        "tags": item["tags"],
        "caderno": item["caderno"]
    }


def anotacoesEntity(entity) -> list:
    return [anotacaoEntity(item) for item in entity]
