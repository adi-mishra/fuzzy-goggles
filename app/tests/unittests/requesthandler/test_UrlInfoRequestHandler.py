import unittest
from unittest.mock import Mock
import json
from requesthandler.UrlInfoRequestHandlerV1 import UrlInfoRequestHandlerV1


class TestUrlInfoRequestHandler(unittest.TestCase):

    def setUp(self):
        self.mockUrlInfoStore = Mock()
        self.urlRequestHandlerV1 = UrlInfoRequestHandlerV1(self.mockUrlInfoStore)

        self.expectedJsonStructure = "{}"

    def test_getInfoResponseBody_returns_expectedJsonStructure(self):
        self.mockUrlInfoStore.isSafe.return_value = False
        response = self.urlRequestHandlerV1.getSerializedResponse("some/url")
        self.mockUrlInfoStore.isSafe.assert_called_once_with("some/url")
        responseObj = json.loads(response)

        assert responseObj["version"] == "1.0"
        assert responseObj["result"]["version"] == "1.0"
        assert responseObj["result"]["is_safe"] == False

    def test_getInfoResponseBody_returns_NoneIfStoreReturnsNone(self):
        self.mockUrlInfoStore.isSafe.return_value = None
        response = self.urlRequestHandlerV1.getSerializedResponse("some/url")
        self.mockUrlInfoStore.isSafe.assert_called_once_with("some/url")
        assert response is None
