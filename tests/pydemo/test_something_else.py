import pytest
import json
from pathlib import Path

def test_username(parametrized_username):
    assert parametrized_username in ['one', 'two', 'three']
@pytest.mark.smoke
def test_parametrized_username(non_parametrized_username):
    assert non_parametrized_username == 'username'

@pytest.mark.parametrize('test_input, expected',[(3+5, 8), pytest.param(6*7, 42, marks=pytest.mark.xfail)])
def test_eval(test_input, expected):
    assert test_input == expected
@pytest.mark.parametrize('i', range(50))
def test_num(i):
    if i in (17, 25):
        pytest.fail('bad luck')

# 从josn文件中读取参数，进行参数化
def load_json_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)
    
parent_dir = Path(__file__).resolve().parents[1]
json_data_path = parent_dir / 'test_data' / 'demo.json'
json_data = load_json_data(json_data_path)
params_list = [(item['a'], item['b'], item['expected']) for item in json_data]
@pytest.mark.parametrize('a, b, expected', params_list)
def test_add(a, b, expected):
    assert a + b == expected