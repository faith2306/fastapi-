def projectEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "user": item["user"],
        "title": item["title"],
        "description": item["description"],
        "team": item["team"]        
    }

def projectsEntity(entity) -> list:
    return [projectEntity(item) for item in entity]