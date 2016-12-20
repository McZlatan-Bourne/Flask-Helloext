#!/usr/bin/env python

from flask import Flask
from flask_helloext import HelloExt

app = Flask(__name__)
flask=HelloExt(app)

@app.route('/')
def helloFlask():
    return flask.sayHello()


if __name__ == '__main__':
    app.run(debug=True)
