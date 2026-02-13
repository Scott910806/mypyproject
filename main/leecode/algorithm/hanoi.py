# !usr/bin/env python3
# -*- codding : utf-8 -*-

from functools import reduce
def mov(n, a, b, c):
    if n == 1:
        print(a, '->', c)
    else:
        # 先把n-1个盘子借助c由a移动到b
        mov(n - 1, a, c, b)
        # 把最后一个盘子由a移动到c
        print(a, '->', c)
        # 把b上面的盘子借助a移动到c
        mov(n - 1, b, a, c)

def trim_str(str):
    """
    自定义函数去除字符串首尾空格
    :return: 将去除首尾空格的字符串返回
    """
    start = 0
    while start < len(str) and str[start]== ' ':
        start += 1
    end = len(str)-1
    while end >= 0 and str[end]== ' ':
        end -= 1
    if start > end:
        return ''
    return str[start:end+1]

def findMinAndMax(L):
    """
    查找一个List中的最大和最小值
    :return: 返回List中的最小值和最大值, 以元组的形式
    """
    if len(L) == 0:
        return (None, None)
    min = L[0]
    max = L[0]
    for item in L:
        if item < min:
            min = item
        if item > max:
            max = item
    return (min, max)

def str2float(s):
    """
    将字符串转换为浮点数
    :param s: 字符串
    :return: 返回浮点数
    """
    def char2num(s):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,'9': 9}
        return digits[s]
    
    # 将字符串分为整数、小数部分
    parts = s.split('.')
    integer_part = parts[0]
    # 不存在小数部分时，记得返回空字符串，此时map接收到的可迭代对象为空，不会进行调用函数的操作，避免了keyError的报错
    decimal_part = parts[1] if len(parts) > 1 else ''
    # 转换整数部分
    int_num = reduce(lambda x, y: x*10 + y, map(char2num, integer_part))
    # 转换小数部分
    dec_mum = reduce(lambda x, y: x*10 + y, map(char2num, decimal_part)) / 10**len(decimal_part) if decimal_part else 0
    # 拼装整数和小数部分，并返回
    return int_num + dec_mum

def is_palindrome(n):
    """
    过滤函数,判断一个数是否为回数
    return: bool
    """
    s = str(n)
    return s == s[::-1]

def _add_iter():
    """
    构造一个3开头的奇数列
    """
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x : x % n > 0

def primes():
    """
    通过埃氏筛法求素数
    """
    yield 2
    it = _add_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


if __name__ == '__main__':
    # mov(3, 'A', 'B', 'C')
    # L1 = ['Hello', 'World', 18, 'Apple', None]
    # L2 = [s.lower() for s in L1 if isinstance(s, str)]
    # print(L2)
    # print("yXMa".capitalize())
    # print(str2float("123"))
    print(list(filter(is_palindrome, range(1, 200))))
    for i in primes():
        print(i)
        if i > 100:
            break
    