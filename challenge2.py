uri = "https://jsonplaceholder.typicode.com/todos/{}"
todo_ids = list(range(1, 51))

import requests
import json




def write_json_file():
    """
    should save json data into a json file
    """
    helper_dict = {}

    for id in todo_ids:
        data = requests.get(f"https://jsonplaceholder.typicode.com/todos/{id}").json
        helper_dict[data] = id
    
    final_json = json.dumps(helper_dict)
    with open("document.json", "w") as document:
        document.write(final_json)





def get_todos():
    """
    Given a list of todo ids,  fetch each todo and return a list of todos
    Example of a request: https://jsonplaceholder.typicode.com/todos/1

    Step 2: Make sure to use or have used a mechanism to improve performance
    """
    return []


##todos = get_todos()
write_json_file()