from .Result import Result

"""
Represent the result of request for information about a url
"""


class UrlInfoResultV1(Result):
    def __init__(self, isSafe):
        self._isSafe = isSafe
        self._version = "1.0"

    """
    Get if information requested about a url contains the url being safe. 
    """

    def getIsSafe(self):
        return self._isSafe

    """
    Get serializable representation of this result object.
    """

    def getSerializableResult(self):
        seriazableResult = {"is_safe": self._isSafe, "version": self._version}
        return seriazableResult
