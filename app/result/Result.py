import logging

"""
Interface class to represent Result from processing request.
"""


class Result:
    """
    Get serializable representation of result object.
    """

    def getSerializableResult(self):
        logging.error("getSerializableResult method of Result class has not implemented")
        raise NotImplementedError("Unimplemeted method")
