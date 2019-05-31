from .RequestHandler import RequestHandler
from result.ResultFactory import ResultFactory
from response.ResponseFactory import ResponseFactory
from responseconverter.ResponseConverterFactory import ResponseConverterFactory
from errors.StoreError import StoreError
import logging
from flask import Response

"""
Version 1 of class that handles url information requests.
"""


class UrlInfoRequestHandlerV1(RequestHandler):
    def __init__(self, urlStore):
        self._urlStore = urlStore

    """
    Get information about supplied url as part of request.
    Returns valid response to be sent back to the user.
    """

    def handleRequest(self, request):
        entireUrl = request.url
        pathPrefix = "/urlinfo/1/"

        indexOfExpectedUrlToQuery = entireUrl.find(pathPrefix)
        urlToQuery = entireUrl[indexOfExpectedUrlToQuery + len(pathPrefix):]

        logging.info("Request received for information about url: %s" % urlToQuery)

        try:
            isUrlSafe = self._urlStore.isSafe(urlToQuery)
        except StoreError:
            logging.warning("Could not fetch information about requested url: %s" % urlToQuery)
            return Response(response="Internal error when handling url information request, url:" % urlToQuery,
                            status=500,
                            mimetype='text/plain')
        else:
            result = ResultFactory.createUrlInfoResultV1(isUrlSafe)
            response = ResponseFactory.createResponseV1(result)
            responseGenerator = ResponseConverterFactory.createPrettyJsonConverter()
            return Response(response=responseGenerator.convertSerializedResponse(response),
                            status=200,
                            mimetype='application/json')
