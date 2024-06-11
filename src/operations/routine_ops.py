import requests

BASE_URL = "http://localhost:5002/routines"

def get_routines_schema():
    response = requests.get(f"{BASE_URL}/schema")
    return response.json()

def get_all_routines():
    response = requests.get(BASE_URL)
    return response.json()

def get_routine(routine_id):
    response = requests.get(f"{BASE_URL}/{routine_id}")
    return response.json()

def get_routine_by_name(routine_name):
    response = requests.get(f"{BASE_URL}/{routine_name}")
    return response.json()

def create_routine(name, description):
    data = {
        "name": name,
        "description": description
    }
    response = requests.post(BASE_URL, json=data)
    return response.json()

def update_routine(routine_id, name, description):
    data = {
        "name": name,
        "description": description
    }
    response = requests.put(f"{BASE_URL}/{routine_id}", json=data)
    return response.json()

def delete_routine(routine_id):
    response = requests.delete(f"{BASE_URL}/{routine_id}")
    return response.json()

def get_objects_by_routine(routine_id):
    response = requests.get(f"{BASE_URL}/{routine_id}/objects")
    return response.json()

if __name__ == "__main__":
    import app_ops
    app_ops.reset_db()
    # Example usage
    print("Schema:", get_routines_schema())
    
    new_routine = create_routine("Morning Routine", "Wake up, exercise, breakfast")
    print("\n\nCreated Routine:", new_routine)
    print("\nAll Routines:", get_all_routines())
    
    routine_id = new_routine.get("routine_id")
    print("\n\nRoutine ID:", routine_id)
    if routine_id:
        print("\n\nGet Routine:", get_routine(routine_id))
        
        updated_routine = update_routine(routine_id, "Updated Morning Routine", "Wake up, exercise, breakfast, read")
        print("\n\nUpdated Routine:", updated_routine)
        print("\nAll Routines:", get_all_routines())
        
        print("\n\nGet Routine by Name:", get_routine_by_name("Updated Morning Routine"))

        print("\n\nDelete Routine:", delete_routine(routine_id))
        print("\nAll Routines:", get_all_routines())
    