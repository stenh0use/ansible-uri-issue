from flask import Flask

app = Flask(__name__)

headers = {
    'Content-Type': 'application/json'
}

body = '{ "hello": "world" }'

@app.route("/200")
def sc_200():
    return (body, 200, headers)

@app.route("/429")
def sc_429():
    return (body, 429, headers)

@app.route("/501")
def sc_501():
    return (body, 501, headers)

@app.route("/503")
def sc_503():
    return (body, 503, headers)
