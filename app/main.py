from flask import Flask, request, Request
from requesthandler.RequestHandlerFactory import RequestHandlerFactory
from errors.JSONBadRequest import JSONBadRequest
import logging
import sys

app = Flask(__name__)

logging.basicConfig(stream=sys.stderr, format='%(asctime)s - %(process)d - %(message)s', level=logging.DEBUG)

requestHandlerFactory = RequestHandlerFactory()


def on_json_loading_failed(self, error):
    raise JSONBadRequest()


Request.on_json_loading_failed = on_json_loading_failed


@app.route("/urlinfo/1/<path:text>", methods=['GET'])
def getUrlInfoV1(text):
    responseHandler = requestHandlerFactory.createUrlInfoRequestHandlerV1()
    response = responseHandler.handleRequest(request)
    return response


@app.route("/blacklist/1", methods=['POST'])
def postUrlBlacklistV1():
    responseHandler = requestHandlerFactory.createUrlBlacklistRequestHandlerV1()
    response = responseHandler.handleRequest(request)
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
