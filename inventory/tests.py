from django.test import TestCase
import requests
import json
import unittest

# Create your tests here.


base_url = "http://127.0.0.1:8000/retrieve_view/"
def get_all_data(sid = None):
    data = {}
    # print(data)
    if sid :
        data = {"id" : sid}
    py2json = json.dumps(data)
    response = requests.get(base_url,data=py2json)
    # print(response)
    
    return response.json()
    


class Retrievetest(unittest.TestCase) :
    """"Testing the retrieve function"""

    def test_getmethod(self):
        result = get_all_data()
        self.assertEqual(result,"Data retrieved successfully")


if __name__ == "__main__"     :
    unittest.main()