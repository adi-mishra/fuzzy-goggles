from .UrlInfoStore import UrlInfoStore
from .datastore.DynamoDbUrlBlacklistDataStore import DynamoDbUrlBlacklistDataStore

"""
Factory class to represent various representation of storing information.
"""


class StoreFactory:
    def __init__(self):
        self._urlInfoStore = UrlInfoStore(DynamoDbUrlBlacklistDataStore())

    """
    Returns class that facilitates storing and querying of information about a url.
    """

    def getUrlInfoStore(self):
        return self._urlInfoStore
