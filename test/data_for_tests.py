import os

valid_test_data = {
    "dataset":
    {
        'code': 'USD',
        'currency': 'dolar amerykański',
        'rates': [
            {'effectiveDate': '2020-12-17', 'mid': 3.6254, 'no': '246/A/NBP/2020'},
            {'effectiveDate': '2020-12-18', 'mid': 3.6322, 'no': '247/A/NBP/2020'},
            {'effectiveDate': '2020-12-21', 'mid': 3.7082, 'no': '248/A/NBP/2020'},
            {'effectiveDate': '2020-12-22', 'mid': 3.6921, 'no': '249/A/NBP/2020'},
            {'effectiveDate': '2020-12-23', 'mid': 3.6919, 'no': '250/A/NBP/2020'},
            {'effectiveDate': '2020-12-24', 'mid': 3.6981, 'no': '251/A/NBP/2020'},
            {'effectiveDate': '2020-12-28', 'mid': 3.6639, 'no': '252/A/NBP/2020'},
            {'effectiveDate': '2020-12-29', 'mid': 3.6778, 'no': '253/A/NBP/2020'},
            {'effectiveDate': '2020-12-30', 'mid': 3.6901, 'no': '254/A/NBP/2020'},
            {'effectiveDate': '2020-12-31', 'mid': 3.7584, 'no': '255/A/NBP/2020'},
            {'effectiveDate': '2021-01-04', 'mid': 3.6998, 'no': '001/A/NBP/2021'},
            {'effectiveDate': '2021-01-05', 'mid': 3.7031, 'no': '002/A/NBP/2021'},
            {'effectiveDate': '2021-01-07', 'mid': 3.6656, 'no': '003/A/NBP/2021'},
            {'effectiveDate': '2021-01-08', 'mid': 3.6919, 'no': '004/A/NBP/2021'}
        ],
        'table': 'A'
    },
    "results":
    {
        "increase": 8,
        "decrease": 5,
        "stable": 0
    }
}


invalid_test_data = {
    "dataset":
    {
        'some rubbish data': 'invalid'
    },
    "results": None
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
