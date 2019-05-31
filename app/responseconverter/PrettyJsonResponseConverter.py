from .ResponseConverter import ResponseConverter
import json

"""
Converts Response into human readable json format.
"""


class PrettyJsonResponseConverter(ResponseConverter):
    """
    Convert response into human readable json format
    """

    def convertSerializedResponse(self, response):
        return json.dumps(response.getSerializableResponse(), sort_keys=True, indent=4)
