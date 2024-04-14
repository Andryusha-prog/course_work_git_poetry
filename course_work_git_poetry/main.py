import utils

inp_data = utils.input_json_data()

last_5_oper = utils.take_exec_str(inp_data)

for elem in last_5_oper:
    print(utils.create_output_data(elem))
