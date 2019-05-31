"""
Class for storing information about a url.
"""


class UrlInfoStore:
    def __init__(self, dataStore):
        self._dataStore = dataStore

    """
    Get if the url is a safe url.

    returns true/false if information was fetched about url being safe or not. None if an error occurred.
    """

    def isSafe(self, url):
        result = self._dataStore.hasItem(url)
        if result == None:
            return None
        elif result == True:
            return False
        else:
            return True
