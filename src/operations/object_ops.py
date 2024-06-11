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

if __name__ == "__main__":
    # Example usage
    print("Schema:", get_objects_schema())
    
    print("All Objects:", get_all_objects())
    
    new_obj = create_object("New Object")
    print("Created Object:", new_obj)
    
    obj_id = new_obj.get("id")
    if obj_id:
        print("Get Object:", get_object(obj_id))
        
        updated_obj = update_object(obj_id, "Updated Object")
        print("Updated Object:", updated_obj)
        
        print("Delete Object:", delete_object(obj_id))
    
    print("Get Object by Name:", get_object_by_name("Updated Object"))
    
    if obj_id:
        print("Add Association:", add_association(obj_id, "verb", 1))