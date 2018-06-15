from flask import Flask
from flask import render_template
from flask import request
from twisted.web.wsgi import WSGIResource
from twisted.web.server import Site
from twisted.internet import reactor
from arachne import Arachne



app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello():
    return render_template('home.html', name=None)


@app.route('/start', methods=['POST', 'GET'])
def start():
    params = {}
    params['url'] = request.form['url']
    return render_template("home.html", name=params)


if __name__ == '__main__':
    app.debug = True
    app.run()
