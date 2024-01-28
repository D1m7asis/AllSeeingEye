import json
import unittest

import requests

url = 'http://127.0.0.1:5000/visited_links'
headers = {'Content-type': 'application/json'}
getparams = {'from': '1000000000', 'to': '2000000000'}
postjson = {
    "links": [
        "https://ya.ru/",
        "https://ya.ru/search/?text=мемы+с+котиками",
        "https://sber.ru",
        "https://stackoverflow.com/questions/65724760/how-it-is"]
}
testDomains = [
    "ya.ru",
    "sber.ru",
    "stackoverflow.com"
]


class MyTestCase(unittest.TestCase):
    def test_GETRequests(self):
        resp = requests.get(url, params=getparams)
        print(resp.text)
        assert (json.loads(resp.text)['status'] == 'ok'), 'GETReq'

    def test_POSTRequests(self):
        resp = requests.post(url, json=postjson, headers=headers)
        print(resp.text)
        assert (json.loads(resp.text)['status'] == 'ok'), 'POSTReq'

    def test_POSTnGETRequests(self):
        postresp = requests.post(url, json=postjson, headers=headers)
        getresp = requests.get(url, params=getparams)

        print(postresp.text)
        print(getresp.text)

        assert (json.loads(postresp.text)['status'] == 'ok'), 'POSTReq'
        assert (json.loads(getresp.text)['status'] == 'ok'), 'GETReq'
        assert (json.loads(getresp.text)['domains'] == testDomains)


if __name__ == '__main__':
    unittest.main()
