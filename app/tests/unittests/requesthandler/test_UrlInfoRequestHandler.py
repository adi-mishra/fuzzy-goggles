import unittest
from unittest.mock import Mock
import json
from requesthandler.UrlInfoRequestHandlerV1 import UrlInfoRequestHandlerV1


class TestUrlInfoRequestHandler(unittest.TestCase):

    def setUp(self):
        self.mockUrlInfoStore = Mock()
        self.mockRequest = Mock()
        self.urlRequestHandlerV1 = UrlInfoRequestHandlerV1(self.mockUrlInfoStore)

    def test_getInfoResponseBody_returns_expectedJsonStructure(self):
        self.mockUrlInfoStore.isSafe.return_value = False
        self.mockRequest.url = "http://something.com:8080/urlinfo/1/some/url"
        response = self.urlRequestHandlerV1.handleRequest(self.mockRequest)
        self.mockUrlInfoStore.isSafe.assert_called_once_with("some/url")
        responseJson = response.get_json()

        assert responseJson["version"] == "1.0"
        assert responseJson["result"]["version"] == "1.0"
        assert responseJson["result"]["is_safe"] is False
