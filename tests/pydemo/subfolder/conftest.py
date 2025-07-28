import pytest

# 重写上级目录conftest文件中的 username fixture
@pytest.fixture
def username(username):
    return 'overridden-' + username