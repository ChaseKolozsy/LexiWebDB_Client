import requests

BASE_URL = 'http://localhost:5002/api/branch_nodes'

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
    return response

def get_all_branch_nodes():
    response = requests.get(BASE_URL)
    return response

def get_branch_node_by_id(node_id):
    response = requests.get(f'{BASE_URL}/{node_id}')
    return response

def update_branch_node(node_id, data):
    response = requests.put(f'{BASE_URL}/{node_id}', json=data)
    return response

def delete_branch_node(node_id):
    response = requests.delete(f'{BASE_URL}/{node_id}')
    return response

if __name__ == '__main__':
    pass