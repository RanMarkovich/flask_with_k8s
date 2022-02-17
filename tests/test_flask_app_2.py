import requests


def test_hello_world():
    r = requests.get('http://localhost:5001/ran')
    assert r.text == 'hello ran!'
