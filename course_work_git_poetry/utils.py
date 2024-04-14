import datetime
import json
import os.path


def input_json_data():
    path = os.path.join("..", "resource", "operations.json")
    with open(path, "r") as file:
        data = json.load(file)
    return data


def take_exec_str(inp_json_data):
    result = []

    for value in inp_json_data:
        if 'state' in value:
            if value['state'].lower() == 'executed':
                result.append(value)

    result.sort(key=lambda x: x['date'], reverse=True)

    return result[:5]


def create_output_data(elem: dict):
    temp_date = datetime.datetime.fromisoformat(elem['date'])
    date_operation = temp_date.strftime('%d.%m.%Y')

    description_operation = elem['description']

    data_from = from_operation(elem.get('from'))
    data_to = to_operation(elem['to'])
    rubles = amount_operation(elem['operationAmount'])

    return (f'{date_operation} {description_operation}\n'
            f'{data_from} -> {data_to}\n'
            f'{rubles}\n')


def from_operation(inp: str):
    if inp:
        *str_data, num = inp.split(' ')

        new_num = f'{num[:4]} {num[4:6]}** **** {num[-4:]}'
        return f"{' '.join(str_data)} {new_num}"

    else:
        return ''


def to_operation(inp: str):
    *str_data, num = inp.split(' ')
    return f'{" ".join(str_data)} **{num[-4:]}'


def amount_operation(inp: dict):
    return f"{inp['amount']} {inp['currency']['name']}"
