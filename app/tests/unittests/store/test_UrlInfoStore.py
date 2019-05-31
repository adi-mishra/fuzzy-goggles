import unittest
from unittest.mock import Mock
from store.UrlStore import UrlStore


class TestUrlInfoStore(unittest.TestCase):

    def setUp(self):
        self.mockDataStore = Mock()
        self.urlInfoStore = UrlStore(self.mockDataStore)

    def test_isSafeReturnsTrue_whenResponseForHasItemFromDataStoreIsFalse(self):
        self.mockDataStore.hasItem.return_value = False
        response = self.urlInfoStore.isSafe("some/url")
        self.mockDataStore.hasItem.assert_called_once_with("some/url")
        assert response is True

    def test_isSafeReturnsFalse_whenResponseForHasItemFromDataStoreIsTrue(self):
        self.mockDataStore.hasItem.return_value = True
        response = self.urlInfoStore.isSafe("some/url")
        self.mockDataStore.hasItem.assert_called_once_with("some/url")
        assert response is False
