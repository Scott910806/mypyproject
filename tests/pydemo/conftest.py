# conftest.py 是pytest框架中具有特殊意义的配置文件，pytest会自动加载该文件，支持在不同层级中定义（遵循就近优先原则）

import  pytest

@pytest.fixture
def username():
    return 'username'

@pytest.fixture
def other_username(username):
    return 'other-' + username

@pytest.fixture(params=['one', 'two', 'three'])
def parametrized_username(request):
    return request.param

@pytest.fixture
def non_parametrized_username():
    return 'username'