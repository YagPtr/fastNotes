import unittest
import requests
from datetime import datetime


class TestingAPI(unittest.TestCase):
    def testComon(self):
        print("test without amount")
        data = requests.get("http://127.0.0.1:8000/notes/")
        print("status code is ", data.status_code)
        assert data.status_code==200
        data = data.json()
        assert data is not None
        

    def testAPI(self):
        print("test with amount")
        data = requests.get("http://127.0.0.1:8000/notes/me")
        print(data.text)
        print("status code is ", data.status_code)
        data = data.json() 

    def testAddNote(self):
        print("valid data load ")
        data = requests.post(
            "http://127.0.0.1:8000/notes/",
            json=dict(
                {
                    "Note": "whatever","author":"me"
                }
            ),
        )
        print(data.text)
        assert data.status_code==200
        print("status code is ", data.status_code)

    def testAddNotNote(self):
        print("error data load")
        data = requests.post(
            "http://127.0.0.1:8000/notes/",
            json=dict({}),
        )
        print(data.text)
        print("status code is ", data.status_code)
        assert data.status_code==502

 
    def testDeleteNotNote(self):
        print("delete note")
        data = requests.delete(
            "http://127.0.0.1:8000/notes/1",
        )
        print(data)

        print(data.text)
        print("status code is ", data.status_code)
        assert data.status_code==200



if __name__ == "__main__":
    unittest.main()
