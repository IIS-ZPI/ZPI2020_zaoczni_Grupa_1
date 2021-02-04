import os

valid_test_data = {
    "dataset": {
        'code': 'USD',
        'currency': 'dolar amerykański',
        'rates': [{
                'effectiveDate': '2020-12-17',
                'mid': 3.6254,
                'no': '246/A/NBP/2020'
        },
            {
                'effectiveDate': '2020-12-18',
                'mid': 3.6322,
                'no': '247/A/NBP/2020'
        },
            {
                'effectiveDate': '2020-12-21',
                'mid': 3.7082,
                'no': '248/A/NBP/2020'
        },
            {
                'effectiveDate': '2020-12-22',
                'mid': 3.6921,
                'no': '249/A/NBP/2020'
        },
            {
                'effectiveDate': '2020-12-23',
                'mid': 3.6919,
                'no': '250/A/NBP/2020'
        },
            {
                'effectiveDate': '2020-12-24',
                'mid': 3.6981,
                'no': '251/A/NBP/2020'
        },
            {
                'effectiveDate': '2020-12-28',
                'mid': 3.6639,
                'no': '252/A/NBP/2020'
        },
            {
                'effectiveDate': '2020-12-29',
                'mid': 3.6778,
                'no': '253/A/NBP/2020'
        },
            {
                'effectiveDate': '2020-12-30',
                'mid': 3.6901,
                'no': '254/A/NBP/2020'
        },
            {
                'effectiveDate': '2020-12-31',
                'mid': 3.7584,
                'no': '255/A/NBP/2020'
        },
            {
                'effectiveDate': '2021-01-04',
                'mid': 3.6998,
                'no': '001/A/NBP/2021'
        },
            {
                'effectiveDate': '2021-01-05',
                'mid': 3.7031,
                'no': '002/A/NBP/2021'
        },
            {
                'effectiveDate': '2021-01-07',
                'mid': 3.6656,
                'no': '003/A/NBP/2021'
        },
            {
                'effectiveDate': '2021-01-08',
                'mid': 3.6919,
                'no': '004/A/NBP/2021'
        }
        ],
        'table': 'A'
    },
    "results": {
        "increase": 8,
        "decrease": 5,
        "stable": 0
    }
}


invalid_test_data = {
    "dataset": {
        'some rubbish data': 'invalid'
    },
    "results": None
}


currency_EUR_exchange = {
    "table": "A",
    "currency": "euro",
    "code": "EUR",
    "rates": [{
        "no": "255/A/NBP/2020",
        "effectiveDate": "2020-12-31",
        "mid": 4.6148
    }, {
        "no": "001/A/NBP/2021",
        "effectiveDate": "2021-01-04",
        "mid": 4.5485
    }, {
        "no": "002/A/NBP/2021",
        "effectiveDate": "2021-01-05",
        "mid": 4.5446
    }, {
        "no": "003/A/NBP/2021",
        "effectiveDate": "2021-01-07",
        "mid": 4.4973
    }, {
        "no": "004/A/NBP/2021",
        "effectiveDate": "2021-01-08",
        "mid": 4.5189
    }, {
        "no": "005/A/NBP/2021",
        "effectiveDate": "2021-01-11",
        "mid": 4.5325
    }, {
        "no": "006/A/NBP/2021",
        "effectiveDate": "2021-01-12",
        "mid": 4.5228
    }, {
        "no": "007/A/NBP/2021",
        "effectiveDate": "2021-01-13",
        "mid": 4.5272
    }, {
        "no": "008/A/NBP/2021",
        "effectiveDate": "2021-01-14",
        "mid": 4.5407
    }, {
        "no": "009/A/NBP/2021",
        "effectiveDate": "2021-01-15",
        "mid": 4.5480
    }, {
        "no": "010/A/NBP/2021",
        "effectiveDate": "2021-01-18",
        "mid": 4.5473
    }, {
        "no": "011/A/NBP/2021",
        "effectiveDate": "2021-01-19",
        "mid": 4.5342
    }, {
        "no": "012/A/NBP/2021",
        "effectiveDate": "2021-01-20",
        "mid": 4.5237
    }, {
        "no": "013/A/NBP/2021",
        "effectiveDate": "2021-01-21",
        "mid": 4.5310
    }, {
        "no": "014/A/NBP/2021",
        "effectiveDate": "2021-01-22",
        "mid": 4.5354
    }, {
        "no": "015/A/NBP/2021",
        "effectiveDate": "2021-01-25",
        "mid": 4.5436
    }, {
        "no": "016/A/NBP/2021",
        "effectiveDate": "2021-01-26",
        "mid": 4.5497
    }, {
        "no": "017/A/NBP/2021",
        "effectiveDate": "2021-01-27",
        "mid": 4.5468
    }, {
        "no": "018/A/NBP/2021",
        "effectiveDate": "2021-01-28",
        "mid": 4.5479
    }, {
        "no": "019/A/NBP/2021",
        "effectiveDate": "2021-01-29",
        "mid": 4.5385
    }]
}
currency_USD_exchange = {
    'table': 'A',
    'currency': 'dolar amerykański',
    'code': 'USD',
    'rates': [{
        'no': '255/A/NBP/2020',
        'effectiveDate': '2020-12-31',
        'mid': 3.7584
    }, {
        'no': '001/A/NBP/2021',
        'effectiveDate': '2021-01-04',
        'mid': 3.6998
    }, {
        'no': '002/A/NBP/2021',
        'effectiveDate': '2021-01-05',
        'mid': 3.7031
    }, {
        'no': '003/A/NBP/2021',
        'effectiveDate': '2021-01-07',
        'mid': 3.6656
    }, {
        'no': '004/A/NBP/2021',
        'effectiveDate': '2021-01-08',
        'mid': 3.6919
    }, {
        'no': '005/A/NBP/2021',
        'effectiveDate': '2021-01-11',
        'mid': 3.7271
    }, {
        'no': '006/A/NBP/2021',
        'effectiveDate': '2021-01-12',
        'mid': 3.7188
    }, {
        'no': '007/A/NBP/2021',
        'effectiveDate': '2021-01-13',
        'mid': 3.7142
    }, {
        'no': '008/A/NBP/2021',
        'effectiveDate': '2021-01-14',
        'mid': 3.7323
    }, {
        'no': '009/A/NBP/2021',
        'effectiveDate': '2021-01-15',
        'mid': 3.7466
    }, {
        'no': '010/A/NBP/2021',
        'effectiveDate': '2021-01-18',
        'mid': 3.7699
    }, {
        'no': '011/A/NBP/2021',
        'effectiveDate': '2021-01-19',
        'mid': 3.7416
    }, {
        'no': '012/A/NBP/2021',
        'effectiveDate': '2021-01-20',
        'mid': 3.7303
    }, {
        'no': '013/A/NBP/2021',
        'effectiveDate': '2021-01-21',
        'mid': 3.7312
    }, {
        'no': '014/A/NBP/2021',
        'effectiveDate': '2021-01-22',
        'mid': 3.7255
    }, {
        'no': '015/A/NBP/2021',
        'effectiveDate': '2021-01-25',
        'mid': 3.7402
    }, {
        'no': '016/A/NBP/2021',
        'effectiveDate': '2021-01-26',
        'mid': 3.7512
    }, {
        'no': '017/A/NBP/2021',
        'effectiveDate': '2021-01-27',
        'mid': 3.7507
    }, {
        'no': '018/A/NBP/2021',
        'effectiveDate': '2021-01-28',
        'mid': 3.7566
    }, {
        'no': '019/A/NBP/2021',
        'effectiveDate': '2021-01-29',
        'mid': 3.746
    }]
}


# Utility functions


def create_empty_file_in_directory(filename, subdirectory_path):
    directory_path = os.path.join(os.getcwd(), subdirectory_path)
    file_path = os.path.join(os.getcwd(), directory_path, filename)
    if (os.path.exists(directory_path) == False):
        os.mkdir(directory_path)
    if os.path.isfile(file_path):
        os.remove(file_path)
    try:
        open(file_path, "w")
    except IOError:
        return None
    return file_path
