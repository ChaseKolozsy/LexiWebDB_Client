import requests

BASE_URL = "http://localhost:5002/verbs"

def get_verbs_schema():
    response = requests.get(f"{BASE_URL}/schema")
    return response.json()

def get_all_verbs():
    response = requests.get(BASE_URL)
    return response.json()

def get_verb(verb_id):
    response = requests.get(f"{BASE_URL}/{verb_id}")
    return response.json()

def get_verb_by_name(verb_name):
    response = requests.get(f"{BASE_URL}/{verb_name}")
    return response.json()

def create_verb(name):
    data = {"name": name}
    response = requests.post(BASE_URL, json=data)
    return response.json()

def update_verb(verb_id, name):
    data = {"name": name}
    response = requests.put(f"{BASE_URL}/{verb_id}", json=data)
    return response.json()

def delete_verb(verb_id):
    response = requests.delete(f"{BASE_URL}/{verb_id}")
    return response.json()

if __name__ == "__main__":
    # Example usage
    print("Schema:", get_verbs_schema())
    
    print("All Verbs:", get_all_verbs())
    
    new_verb = create_verb("New Verb")
    print("Created Verb:", new_verb)
    
    verb_id = new_verb.get("id")
    if verb_id:
        print("Get Verb:", get_verb(verb_id))
        
        updated_verb = update_verb(verb_id, "Updated Verb")
        print("Updated Verb:", updated_verb)
        
        print("Delete Verb:", delete_verb(verb_id))
    
    print("Get Verb by Name:", get_verb_by_name("Updated Verb"))