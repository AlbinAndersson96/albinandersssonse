import json
import os

from flask import Flask, request, render_template

from gevent.pywsgi import WSGIServer

import smtplib, ssl

app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/static/client.html', methods=['GET'])
def root():
    return render_template('client.html')

@app.errorhandler(404)
def pageNotFound(error):
    return 'four oh four'

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    http_server = WSGIServer(('0.0.0.0', port), app)
    http_server.serve_forever()