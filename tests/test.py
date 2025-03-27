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
        data = requests.get("http://127.0.0.1:8000/notes/12313")
        print(data.text)
        print("status code is ", data.status_code)
        data = data.json() 

    def testAddUser(self):
        print("add new user")
        data = requests.post(
            "http://127.0.0.1:8000/notes/register/",
            json=dict(
                {
                    "user_id": "whatever", 
                    "first_name":"whatever",
                    "last_name":"whatever"
                }
            ),
        )

    def testAddNote(self):
        print("valid data load ")
        data = requests.post(
            "http://127.0.0.1:8000/notes/",
            json=dict(
                {
                    "Note": "whatever","user_id":"whatever"
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



# if __name__ == "__main__":
#     unittest.main()
