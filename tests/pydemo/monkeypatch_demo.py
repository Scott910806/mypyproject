import requests
import os
import pytest

def get_os_user_lower():
    username = os.getenv('USER')
    if username is None:
        raise OSError('USER environment variable not set')
    return username.lower()

def get_json(url):
    r = requests.get(url)
    return r.json()

class MockResponse:
    @staticmethod
    def json():
        return {
            "name": "MOCK_NAME",
            "age": 18
        }    
    
def test_get_json(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse()
    
    monkeypatch.setattr(requests, 'get', mock_get)
    r = get_json('https://fakeurl')
    assert r['name'] == 'MOCK_NAME'

def test_upper_to_lower(mock_env_user):
    assert get_os_user_lower() == "mocked-username"

def test_upper_to_lower_missing(mock_env_user_missing):
    with pytest.raises(OSError):
        _ = get_os_user_lower()