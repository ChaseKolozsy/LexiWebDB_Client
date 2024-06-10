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
    import app_ops
    import enumerated_lemma_ops
    import branch_ops

    app_ops.reset_db()

    # Create enumerated lemmas
    dog_1 = {
        'enumerated_lemma': 'dog_1',
        'base_lemma': 'dog',
        'part_of_speech': 'noun',
        'definition': 'a domesticated carnivorous mammal that typically has a long snout, an acute sense of smell, and a retractable claw',
        'frequency': 12345,
        'phrase': 'Look at the dog who is barking',
        'story_link': 'https://www.example.com',
        'media_excerpts': ['filename.mp4'],
        'object_exploration_link': 'https://www.example.com',
        'familiar': True 
    }
    print("Creating enumerated lemma:", enumerated_lemma_ops.create_enumerated_lemma(data=dog_1))

    # Create a branch
    print("Creating branch:", branch_ops.create_branch('dog_1', 'Dog Branch'))

    ## Get all branches to find the branch_id
    branches = branch_ops.get_all_branches()
    branch_id = branches['branches'][0]['branch_id']
    print("\n\nAll branches:", branches)

    # Create a branch node for dog_1
    print("\n\nCreating branch node for dog_1:", create_branch_node(branch_id, 'dog_1'))

    # Create a child node for dog_1
    child_lemma = {
        'enumerated_lemma': 'canine',
        'base_lemma': 'canine',
        'part_of_speech': 'noun',
        'definition': 'a member of the dog family',
        'frequency': 100,
        'phrase': 'The canine is a loyal animal.',
        'story_link': 'https://www.example.com',
        'media_excerpts': ['filename_canine.mp4'],
        'object_exploration_link': 'https://www.example.com',
        'familiar': True 
    }
    print("\n\nCreating enumerated lemma for child node:", enumerated_lemma_ops.create_enumerated_lemma(data=child_lemma))

    # Get the node_id of dog_1
    branch_nodes = get_all_branch_nodes()
    dog_1_node_id = next(node['node_id'] for node in branch_nodes['branch_nodes'] if node['enumerated_lemma'] == 'dog_1')
    print("\n\nAll branch nodes:", branch_nodes)

    # Create a branch node for the child lemma with dog_1 as the parent
    print("\n\nCreating branch node for child lemma:", create_branch_node(branch_id, 'canine', parent_node_id=dog_1_node_id))

    # Verify the parent-child relationship
    branch_nodes = get_all_branch_nodes()
    print("All branch nodes after adding child:", branch_nodes)

    ## Get branch node by ID
    node_id = dog_1_node_id
    print(f"\n\nBranch node {node_id}:", get_branch_node_by_id(node_id))

    # Delete branch node
    print(f"\n\nDeleting branch node {node_id}:", delete_branch_node(node_id))

    branch_nodes = get_all_branch_nodes()
    print("All branch nodes after adding child:", branch_nodes)