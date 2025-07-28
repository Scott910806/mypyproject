# username取的是当前层级conftest.py文件（遵循就近原则）中重写后的username
def test_username(username):
    assert username == 'overridden-username'