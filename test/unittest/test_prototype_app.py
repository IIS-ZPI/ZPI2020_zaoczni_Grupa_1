from unittest import TestCase

import os
from json.decoder import JSONDecodeError

import prototypes.app

class TestPrototypeApp(TestCase):
    def test_parseResponse_correct_address(self):
        test_address = "http://api.nbp.pl/api/cenyzlota"
        actual_response_list = prototypes.app.parseResponse(test_address).json()
        actual_response = actual_response_list[0]
        try:
            check = actual_response["data"]
            check = actual_response["cena"]
        except JSONDecodeError as e:
            self.fail("Incorrect response")    
        
    def test_parseResponse_wrong_address(self):
        test_address = "http://api.nbp.pl/api/cenyzlota_incorrect" #intentionally wrong address
        actual_response = prototypes.app.parseResponse(test_address)
        self.assertFalse(actual_response.ok, "Correct response when incorrect expected")

    def test_saveResponse_if_file_exists(self):
        test_file_path = "response.txt" #hardcoded in tested function
        test_response = """[{"data":"2021-01-08","cena":226.28}]""" #test value
        prototypes.app.saveResponse(test_response)
        self.assertTrue(os.path.exists(test_file_path), "File does not exist")
