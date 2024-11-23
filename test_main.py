import json
import unittest

import requests

url = "http://localhost:5000/visited_links"
headers = {"Content-type": "application/json"}
datetime_from_epoch = {"from": "1000000000", "to": "2000000000"}
post_json = {
    "links": [
        "https://ya.ru/",
        "https://ya.ru/search/?text=мемы+с+котиками",
        "https://sber.ru",
        "https://stackoverflow.com/questions/65724760/how-it-is",
    ]
}
testDomains = ["ya.ru", "sber.ru", "stackoverflow.com"]


class MyTestCase(unittest.TestCase):
    @staticmethod
    def test_GETRequests():
        response = requests.get(url, params=datetime_from_epoch)

        print()
        print("test_POSTRequests", "response", response.text)

        assert json.loads(response.text)["status"] == "ok", "GETReq"

    @staticmethod
    def test_POSTRequests():
        response = requests.post(url, json=post_json, headers=headers)

        print()
        print("test_POSTRequests", "response", response.text)

        assert json.loads(response.text)["status"] == "ok", "POSTReq"

    @staticmethod
    def test_POSTnGETRequests():
        post_response = requests.post(url, json=post_json, headers=headers)
        get_response = requests.get(url, params=datetime_from_epoch)

        print()
        print("post_response", post_response.text)
        print("get_response", get_response.text)

        assert json.loads(post_response.text)["status"] == "ok", "POSTReq"
        assert json.loads(get_response.text)["status"] == "ok", "GETReq"
        assert json.loads(get_response.text)["domains"] == testDomains


if __name__ == "__main__":
    unittest.main()
