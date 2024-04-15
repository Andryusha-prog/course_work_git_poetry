import utils

inp_data = utils.input_json_data()

last_5_oper = utils.take_last_operation(inp_data)

for elem in last_5_oper:
    print(utils.create_output_data(elem))


#for i in inp_data:
#    print(i)
print(utils.create_output_data({'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364', 'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758', 'to': 'Счет 35383033474447895560'}))