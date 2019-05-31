"""
Class for storing information about a url.
"""


class UrlStore:
    def __init__(self, dataStore):
        self._dataStore = dataStore

    """
    Get if the url is a safe url.

    returns true/false if information was fetched about url being safe or not.
    raises Store error in case of error.
    """

    def isSafe(self, url):
        result = self._dataStore.hasItem(url)
        return not result

    """
    Add url to blacklist.
    raises Store error in case of error.
    """

    def addUrlToBlacklist(self, url):
        result = self._dataStore.addItem(url)
        return result
