from .UrlInfoStore import UrlInfoStore

"""
Factory class to represent various representation of storing information
"""


class StoreFactory:
    def __init__(self):
        self._urlInfoStore = UrlInfoStore()

    """
    Returns class that facilitates storing and querying of information about a url.
    """

    def getUrlInfoStore(self):
        return self._urlInfoStore
