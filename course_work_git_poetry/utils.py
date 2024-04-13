import json
import os.path


def input_json_data():
    path = os.path.join("..", "resource", "operations.json")
    with open(path, "r") as file:
        data = json.load(file)
    return data


def print_exec_str():
    for value in input_json_data():
        if 'state' in value:
            if value['state'].lower() == 'executed':
                print(value)
