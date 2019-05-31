from .VersionedResponseV1 import VersionedResponseV1

"""
Factory to create various response representations.
"""


class ResponseFactory:
    """
    Version 1 of complete response representation that contains version information and result.
    """

    @staticmethod
    def createResponseV1(result):
        return VersionedResponseV1(result)
