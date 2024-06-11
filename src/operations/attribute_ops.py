import requests

BASE_URL = "http://localhost:5002/attributes"

def get_attributes_schema():
    response = requests.get(f"{BASE_URL}/schema")
    return response.json()

def get_all_attributes():
    response = requests.get(BASE_URL)
    return response.json()

def get_attribute(attribute_id):
    response = requests.get(f"{BASE_URL}/{attribute_id}")
    return response.json()

def get_attribute_by_name(attribute_name):
    response = requests.get(f"{BASE_URL}/{attribute_name}")
    return response.json()

def create_attribute(name):
    data = {"name": name}
    response = requests.post(BASE_URL, json=data)
    return response.json()

def update_attribute(attribute_id, name):
    data = {"name": name}
    response = requests.put(f"{BASE_URL}/{attribute_id}", json=data)
    return response.json()

def delete_attribute(attribute_id):
    response = requests.delete(f"{BASE_URL}/{attribute_id}")
    return response.json()

if __name__ == "__main__":
    # Example usage
    print("Schema:", get_attributes_schema())
    
    print("All Attributes:", get_all_attributes())
    
    new_attr = create_attribute("New Attribute")
    print("Created Attribute:", new_attr)
    
    attr_id = new_attr.get("id")
    if attr_id:
        print("Get Attribute:", get_attribute(attr_id))
        
        updated_attr = update_attribute(attr_id, "Updated Attribute")
        print("Updated Attribute:", updated_attr)
        
        print("Delete Attribute:", delete_attribute(attr_id))
    
    print("Get Attribute by Name:", get_attribute_by_name("Updated Attribute"))