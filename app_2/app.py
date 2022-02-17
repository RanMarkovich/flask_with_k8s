from flask import Flask

app = Flask(__name__)


@app.route('/<name>')
def hello_world(name):
    return f'hello {name}!', 200


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)
