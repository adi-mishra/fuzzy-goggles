from .UrlInfoRequestHandlerV1 import UrlInfoRequestHandlerV1
from store.StoreFactory import StoreFactory

"""
Factory to create various request handlers.
"""


class RequestHandlerFactory:
    def __init__(self):
        self._storeFactory = StoreFactory()

    """
    Creates version 1 of request handler to handle requests for information about a url.
    """

    def createUrlInfoRequestHandlerV1(self):
        return UrlInfoRequestHandlerV1(self._storeFactory.getUrlInfoStore())
