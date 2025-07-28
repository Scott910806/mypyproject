import pytest

@pytest.fixture
def parametrized_username():
    return 'overridden-username'

@pytest.fixture(params=['one', 'two', 'three'])
def non_parametrized_username(request):
    return request.param

def test_username(parametrized_username):
    assert parametrized_username == 'overridden-username'

def test_parametrized_username(non_parametrized_username):
    assert non_parametrized_username in ['one', 'two', 'three']

@pytest.mark.parametrize('username', ['directly-overriden-username'])
def test_username_pro(username):
    assert username == 'directly-overriden-username'

@pytest.mark.parametrize('username', ['directly-overriden-username-other'])
def test_username_other(other_username):
    assert other_username == 'other-directly-overriden-username-other'