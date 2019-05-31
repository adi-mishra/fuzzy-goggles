import logging
from errors.StoreError import StoreError
from errors.JSONBadRequest import JSONBadRequest

"""
Class intended to be an interface for url blacklist RequestHandlers
"""


class UrlBlacklistRequestHandlerV1:
    def __init__(self, urlStore):
        self._urlStore = urlStore

    """
    Sets supplied url as part of request as blacklisted and unsafe.
    Returns valid response to be sent back to the user.
    """

    def handleRequest(self, request):
        try:
            urlToBlacklistJson = request.get_json(force=True)
        except JSONBadRequest:
            logging.warning("payload is not parse-able as json")
            return "Payload needs to be json and contain url key intended to be blacklisted", 400

        if 'url' not in urlToBlacklistJson:
            logging.warning("payload json does not contain url key, json payload: %s" % urlToBlacklistJson)
            return "Payload needs to be json and contain url key intended to be blacklisted", 400

        urlToBlacklist = urlToBlacklistJson['url']

        if urlToBlacklist == "":
            return "Payload needs to contain the url intended to be blacklisted", 400

        logging.info("Request received to blacklist url: %s" % urlToBlacklist)

        try:
            self._urlStore.addUrlToBlacklist(urlToBlacklist)
        except StoreError:
            return "Internal error when handling url to be blacklisted, url: %s" % urlToBlacklist, 500
        else:
            return ""
