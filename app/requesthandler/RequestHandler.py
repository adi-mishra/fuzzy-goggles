import logging

"""
Class intended to be an interface for RequestHandlers
"""


class RequestHandler:
    """
    Handles request of flask from user.
    Returns response to be sent back to user.
    """

    def handleRequest(self, request):
        logging.error("handleRequest method of RequestHandler class has not implemented")
        raise NotImplementedError("Unimplemeted method")
