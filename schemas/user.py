def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "binusianId": item["binusianId"],
        "name": item["name"],
        "email": item["email"],
        "major": item["major"],
        "batch": item["batch"]
    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]