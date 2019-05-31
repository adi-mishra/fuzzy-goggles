from .UrlInfoRequestHandler import UrlInfoRequestHandler
from result.ResultFactory import ResultFactory
from response.ResponseFactory import ResponseFactory
from responseconverter.ResponseConverterFactory import ResponseConverterFactory
import logging

"""
Version 1 of class that handles url information requests.
"""


class UrlInfoRequestHandlerV1(UrlInfoRequestHandler):
    def __init__(self, urlInfoStore):
        self._urlInfoStore = urlInfoStore

    """
    Get information about supplied url.
    Returns valid json response body to be sent back to the user or None in case of error.
    """

    def getSerializedResponse(self, url):
        isUrlSafe = self._urlInfoStore.isSafe(url)
        if isUrlSafe == None:
            logging.warning("Could not fetch information about requested url: %s" % url)
            return None

        result = ResultFactory.createUrlInfoResultV1(isUrlSafe)

        response = ResponseFactory.createResponseV1(result)
        responseGenerator = ResponseConverterFactory.createPrettyJsonConverter()
        return responseGenerator.convertSerializedResponse(response)
