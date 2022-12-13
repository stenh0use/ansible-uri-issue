from flask import Flask

app = Flask(__name__)

@app.route('/<int:code>')
def status(code):
    return '{"hello": "world"}', code, {'Content-Type': 'application/json'}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
