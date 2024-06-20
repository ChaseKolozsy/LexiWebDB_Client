import requests

BASE_URL = "http://localhost:5002/api/attributes"

def get_attributes_schema():
    response = requests.get(f"{BASE_URL}/schema")
    return response

def get_all_attributes():
    response = requests.get(BASE_URL)
    return response

def get_attribute(attribute_id):
    response = requests.get(f"{BASE_URL}/{attribute_id}")
    return response

def get_attribute_by_name(attribute_name):
    response = requests.get(f"{BASE_URL}/{attribute_name}")
    return response

def create_attribute(name):
    data = {"name": name}
    response = requests.post(BASE_URL, json=data)
    return response

def update_attribute(attribute_id, name):
    data = {"name": name}
    response = requests.put(f"{BASE_URL}/{attribute_id}", json=data)
    return response

def delete_attribute(attribute_id):
    response = requests.delete(f"{BASE_URL}/{attribute_id}")
    return response

def get_objects_by_attribute(attribute_id):
    response = requests.get(f"{BASE_URL}/{attribute_id}/objects")
    return response

if __name__ == "__main__":
    pass
    
    