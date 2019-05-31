from flask import Flask, request
from requesthandler.RequestHandlerFactory import RequestHandlerFactory
import logging
import sys

app = Flask(__name__)

logging.basicConfig(stream=sys.stderr, format='%(asctime)s - %(process)d - %(message)s', level=logging.DEBUG)

requestHandlerFactory = RequestHandlerFactory()


@app.route("/urlinfo/1/<path:text>", methods=['GET'])
def getUrlInfoV1(text):
    entireUrl = request.url
    pathPrefix = "/urlinfo/1/"

    indexOfExpectedUrlToQuery = entireUrl.find(pathPrefix)
    urlToQuery = entireUrl[indexOfExpectedUrlToQuery + len(pathPrefix):]

    logging.info("Request received for information about url: %s" % urlToQuery)

    responseHandler = requestHandlerFactory.createUrlInfoRequestHandlerV1()
    response = responseHandler.getSerializedResponse(urlToQuery)

    if response == None:
        return "Internal error when handling url information request, url:" % urlToQuery, 500

    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
