from .Response import Response

"""
Version 1 representation of response that contains version and result.
"""


class VersionedResponseV1(Response):
    def __init__(self, result):
        self._result = result

    """
    Get representation of this response object that can be serialized
    """

    def getSerializableResponse(self):
        serializableResult = self._result.getSerializableResult()
        serializableResponse = {"version": "1.0", "result": serializableResult}
        return serializableResponse
