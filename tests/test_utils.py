import course_work_git_poetry.utils
from tests.conftest import inp_data_dict_amount


def test_create_output_data(inp_data_dict_main):
    assert course_work_git_poetry.utils.create_output_data(inp_data_dict_main) == "03.07.2019 Перевод организации\nMasterCard 7158 30** **** 6758 -> Счет **5560\n8221.37 USD\n"


def test_from_operation():
    assert course_work_git_poetry.utils.from_operation('Maestro 1596837868705199') == 'Maestro 1596 83** **** 5199'
    assert course_work_git_poetry.utils.from_operation(None) == ''


def test_to_operation():
    assert course_work_git_poetry.utils.to_operation('Счет 11776614605963066702') == 'Счет **6702'


def test_amount_operation(inp_data_dict_amount):
    assert course_work_git_poetry.utils.amount_operation(inp_data_dict_amount) == '31957.58 руб.'
