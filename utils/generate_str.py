import string, random
from datetime import datetime


def get_random_str(length = 8):
    if not isinstance(length, int) or length <= 0:
        raise ValueError("长度必须为正整数")
        
    # 生成字符池：字母（大小写） + 数字
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

def get_random_number(digits = 8):
    if not isinstance(digits, int):
        raise ValueError("位数必须为正整数")
    return ''.join(random.choices('0123456789', k=digits))

def get_specified_prefix_str(s):
    """
    获取指定字符串
    """
    return s+ '_' + get_random_str()

def get_current_day(format='%Y-%m-%d'):
    return datetime.now().strftime(format)

if __name__  == '__main__':
    current_day = get_current_day("%Y年%-m月%-d日")
    print(current_day)