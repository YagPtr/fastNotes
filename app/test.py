import unittest
import requests
import json
from models.note import Note
from datetime import datetime
# from utils import response_to_dict, result_to_response


class TestingAPI(unittest.TestCase):
    def testComon(self):
        print("test without amount")
        data = requests.get("http://127.0.0.1:8000/notes/")
        # print(data)
        print(data)
        print("status code is ", data.status_code)
        data = data.json()
        self.assertIsNotNone(data)

    def testAPI(self):
        print("test with amount")
        data = requests.get("http://127.0.0.1:8000/notes/2")
        # print(data)
        print(data)
        print("status code is ", data.status_code)
        data = data.json()
        self.assertEqual(1, len(data))

    def testAddNote(self):
        print("valid data load ")
        data = requests.post(
            "http://127.0.0.1:8000/register/",
            json=dict(
                {
                    "Note": "whatever",
                    "data": str(datetime.now().strftime("%m-%d-%y %H:%M")),
                }
            ),
        )
        print(data.text)
        print("status code is ", data.status_code)
        # self.assertEqual(2, len(data))

    def testAddNotNote(self):
        print("error data load")
        data = requests.post(
            "http://127.0.0.1:8000/register/",
            json=dict({}),
        )
        print(data.text)
        print("status code is ", data.status_code)
        # self.assertEqual(2, len(data))


if __name__ == "__main__":
    unittest.main()
