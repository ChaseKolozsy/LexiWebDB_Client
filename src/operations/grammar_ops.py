import requests

BASE_URL = "http://localhost:5002/api/grammar_points"

def get_grammar_points_schema():
    response = requests.get(f"{BASE_URL}/schema")
    return response

def get_all_grammar_points():
    response = requests.get(BASE_URL)
    return response

def get_grammar_point(gp_id):
    response = requests.get(f"{BASE_URL}/{gp_id}")
    return response

def create_grammar_point(grammar_point, example_phrase):
    data = {
        "grammar_point": grammar_point,
        "example_phrase": example_phrase
    }
    response = requests.post(BASE_URL, json=data)
    return response

def update_grammar_point(gp_id, grammar_point, example_phrase):
    data = {
        "grammar_point": grammar_point,
        "example_phrase": example_phrase
    }
    response = requests.put(f"{BASE_URL}/{gp_id}", json=data)
    return response

def delete_grammar_point(gp_id):
    response = requests.delete(f"{BASE_URL}/{gp_id}")
    return response

if __name__ == "__main__":
    pass