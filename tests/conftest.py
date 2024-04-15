import pytest


@pytest.fixture
def inp_data_dict_main():
    return {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364',
            'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}},
            'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758',
            'to': 'Счет 35383033474447895560'}


@pytest.fixture
def inp_data_dict_amount():
    return {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}
