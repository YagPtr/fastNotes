import unittest
import requests
from datetime import datetime


class TestingAPI(unittest.TestCase):
    def testComon(self):
        print("test without amount")
        data = requests.get("http://127.0.0.1:8000/notes/")
        print("status code is ", data.status_code)
        data = data.json()
        self.assertIsNotNone(data)

    def testAPI(self):
        print("test with amount")
        data = requests.get("http://127.0.0.1:8000/notes/2")
        print(data.text)
        print("status code is ", data.status_code)
        data = data.json()

    def testAddNote(self):
        print("valid data load ")
        data = requests.post(
            "http://127.0.0.1:8000/notes/",
            json=dict(
                {
                    "Note": "whatever",
                    "data": str(datetime.now().strftime("%m-%d-%y %H:%M")),
                }
            ),
        )
        print(data.text)
        print("status code is ", data.status_code)

    def testAddNotNote(self):
        print("error data load")
        data = requests.post(
            "http://127.0.0.1:8000/notes/",
            json=dict({}),
        )
        print(data.text)
        print("status code is ", data.status_code)

    def testDeleteNotNote(self):
        print("delete note")
        data = requests.delete(
            "http://127.0.0.1:8000/notes/4",
        )
        print(data.text)

        print("status code is ", data.status_code)


if __name__ == "__main__":
    unittest.main()
