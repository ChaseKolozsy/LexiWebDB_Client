import requests

BASE_URL = "http://localhost:5002/objects"

def get_objects_schema():
    response = requests.get(f"{BASE_URL}/schema")
    return response.json()

def get_all_objects():
    response = requests.get(BASE_URL)
    return response.json()

def get_object(object_id):
    response = requests.get(f"{BASE_URL}/{object_id}")
    return response.json()

def get_object_by_name(object_name):
    response = requests.get(f"{BASE_URL}/{object_name}")
    return response.json()

def create_object(name):
    data = {"name": name}
    response = requests.post(BASE_URL, json=data)
    return response.json()

def update_object(object_id, name):
    data = {"name": name}
    response = requests.put(f"{BASE_URL}/{object_id}", json=data)
    return response.json()

def delete_object(object_id):
    response = requests.delete(f"{BASE_URL}/{object_id}")
    return response.json()

def add_association(object_id, assoc_type, assoc_id):
    data = {"type": assoc_type, "id": assoc_id}
    response = requests.post(f"{BASE_URL}/{object_id}/add_association", json=data)
    return response.json()

def query_by_association(assoc_type, assoc_id):
    data = {"type": assoc_type, "id": assoc_id}
    response = requests.post(f"{BASE_URL}/query_by_association", json=data)
    return response.json()

def remove_association(object_id, assoc_type, assoc_id):
    data = {"type": assoc_type, "id": assoc_id}
    response = requests.post(f"{BASE_URL}/{object_id}/remove_association", json=data)
    return response.json()

if __name__ == "__main__":
    import app_ops
    import verb_ops
    app_ops.reset_db()

    # Example usage
    print("Schema:", get_objects_schema())
    
    
    new_obj = create_object("New Object")
    print("\n\nCreated Object:", new_obj)
    print("\nAll Objects:", get_all_objects())
    
    object_id = new_obj.get("object_id")
    print("\n\nObject ID:", object_id)
    if object_id:
        print("Get Object:", get_object(object_id))
        
        updated_obj = update_object(object_id, "Updated Object")
        print("\n\nUpdated Object:", updated_obj)
        
        print("\n\nGet Object by Name:", get_object_by_name("Updated Object"))
        
        new_verb = verb_ops.create_verb("New Verb")
        print("\n\nAdd Association:", add_association(object_id, "verb", new_verb.get("verb_id")))
        print("\nQuery by Association:", query_by_association("verb", new_verb.get("verb_id")))
        print("\nGet Objects by Verb:", verb_ops.get_objects_by_verb(new_verb.get("verb_id")))

        print("\n\nRemove Association:", remove_association(object_id, "verb", new_verb.get("verb_id")))
        print("\nQuery by Association:", query_by_association("verb", new_verb.get("verb_id")))
        print("\nGet Objects by Verb:", verb_ops.get_objects_by_verb(new_verb.get("verb_id")))

        print("\n\nDelete Object:", delete_object(object_id))
        print("\nAll Objects:", get_all_objects())
    