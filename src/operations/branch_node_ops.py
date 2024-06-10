import requests

BASE_URL = 'http://localhost:5002/branch_nodes'

def get_branch_nodes_schema():
    response = requests.get(f'{BASE_URL}/schema')
    return response.json()

def create_branch_node(branch_id, enumerated_lemma, parent_node_id=None):
    data = {
        'branch_id': branch_id,
        'enumerated_lemma': enumerated_lemma,
        'parent_node_id': parent_node_id
    }
    response = requests.post(BASE_URL, json=data)
    return response.json()

def get_all_branch_nodes():
    response = requests.get(BASE_URL)
    return response.json()

def get_branch_node_by_id(node_id):
    response = requests.get(f'{BASE_URL}/{node_id}')
    return response.json()

def update_branch_node(node_id, data):
    response = requests.put(f'{BASE_URL}/{node_id}', json=data)
    return response.json()

def delete_branch_node(node_id):
    response = requests.delete(f'{BASE_URL}/{node_id}')
    return response.json()

if __name__ == '__main__':
    # Example usage
    print("Schema:", get_branch_nodes_schema())

    print("Creating branch node:", create_branch_node(1, 'lemma1'))

    print("All branch nodes:", get_all_branch_nodes())

    node_id = 1
    print(f"Branch node {node_id}:", get_branch_node_by_id(node_id))

    update_data = {'enumerated_lemma': 'updated_lemma1'}
    print(f"Updating branch node {node_id}:", update_branch_node(node_id, update_data))

    print(f"Deleting branch node {node_id}:", delete_branch_node(node_id))