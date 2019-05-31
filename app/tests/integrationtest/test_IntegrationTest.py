import unittest
import requests
import os
import random
import string
import json


class IntegrationTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        os.system('cd ../../../ && docker-compose build && docker-compose up --scale app=5 -d')

    def getUniqueUrl(self):
        return "integTest.com:66/" + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))

    def test_expectedResponseWhenrequestingInformationAboutNonBlacklistedUrls(self):
        url = self.getUniqueUrl()
        responseBlob = requests.get("http://localhost/urlinfo/1/%s" % url)
        response = responseBlob.json()

        assert response["version"] == "1.0"
        assert response["result"]["version"] == "1.0"
        assert response["result"]["is_safe"] is True

    def test_expectedResponseWhenrequestingInformationAboutBlacklistedUrl(self):
        url = self.getUniqueUrl()
        requests.post("http://localhost/blacklist/1", data=json.dumps({"url": url}))
        responseBlob = requests.get("http://localhost/urlinfo/1/%s" % url)
        response = responseBlob.json()

        assert response["version"] == "1.0"
        assert response["result"]["version"] == "1.0"
        assert response["result"]["is_safe"] is False

    def test_malformedPayloadForBlacklistingUrlReturnsExpectedErrorCodes(self):
        response = requests.post("http://localhost/blacklist/1", data='simpleString', )
        assert response.status_code == 400
        response = requests.post("http://localhost/blacklist/1", data=json.dumps({"simple": "json"}))
        assert response.status_code == 400
