import logging

"""
Class intended to be an interface for UrlInfo RequestHandlers
"""


class UrlInfoRequestHandler:
    """
    Get information about supplied url in a serialized format to be sent back as response payload.
    Returns information fetched about requested url or else returns None in case of error.
    """

    def getSerializedResponse(self, url):
        logging.error("getInfoResponseBody method of UrlInfoRequestHandler class has not implemented")
        raise NotImplementedError("Unimplemeted method")
