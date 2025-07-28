def test_username(parametrized_username):
    assert parametrized_username in ['one', 'two', 'three']

def test_parametrized_username(non_parametrized_username):
    assert non_parametrized_username == 'username'