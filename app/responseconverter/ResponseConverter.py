import logging

"""
Class intended to be an interface for converting responses into serialized format
"""


class ResponseConverter:
    """
    Create serialized format from response
    """

    def convertSerializedResponse(self, response):
        logging.error("convertSerializedResponse method of ResponseGenerator class has not implemented")
        raise NotImplementedError("Unimplemeted method")
