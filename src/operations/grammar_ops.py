import requests

BASE_URL = "http://localhost:5002/grammar_points"

def get_grammar_points_schema():
    response = requests.get(f"{BASE_URL}/schema")
    return response.json()

def get_all_grammar_points():
    response = requests.get(BASE_URL)
    return response.json()

def get_grammar_point(gp_id):
    response = requests.get(f"{BASE_URL}/{gp_id}")
    return response.json()

def create_grammar_point(grammar_point, example_phrase):
    data = {
        "grammar_point": grammar_point,
        "example_phrase": example_phrase
    }
    response = requests.post(BASE_URL, json=data)
    return response.json()

def update_grammar_point(gp_id, grammar_point, example_phrase):
    data = {
        "grammar_point": grammar_point,
        "example_phrase": example_phrase
    }
    response = requests.put(f"{BASE_URL}/{gp_id}", json=data)
    return response.json()

def delete_grammar_point(gp_id):
    response = requests.delete(f"{BASE_URL}/{gp_id}")
    return response.json()

if __name__ == "__main__":
    import app_ops
    # Example usage
    app_ops.reset_db()
    print("Schema:", get_grammar_points_schema())
    
    new_gp = create_grammar_point("Past Tense", "I walked to the store.")
    print("\n\nCreated Grammar Point:", new_gp)
    print("\nAll Grammar Points:", get_all_grammar_points())
    
    
    gp_id = new_gp.get("gp_id")
    print("\n\nGrammar Point ID:", gp_id)
    if gp_id:
        print("Get Grammar Point:", get_grammar_point(gp_id))
        
        updated_gp = update_grammar_point(gp_id, "Past Tense Updated", "I walked to the park.")
        print("\n\nUpdated Grammar Point:", updated_gp)
        print("\nAll Grammar Points:", get_all_grammar_points())
        
        print("\n\nDelete Grammar Point:", delete_grammar_point(gp_id))
        print("\nAll Grammar Points:", get_all_grammar_points())