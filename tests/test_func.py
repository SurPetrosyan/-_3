from functions import filter_sort, format_date, mask_card


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
