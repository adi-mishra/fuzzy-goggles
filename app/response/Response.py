import logging

"""
A class intended to be interface for various representations of Responses
"""


class Response:
    """
    Create serializable representation of response object
    """

    def getSerializableResponse(self):
        logging.error("getSerializableResponse method of Response class has not implemented")
        raise NotImplementedError("Unimplemeted method")
