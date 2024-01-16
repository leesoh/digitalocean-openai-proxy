import logging

from flask import Flask, request
from openai import OpenAI

from tools.extwis import extwis
from util.auth import token_required

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)


@app.route("/extwis", methods=["POST"])
@token_required
def hello_world():
    logging.info("running extwis")
    resp = extwis.send(request.data.decode("utf-8"))
    logging.info("response received")
    return resp.encode("utf-8")
