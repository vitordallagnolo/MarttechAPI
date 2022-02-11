def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "nome": item["nome"],
        "email": item["email"],
        "password": item["password"]
    }


def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]