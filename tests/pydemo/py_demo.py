import pytest 
@pytest.fixture(scope="module")
def share_resource():
    print("\n>>>>>> Class fixture 初始化 <<<<<<")
    yield "共享资源"
    print("\n>>>>>> Class fixture 销毁 <<<<<<")

class TestExample:

    def test_case1(self):
        print("test_case1未使用fixture")

    def test_case2(self, share_resource):
        print(f"test_case2使用了{share_resource}")

def test_outside_class():
    print("\n非类测试方法不会触发 class 作用域 fixture")

@pytest.fixture(params=["apple", "banana"], ids=["苹果", "香蕉"])
def fruit(request):
    return request.param

def test_fruit(fruit):
    print(fruit)

if __name__ == "__main__":
    def compare_with_zero(num):
        if isinstance(num, str):
            if not num.isdigit():
                raise ValueError(f"字符串包含非数字字符：'{num}'")
            num = int(num)

        if not isinstance(num, (int, float)):
            raise TypeError(f"参数必须是数字或整数字符串，输入类型{type(num).__name__}")
        
        return num > 0
    
    import ast, random

    def get_random_ele(list):
        """
        随机返回list中的元素
        """
        if isinstance(list, str):
            list = ast.literal_eval(list)   
        try:
            random_ele = random.choice(list)
            return random_ele
        except IndexError:
            return None

    list = "[1, 2, 'apple', True]"
    print(get_random_ele(list))