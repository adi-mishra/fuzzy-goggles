from .UrlInfoResultV1 import UrlInfoResultV1

"""
Factory class to create various classes to represent Result of a request
"""


class ResultFactory:
    """
    Creates class to represent result of request for information about a url.
    """

    @staticmethod
    def createUrlInfoResultV1(isSafe):
        return UrlInfoResultV1(isSafe)
