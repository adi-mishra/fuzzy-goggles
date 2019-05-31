from .PrettyJsonResponseConverter import PrettyJsonResponseConverter

"""
Factory to create various response converters.
"""


class ResponseConverterFactory:
    """
    Creates a response converter for converting responses into human readable serialized format.
    """

    @staticmethod
    def createPrettyJsonConverter():
        return PrettyJsonResponseConverter()
