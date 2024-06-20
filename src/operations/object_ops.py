import requests

BASE_URL = "http://localhost:5002/api/objects"

def get_objects_schema():
    response = requests.get(f"{BASE_URL}/schema")
    return response

def get_all_objects():
    response = requests.get(BASE_URL)
    return response

def get_object(object_id):
    response = requests.get(f"{BASE_URL}/{object_id}")
    return response

def get_object_by_name(object_name):
    response = requests.get(f"{BASE_URL}/{object_name}")
    return response

def create_object(name):
    data = {"name": name}
    response = requests.post(BASE_URL, json=data)
    return response

def update_object(object_id, name):
    data = {"name": name}
    response = requests.put(f"{BASE_URL}/{object_id}", json=data)
    return response

def delete_object(object_id):
    response = requests.delete(f"{BASE_URL}/{object_id}")
    return response

def add_association(object_id, assoc_type, assoc_id):
    data = {"type": assoc_type, "id": assoc_id}
    response = requests.post(f"{BASE_URL}/{object_id}/add_association", json=data)
    return response

def query_by_association(assoc_type, assoc_id):
    data = {"type": assoc_type, "id": assoc_id}
    response = requests.post(f"{BASE_URL}/query_by_association", json=data)
    return response

def remove_association(object_id, assoc_type, assoc_id):
    data = {"type": assoc_type, "id": assoc_id}
    response = requests.post(f"{BASE_URL}/{object_id}/remove_association", json=data)
    return response

if __name__ == "__main__":
    pass