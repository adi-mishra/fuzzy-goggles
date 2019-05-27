from flask import Flask
import socket
import logging
import sys

app = Flask(__name__)

logging.basicConfig(stream=sys.stderr, format='%(asctime)s - %(process)d - %(message)s', level=logging.DEBUG)


@app.route("/")
def index():
    logging.debug("Received request with empty resource path")
    return "Hello world. My Hostname is: %s \n" % (socket.gethostname())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
