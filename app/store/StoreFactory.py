from .UrlStore import UrlStore
from .datastore.DynamoDbUrlBlacklistDataStore import DynamoDbUrlBlacklistDataStore

"""
Factory class to represent various representation of storing information.
"""


class StoreFactory:
    def __init__(self):
        self._urlStore = UrlStore(DynamoDbUrlBlacklistDataStore())

    """
    Returns class that facilitates storing and querying of information about a url.
    """

    def getUrlStore(self):
        return self._urlStore
