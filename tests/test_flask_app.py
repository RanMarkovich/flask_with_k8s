import requests


def test_hello_world():
    r = requests.get('http://localhost:5000')
    assert r.text == 'hello world!'
