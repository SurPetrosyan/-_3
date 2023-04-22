from coursework.functions import filter_sort, format_date, mask_card, formatted_data, load_data


def test_filter_sort():
    list_1 = [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2020-08-26T10:50:58.294041"
        },
        {
            "id": 2,
            "state": "CLOSE",
            "date": "2019-08-26T10:50:58.294041"
        },
        {
            "id": 3,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041"
        }
    ]
    list_sort = [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2020-08-26T10:50:58.294041"
        },
        {
            "id": 3,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041"
        }

    ]
    assert list_sort == filter_sort(list_1)


def test_format_date():
    assert format_date('2018-03-23T10:45:06.972075') == '23.03.2018'


def test_mask_card():
    assert mask_card("Счет 75106830613657916952") == 'Счет **6952'
    assert mask_card("Visa Classic 6831982476737658") == 'Visa Classic 683198** **** 7658'


def test_formatted_data():
    dict_1 = {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {
            "amount": "56883.54",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229"
    }
    dict_2 = {
        "id": 596171168,
        "state": "EXECUTED",
        "date": "2018-07-11T02:26:18.671407",
        "operationAmount": {
            "amount": "79931.03",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 72082042523231456215"
    }
    str_1 = '19.08.2018 Перевод с карты на карту\n' \
            'Visa Classic 6831 98** **** 7658 -> Visa Platinum 8990 92** **** 5229\n' \
            '56883.54 USD\n'
    str_2 = '11.07.2018 Открытие вклада\n' \
            'Счет **6215\n' \
            '56883.54 руб.\n'
    assert formatted_data(dict_1) == str_1
    assert formatted_data(dict_2) == str_2


def test_load_data():
    list_1 = [
        {
            "id": 596171168,
            "state": "EXECUTED",
            "date": "2018-07-11T02:26:18.671407",
            "operationAmount": {
                "amount": "79931.03",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 72082042523231456215"
        }

    ]
    assert load_data() == list_1
